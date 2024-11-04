import httpx
import jwt
import datetime

import jwt.exceptions

from config import settings


class Session:
    def __init__(self):
        self.refresh_token = ""
        self.access_token = ""
        self.refresh_session()

    def refresh_session(self):
        print("Refreshing refresh token ...")
        self.get_refresh_token()

        print("Refreshing access token ...")
        self.get_access_token()

    def get_refresh_token(self) -> str:
        response = httpx.post(
            f"{settings.API_BASE}/auth/agents/{settings.AGENT_ID}/token",
            headers={
                "Content-Type": "application/json",
                "X-Api-Key": settings.AGENT_KEY,
            },
            json={},
        )
        response.raise_for_status()  # Raises an error for bad responses
        self.refresh_token = response.json().get("refresh_token")

    def get_access_token(self) -> str:
        response = httpx.put(
            f"{settings.API_BASE}/auth/agents/{settings.AGENT_ID}/token",
            headers={
                "Content-Type": "application/json",
                "X-Api-Key": settings.AGENT_KEY,
            },
            params={"refresh_token": self.refresh_token},
        )
        response.raise_for_status()  # Raises an error for bad responses
        self.access_token = response.json().get("access_token")
        self.is_expired(self.access_token)

    @staticmethod
    def is_expired(token: str) -> bool:
        if not token:
            return True
        try:
            # Decode the token without verifying (you might want to verify in a real scenario)
            decoded = jwt.decode(
                token, options={"verify_signature": False, "verify_exp": True}
            )
            # Get the expiration time
            exp_timestamp = decoded.get("exp")
            if exp_timestamp:
                # Convert to datetime
                expiration_time = datetime.datetime.fromtimestamp(exp_timestamp)
                print(f"The JWT expires at: {expiration_time}")
            else:
                print("No expiration time found in the token.")
        except jwt.ExpiredSignatureError:
            print("The token has already expired.")
            return True
        except Exception as e:
            print(e)
            raise e

        return False
