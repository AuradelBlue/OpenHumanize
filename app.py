from flask import Flask, jsonify
from utils import install_spacy_model, load_spacy_model
import routes  # Make sure to import the routes module

app = Flask(__name__, static_url_path='/static')

# Preload the spaCy model at startup
try:
    install_spacy_model()  # Ensure the model is installed
    nlp_model = load_spacy_model() # Load the model
except Exception as e:
    app.logger.error(\"Failed to install or load spaCy model: {}\".format(e))
    # We could choose to halt the app or leave it running with limited functionality
    nlp_model = None

# Configure routes and pass the loaded nlp_model
if nlp_model:
    routes.configure_routes(app, nlp_model)
else:
    @app.route('/')
    def error():
        return jsonify({"error: \"The NPP model could not be loaded, please check the server logs for more details.\"}), 500

if __name__ == '__main__':
    app.run(debug=True)