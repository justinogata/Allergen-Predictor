# Allergen-Predictor

## Biological Question
Can we predict the allergenicity of a novel protein based on its properties, even if it has no sequence homology to known allergens?

## Project Description
The Allergen-Predictor is a machine learning classifier designed to assess the allergenic potential of novel proteins. Unlike traditional alignment methods (BLAST) that require exact matches to known databases, this tool uses a **Random Forest Classifier** trained on physicochemical properties (hydrophobicity, charge, molecular weight) to predict the likelihood that a new protein sequence is an allergen.

## Input
* **Training Data for the model:**
    * `positives.csv`: A list of confirmed allergen sequences from Immune Epitope Database (IEDB)
    * `negatives.csv`: A list of non-allergenic protein sequences from UniProt
* **User Input:**
    * `query.fasta`: The amino acid sequence of the new protein you want to test

## Output
* **Format:** Prediction Score.
* **Data:**
    * **Class:** "Allergen" or "Non-Allergen"
    * **Confidence Score:** A probability value
    * **Feature Importance:** A chart showing which properties contributed most to the decision
