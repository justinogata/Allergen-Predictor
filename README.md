# Allergen-Predictor

## Biological Question
Can we predict the allergenicity of a novel protein based on its physicochemical properties, even if it has no sequence homology to known allergens?

## Project Description
The Allergen-Predictor is a machine learning classifier designed to assess the allergenic potential of novel proteins. Unlike traditional alignment methods that require exact matches to known databases, this tool uses a **Random Forest Classifier** trained on physicochemical properties (hydrophobicity, charge, molecular weight) to predict the likelihood that a new protein sequence is an allergen.

## Input
* **Training Data for the model:**
    * `IEDB_positive.csv`: A list of confirmed allergen sequences from Immune Epitope Database (IEDB)
    * `UniProt_negative.fasta`: A list of non-allergenic protein sequences from UniProt

## Output
* **Format:** Prediction Score.
* **Data:**
    * **Class:** "Allergen" or "Non-Allergen"
    * **Confidence Score:** A probability value
    * **Feature Importance:** A chart showing which properties contributed most to the decision

## Usage Recommendations
Allergen-Predictor is specifically designed to identify novel allergens by analyzing physiochemical properties rather than relying on sequence homology. Because of this, it serves as a complementary approach to traditional methods. For the most comprehensive analysis and highest confidence results, it is highly recommended to use this tool in conjunction with standard sequence-alignment tools, such as BLAST or FASTA-based searches, rather than a replacement.
