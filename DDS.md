# Design Document Specification (DDS)

## 1. Project Goals and Milestones
* **Milestone 1:** Complete Feature Extraction module (converting sequences to numbers).
* **Milestone 2:** Generate Training Dataset (clean and merge IEDB and UniProt data).
* **Milestone 3:** Train Random Forest Classifier and achieve baseline accuracy.

## 2. Module Architecture
The project is divided into four modules:

### Module 1: `data_loader`
* **Scope:** Handles reading raw files (CSV, FASTA) and cleaning the data.
* **Content:** Functions to parse IEDB CSVs, read FASTA files, and remove sequences with invalid characters.
* **Connections:** Passes cleaned lists of strings to the `feature_extractor`.

### Module 2: `feature_extractor`
* **Scope:** The mathematical engine of the project.
* **Content:** Functions to calculate physicochemical properties (GRAVY, Molecular Weight, Isoelectric Point) using Biopython.
* **Connections:** Receives strings from `data_loader`, outputs a Pandas DataFrame of numbers to `model_trainer`.

### Module 3: `model_trainer`
* **Scope:** Handles the Machine Learning logic.
* **Content:** Scikit-learn implementation of the Random Forest Classifier, including splitting data into Train/Test sets.
* **Connections:** Receives DataFrame from `feature_extractor`, saves the trained model to a file.

### Module 4: `predictor`
* **Scope:** The user-facing script.
* **Content:** A Command Line Interface (CLI) that accepts a new sequence, runs it through `feature_extractor`, and asks the saved model for a prediction.
