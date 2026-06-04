import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the main web interface."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles variant analysis requests.
    Expects JSON input with a 'variant' key.
    """
    try:
        data = request.json or {}
        variant_name = data.get('variant', '').strip()

        if not variant_name:
            return jsonify({"error": "No variant provided"}), 400

        # Mocking the BRCA1 response from your research paper
        if "BRCA1" in variant_name.upper():
            response = {
                "variant": variant_name,
                "classification": "PATHOGENIC",
                "score": 0.96,
                "reasons": [
                    {"feature": "Protein-protein interface disrupted (BRCA1 can no longer bind its repair partners)", "impact": "+0.24"},
                    {"feature": "Extreme evolutionary constraint (This position unchanged across 500M years)", "impact": "+0.13"},
                    {"feature": "Located in catalytic domain (Core functional region of the protein)", "impact": "+0.06"}
                ]
            }
        # Mocking the TTN response from your research paper
        else:
            response = {
                "variant": variant_name,
                "classification": "BENIGN",
                "score": 0.08,
                "reasons": [
                    {"feature": "Intrinsically disordered surface region (Flexible part, substitutions tolerated)", "impact": "-0.28"},
                    {"feature": "Observed in healthy primates (Common in non-human primate populations)", "impact": "-0.15"},
                    {"feature": "Low evolutionary constraint (Position varies freely across species)", "impact": "-0.07"}
                ]
            }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Defaulting to Hugging Face's mandatory port 7860
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)
    
