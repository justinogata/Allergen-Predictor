# Datasets

## 1. Data Sources
To train the classifier, we require two distinct classes of data:

### Positive Class (Allergens)
* **Source:** Immune Epitope Database (IEDB).
* **Content:** Linear peptide epitopes known for inducing allergic reactions in humans. For IEDB database parameters, select "Linear peptide" for Epitope. "Positive" for Assay Outcome and "B Cell","T Cell", and "MHC Ligand" for Assay. "Human" for Host. "Allergic" for Disease.
* **Format:** CSV containing epitope sequences, the source organism, and assay results.
* **Size:** 10,858 unique epitope sequences.
* **Link:** https://www.iedb.org/result_v3.php?cookie_id=61ee31

### Negative Class (Non-Allergens)
* **Source:** UniProt (Swiss-Prot).
* **Content:** Reviewed human proteins explicitly *not* annotated with the keyword "Allergen."
* **Format:** FASTA file.
* **Size:** 573,620 sequences (These will be decreased to match the positive class size).
* **Link:** https://www.uniprot.org/uniprotkb?query=reviewed%3Atrue+AND+NOT+keyword%3Aallergen
* (Note: This file is too large for GitHub, so please download the file using the link.)

## 2. Data Validation & Preprocessing
* **Length Filter:** Both datasets will be filtered to include only sequences between 10 and 50 amino acids to ensure comparability.
* **Ambiguity Removal:** Sequences containing non-standard amino acid codes (B, J, Z, X) will be removed to prevent calculation errors.

### Example dataset for using the tool.
For demonstrating and testing the Allergen-Predictor, I am using a subset dataset located in the repository's `data/` folder. This dataset consists of two files: `subset_pos_file.csv` (containing the first 50 rows from the IEDB database) and `subset_neg_file.fasta` (contains 46 unique, non-allergenic UniProt sequences (filtered down from 50 to remove identical biological homologs)). These files are a small section of the full database inputs, making their structure identical to the full dataset files and requiring the exact same CSV and FASTA parsing logic. This is an ideal example dataset to run the tool on because its compact size of ~60Kb, which is < 20Mb. This allows users to rapidly execute the complete "happy path" from data loading and sequence validation to physiochemical feature extraction without experiencing the heavy computational processing times associated with the full biological datasets.

## 3. Real dataset for answering a biological question using the tool
* **Biological Question:** Can we predict the allergenicity of novel proteins based purely on their physicochemical properties (such as GRAVY score, molecular weight, and isoelectric point) without relying on sequence alignment to known allergens?
* **Dataset Description:** The positive dataset consists of 10,768 known allergen sequences sourced from the Immune Epitope Database (IEDB). The negative dataset consists of non-allergen sequences from UniProt. The original UniProt dataset contained 572,396 sequences, which was clustered and filtered using CD-HIT at an 80% identity threshold to prevent data leakage from evolutionary homologs, resulting in 274,375 unique clusters. A subset of 10,768 sequences from this filtered UniProt dataset was used to match the positive class size, resulting in a balanced, 21,536-row dataset.
* **URLs:** IEDB (https://www.iedb.org/), UniProt (https://www.uniprot.org/).
* **Justification:** This dataset is highly suitable for this tool because biological data is inherently prone to evolutionary data leakage. By utilizing CD-HIT to filter UniProt, we ensure the negative class is diverse and not artificially easy for the model to classify. The large positive class from IEDB provides a strong statistical foundation for the Random Forest classifier to find genuine physicochemical patterns.
* **Expected Results:** The expected result is a trained Random Forest model that achieves an F1-Score and AUROC of >0.85, indicating strong predictive capability. The actual pipeline execution resulted in an AUROC of 0.99, proving that physicochemical properties (specifically Molecular Weight) are accurate predictors of allergenicity.