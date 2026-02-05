# Specification document for the Allergen Predictor Project

## 1. Project Overview
The **Allergen-Predictor** is a machine learning-based bioinformatics tool designed to assess the allergenic potential of novel protein sequences. Unlike alignment-based methods that look for exact sequence matches, this tool predicts allergenicity based on specific properties (hydrophobicity, molecular weight, isoelectric point), allowing it to identify potential risks in novel proteins with low sequence similarity to known allergens.

## 2. Goals
* **Primary Goal:** To classify an input amino acid sequence as "Allergenic" or "Non-Allergenic" with >80% accuracy.
* **Secondary Goal:** To identify which features/properties (hydrophobicity vs. charge) contribute most to the prediction.

## 3. System Features and Use Cases
1.  **Data Input:** The system will accept protein sequences in FASTA format or raw text strings.
2.  **Feature Extraction:** The system will calculate the properties into numerical format (e.g., GRAVY score, Isoelectric Point) for every input sequence.
3.  **Prediction:** The system will output a binary classification (Allergen/Non-Allergen) and a probability score for the input.
4.  **Training Interface:** The system will allow retraining of the underlying model using new CSV datasets from IEDB or UniProt.
