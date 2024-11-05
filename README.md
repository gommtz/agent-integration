# Project Setup Guide

This README file provides instructions for setting up and configuring the project on an Ubuntu system.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

If you don't have Python or pip installed, you can install them using the following commands:

```bash
sudo apt update
sudo apt install python3 python3-pip
```
Step 1: Create a Virtual Environment
To isolate your project dependencies, it's recommended to create a Python virtual environment. You can do this with the following command:

```bash
python3 -m venv venv
```
This will create a venv directory in your project folder that contains the virtual environment.

Step 2: Activate the Virtual Environment
Activate the virtual environment by running the following command:

``` bash
source venv/bin/activate
```

Once activated, your terminal prompt should change to show the environment name, typically (venv).

Step 3: Upgrade pip
It's always a good idea to upgrade pip to the latest version. Run this command to ensure you're using the latest version of pip:

```bash
pip install --upgrade pip
```

Step 4: Install Required Dependencies
Install the necessary Python packages by running the following command:

```bash
pip install httpx openai PyJWT
```
Alternatively, you can install the requirements.txt file:
```bash
pip install -r requirements.txt
```

Step 5: Create and Configure the .env File
You need to create a .env file in the root of your project directory to configure environment variables.

Create the .env file:
```bash
touch .env
```

Open the .env file in your text editor and add the following lines:

```bash
export DATA_AGENT_ID=<your_agent_id>
export DATA_CHATBOT_ID=<your_chatbot_id>
export AGENT_ENDPOINT=<your_agent_endpoint>
```
Replace <your_agent_id>, <your_chatbot_id>, and <your_agent_endpoint> with the actual values provided by the GenAI agent parameters you're using.

Load the .env file:
```bash
source .env
```

Step 6: Running the Application
Once you've set up the environment and installed the required dependencies, you can run your application. The exact command will depend on your project, but typically it will be something like:

```bash
python3 main.py
```
Make sure your virtual environment is activated when running the application.