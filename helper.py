"""API keys for the notebooks.

Keys are read from environment variables so they never end up in Git.
Set them in your shell before starting Jupyter, for example:

    export GEMINI_API_KEY="your-key"
"""
import os


def get_openai_api_key():
    return os.environ.get("OPENAI_API_KEY", "")


def get_gemini_api_key():
    return os.environ.get("GEMINI_API_KEY", "")
