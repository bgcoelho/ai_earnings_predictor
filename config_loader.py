# config_loader.py
import os
import yaml
from dotenv import load_dotenv

def load_config():
    """
    Loads both secrets (.env) and standard config (config.yaml)
    into a single dictionary for convenience.
    """
    # Load .env file
    load_dotenv()

    # Load YAML config
    with open("config.yaml", "r") as f:
        yaml_config = yaml.safe_load(f)

    # Merge environment variables and YAML settings
    config = {
        **yaml_config,
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "PINECODE_API_KEY": os.getenv("PINECONE_API_KEY"),
    }

    # Basic sanity check
    if not config["OPENAI_API_KEY"]:
        raise ValueError("OPENAI_API_KEY missing in .env")

    # Basic sanity check
    if not config["PINECONE_API_KEY"]:
        raise ValueError("PINECONE_API_KEY missing in .env")

    return config