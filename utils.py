import os
import spacy
import subprocess

def install_spacy_model():
    """Install the spaCy model if not already present."""
    model_name = os.getenv("SPACY_MODEL", "en_core_web_sm")
    try:
        spacy.load(model_name)
        print(f"Model '{model_name}' is already installed.")
    except OSError:
        print(f"Model '{model_name}' not found, installing...")
        subprocess.run(["python", "-m", "spacy", "download", model_name], shell=False)
        print(f"Model '{model_name}' installation complete.")

def load_spacy_model():
    """Load the spaCy model."""
    model_name = os.getenv("SPACY_MODEL", "en_core_web_sm")
    return spacy.load(model_name)
