import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the main frontend UI."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives variant data from the frontend and returns mock explanations.
    """
    data = request.json
    variant_name = data.get('variant', '')

    # Mocking the BRCA1 response from your research paper
    if "BRCA1" in variant_name.upper():
        response = {
            "variant": variant_name,
            "classification": "PATHOGENIC",
            "score": 0.96,
            "reasons": [
                {"feature": "Protein-protein interface disrupted", "impact": "+0.24"},
                {"feature": "Extreme evolutionary constraint", "impact": "+0.13"},
                {"feature": "Located in catalytic domain", "impact": "+0.06"}
            ]
        }
    else:
        # Mocking the TTN response
        response = {
            "variant": variant_name,
            "classification": "BENIGN",
            "score": 0.08,
            "reasons": [
                {"feature": "Intrinsically disordered surface region", "impact": "-0.28"},
                {"feature": "Observed in healthy primates", "impact": "-0.15"},
                {"feature": "Low evolutionary constraint", "impact": "-0.07"}
            ]
        }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
