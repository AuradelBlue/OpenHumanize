from flask import render_template, request, jsonify, Flask
import spacy

def configure_routes(app, model):
    global nlp
    nlp = model  # Set the global nlp model

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/parse', methods=['POST'])
    def parse_text():
        # Get the block of text from form data
        text = request.form['text']  # Assuming the form field is named 'text'

        # Parse the block of text into a document
        doc = nlp(text)

        # Split the document into sentences
        sentences = list(doc.sents)

        # Function to build the parse tree for each sentence
        def build_parse_tree(token, level=0):
            indent = "  " * level  # Create indentation
            subtree = {"text": token.text, "dep": token.dep_, "children": []}
            for child in token.children:
                subtree['children'].append(build_parse_tree(child, level + 1))
            return subtree

        # Build and collect parse trees for each sentence
        trees = []
        for sentence in sentences:
            root = [token for token in sentence if token.head == token][0]  # Find the root of the parse tree
            tree = build_parse_tree(root)
            trees.append(tree)

        # Return the parse trees as JSON
        return jsonify(trees)
