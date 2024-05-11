from flask import Flask
from utils import install_spacy_model, load_spacy_model
import routes  # Make sure to import the routes module

app = Flask(__name__, static_url_path='/static')

# Preload the spaCy model at startup
install_spacy_model()  # Ensure the model is installed
nlp_model = load_spacy_model()  # Load the model

# Configure routes and pass the loaded nlp_model
routes.configure_routes(app, nlp_model)

if __name__ == '__main__':
    app.run(debug=True)
