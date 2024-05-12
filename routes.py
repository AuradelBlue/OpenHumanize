from flask import request, jsonify, Flask, render_template

def configure_routes(app, model):
    global nlp
    nlp = model  # Set the global nlp model

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/parse', methods=['POST'])
    def parse_text():
        text = request.form['text']
        doc = nlp(text)
        return jsonify(build_simple_format(doc))

    def build_simple_format(doc):
        sentences = []
        for sent in doc.sents:
            sentence_details = {'text': sent.text, 'tokens': []}
            for token in sent:
                sentence_details['tokens'].append({"word": token.text, "dep": token.dep_, "pos": token.pos_})
            sentences.append(sentence_details)
        return sentences