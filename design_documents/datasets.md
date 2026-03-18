# Datasets

## 1. Data Sources
To train the classifier, we require two distinct classes of data:

### Positive Class (Allergens)
* **Source:** Immune Epitope Database (IEDB).
* **Content:** Linear peptide B-Cell epitopes known for inducing allergic reactions in humans.
* **Format:** CSV containing epitope sequences, the source organism, and assay results.
* **Size:** 10,858 unique epitope sequences.
* **Link:** https://www.iedb.org/result_v3.php?cookie_id=61ee31

### Negative Class (Non-Allergens)
* **Source:** UniProt (Swiss-Prot).
* **Content:** Reviewed human proteins explicitly *not* annotated with the keyword "Allergen."
* **Format:** FASTA file.
* **Size:** 573,620 sequences (These will be decreased to match the positive class size).
* **Link:** https://www.uniprot.org/uniprotkb?query=reviewed%3Atrue+AND+NOT+keyword%3Aallergen

## 2. Data Validation & Preprocessing
* **Length Filter:** Both datasets will be filtered to include only sequences between 10 and 50 amino acids to ensure comparability.
* **Ambiguity Removal:** Sequences containing non-standard amino acid codes (B, J, Z, X) will be removed to prevent calculation errors.

### Example dataset for using the tool.
For demonstrating and testing the Allergen-Predictor, I am using a subset dataset located in the repository's `data/` folder. This dataset consists of two files: `subset_positives.csv` (containing the first 50 rows from the IEDB database) and `subset_negatives.fasta` (containing the first 50 rows from the UniProt sequences, filtered to avoid close homologs). These files are a small section of the full database inputs, making their structure identical to the full dataset files and requiring the exact same CSV and FASTA parsing logic. This is an ideal example dataset to run the tool on because its compact size of ~1.3Mb, which is < 20Mb. This allows users to rapidly execute the complete "happy path" from data loading and sequence validation to physiochemical feature extraction without experiencing the heavy computational processing times associated with the full biological datasets.
