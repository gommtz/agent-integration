from openai import OpenAI, AuthenticationError
from config import settings

from auth import Session


agent_endpoint = settings.AGENT_ENDPOINT + "/api/v1/"

agent_session = Session()

if __name__ == "__main__":
    client = OpenAI(base_url=agent_endpoint, api_key=agent_session.access_token)
    refreshed_session = False

    while True:
        try:
            if refreshed_session:
                refreshed_session = False
            else:
                prompt = input("User: ")

            # Streaming response
            response = client.chat.completions.create(
                model="n/a",
                messages=[{"role": "user", "content": prompt}],
                stream=True,  # Enable streaming
            )

            for chunk in response:
                print(chunk.choices[0].delta.content, end="", flush=True)

            print("")

        except AuthenticationError:
            agent_session.refresh_session()
            client = OpenAI(base_url=agent_endpoint, api_key=agent_session.access_token)
            refreshed_session = True
