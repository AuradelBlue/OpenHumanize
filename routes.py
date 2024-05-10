from flask import request, jsonify, render_template

def configure_routes(app, nlp_model):
    @app.route('/', methods=['GET'])
    def home():
        """Renders the homepage with a form for text input."""
        return render_template('index.html')

    @app.route('/process', methods=['POST'])
    def process_text():
        """Processes posted text and returns tokens as JSON and to the form."""
        text = request.form['text']
        if not text:
            return jsonify({"error": "No text provided"}), 400
        doc = nlp_model(text)
        tokens = [token.text for token in doc]
        return render_template('index.html', original_text=text, tokens=tokens)
