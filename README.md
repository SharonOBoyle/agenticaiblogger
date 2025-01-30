# README

This repository is an example of a basic CrewAI agentic AI application that creates a blog on a given topic.  

# Usage

Before running the scripts, you need to create a .env file from .env.example with an environment variable `GROQ_API_KEY` and replace `your_api_key` with your actual Groq API key.

Install python 3.11.11

Next, create a virtual environment:

For Mac/Linux users, you can do this in the terminal:

```
python3.11.11 -m venv venv
```

For Windows users, you can do this in the command prompt:

```
python3.11.11 -m venv venv
```

Then, activate the virtual environment:

For Mac/Linux users, you can do this in the terminal:

```
source venv/bin/activate
```

For Windows users, you can do this in the command prompt:

```
.\venv\Scripts\activate
```

After setting the environment variable and activating the virtual environment, you'll need to install the required dependencies listed in `requirements.txt`. You can do this with pip:

```
pip install -r requirements.txt
```

Then, you can run the main script with Python:

```
python src/main.py
```


# Contributing

If you'd like to contribute to this project, please feel free to submit a pull request or open an issue. We appreciate your help!

# License

This project is licensed under the terms of the MIT license.
