# Specification document for the Allergen Predictor Project

## 1. Project Overview
The **ML-Allergen-Predictor** is a machine learning-based bioinformatics tool designed to assess the allergenic potential of novel protein sequences. Unlike alignment-based methods (e.g., BLAST) that look for exact sequence matches, this tool predicts allergenicity based on physicochemical properties (hydrophobicity, molecular weight, isoelectric point), allowing it to identify potential risks in novel proteins with low sequence homology to known allergens.

## 2. Goals
* **Primary Goal:** To classify an input amino acid sequence as "Allergenic" or "Non-Allergenic" with >80% accuracy.
* **Secondary Goal:** To identify which physicochemical features (hydrophobicity vs. charge) contribute most to the prediction.

## 3. System Features
1.  **Data Input:** The system shall accept protein sequences in FASTA format or raw text strings.
2.  **Feature Extraction:** The system shall calculate numerical physicochemical properties (e.g., GRAVY score, Isoelectric Point) for every input sequence.
3.  **Prediction:** The system shall output a binary classification (Allergen/Non-Allergen) and a probability score for the input.
4.  **Training Interface:** The system shall allow retraining of the underlying model using new CSV datasets from IEDB or UniProt.
