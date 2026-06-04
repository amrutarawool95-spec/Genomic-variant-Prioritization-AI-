# Explainable AI for Genomic Variant Prioritization

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.9-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A transparent, web-based artificial intelligence tool designed to predict the pathogenicity of genomic missense variants. This application provides both a high-accuracy classification score and a plain-language, mechanistic explanation (via SHAP) for every prediction, closing the gap between AI accuracy and clinical transparency.

## 📖 About the Research
This tool is the official implementation of the research paper: **"An Explainable Artificial Intelligence Framework for Genomic Variant Prioritization and Pathogenicity Assessment"** by Amruta Subhash Rawool. 

While existing state-of-the-art tools operate as "black boxes," this framework utilizes an XGBoost classifier paired with a SHAP explainability module. It evaluates variants based on three distinct biological domains without relying on circular clinical labels:
* **Evolutionary Data:** Likelihood ratios and constraint indices across species.
* **Structural Data:** 3D coordinates (AlphaFold), hydrophobic core disruptions, and catalytic sites.
* **Population Data:** Allele frequencies in healthy human (gnomAD) and non-human primate populations.

The model was validated on 132,714 high-confidence ClinVar variants, achieving an **ROC-AUC of 0.94** and an **F1-score of 0.89**.

## 🚀 Features
* **Pathogenicity Scoring:** Outputs a clear probability score (0.0 to 1.0) classifying the variant as Pathogenic or Benign.
* **Mechanistic Reasoning:** Provides a feature-attribution breakdown explaining exactly *why* the model made its decision (e.g., "Protein-protein interface disrupted").
* **Clean UI:** A responsive, clinical-style web dashboard built with Flask and HTML/CSS.
* **Docker Ready:** Fully containerized for instant deployment on platforms like Hugging Face Spaces, Render, or Railway.

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Gunicorn
* **Machine Learning:** XGBoost, SHAP, Pandas, NumPy
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment:** Docker

## 💻 Local Installation & Setup

If you want to run this application on your local machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
