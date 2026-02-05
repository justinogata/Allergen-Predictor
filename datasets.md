# Datasets

## 1. Data Sources
To train the classifier, we require two distinct classes of data:

### Positive Class (Allergens)
* **Source:** Immune Epitope Database (IEDB).
* **Content:** Linear peptide B-Cell epitopes known for inducing allergic reactions in humans.
* **Format:** CSV containing epitope sequences, the source organism, and assay results.
* **Size:** 10,858 unique epitope sequences.

### Negative Class (Non-Allergens)
* **Source:** UniProt (Swiss-Prot).
* **Content:** Reviewed human proteins explicitly *not* annotated with the keyword "Allergen."
* **Format:** FASTA file.
* **Size:** 573,620 sequences (These will be decreased to match the positive class size).

## 2. Data Validation & Preprocessing
* **Length Filter:** Both datasets will be filtered to include only sequences between 10 and 50 amino acids to ensure comparability.
* **Ambiguity Removal:** Sequences containing non-standard amino acid codes (B, J, Z, X) will be removed to prevent calculation errors.

## 3. Development data (Small)
For the development phase, we will use a **Subset Dataset** to ensure code efficiency:
* **subset_positives.csv:** The first 50 rows of the IEDB sequences.
* **subset_negatives.fasta:** The first 50 entries from the UniProt sequences.
This small dataset allows for rapid testing of the feature extraction functions to avoid long processing times.
