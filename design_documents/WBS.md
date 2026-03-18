# Work Breakdown Structure (WBS)

## Activity 1: Unified Feature Extraction Module
**Goal:** Calculate all required physiochemical properties (GRAVY, Molecular weight, isoelectric point, aromaticity, and instability index) for a single input sequence efficiently using a single Biopython instantiation.

### Tasks:
1.  **Task 1.1: Environment Setup & Dependencies**
    * **Action:** Install the `biopython` library in the development environment.
    * **Deliverable:** A functional python environment where `from Bio.SeqUtils.ProtParam import ProteinAnalysis` executes without errors.
    * **Completion Criteria:** No error when running imports.

2.  **Task 1.2: Implement Consolidated Feature Logic**
    * **Action:** Create `feature_extractor.py` and write the `extract_all_features` function.
    * **Sub-action:** Instantiate `ProteinAnalysis` exactly once per sequence to extract all 5 properties into a dictionary.
    * **Deliverable:** A Python script containing the unified feature extraction function.
    * **Completion Criteria:** The function accepts a string (sequence) and returns a dictionary of 5 valid floats.

3.  **Task 1.3: Validate Output**
    * **Action:** Create an `if __name__ == "__main__":` block to test the function.
    * **Sub-action:** Test a sequence of known properties and print the resulting dictionary.
    * **Deliverable:** Output showing the 5 calculated scores for a test sequence.
    * **Completion Criteria:** The script runs successfully and prints valid numerical scores for all properties.

---

## Activity 2: Model Training Pipeline
**Goal:** Develop the machine learning engine that can clean datasets, read in numerical features, and output a trained classification model.

### Tasks:
1.  **Task 2.1: Negative Dataset Homology Filtering**
    * **Action:** Filter the UniProt non-allergen dataset to prevent data leakage.
    * **Sub-action:** Use a sequence clustering tool (e.g., CD-HIT) to remove sequences with high identity to the positive IEDB dataset.
    * **Deliverable:** A cleaned, filtered FASTA/CSV file of strictly non-homologous negative sequences.
    * **Completion Criteria:** The negative dataset size is visibly reduced, and no sequence shares high identity with the positive set.

2.  **Task 2.2: Data Splitting**
    * **Action:** Implement dataset partitioning.
    * **Sub-action:** Write a function that randomly splits the data into 80% Training and 20% Testing sets.
    * **Deliverable:** Two separate variables/files ready for processing.
    * **Completion Criteria:** The row count of the training set is exactly 80% of the total input.

3.  **Task 2.3: Classifier Implementation**
    * **Action:** Implement and train a Random Forest Classifier.
    * **Sub-action:** Write a function that fits the model to the training data.
    * **Deliverable:** A python object containing the fitted model with learned weights.
    * **Completion Criteria:** The code executes without errors.

4.  **Task 2.4: Save Model**
    * **Action:** Save the trained model for later use.
    * **Sub-action:** Export the model object.
    * **Deliverable:** File of the exported model object.
    * **Completion Criteria:** The file exists on the disk and can be successfully loaded back into Python.

---

## Activity 3: Evaluation Metrics
**Goal:** Visualize and quantify the performance of the model using robust metrics to determine if it accurately classifies imbalanced biological data.

### Tasks:
1.  **Task 3.1: Generate Predictions**
    * **Action:** Run the trained model against the 20% "held-out" Test set.
    * **Sub-action:** Create a list of predicted labels for the test data.
    * **Deliverable:** An array of integers representing the model's guesses.
    * **Completion Criteria:** The length of the prediction array matches the length of the test set.

2.  **Task 3.2: Confusion Matrix Visualization**
    * **Action:** Create a visual representation of True Positives vs False Positives.
    * **Sub-action:** Generate a heatmap.
    * **Deliverable:** A PNG image file.
    * **Completion Criteria:** The image is generated and displays all four quadrants (TP, TN, FP, FN).

3.  **Task 3.3: Calculate Robust Evaluation Metrics**
    * **Action:** Evaluate the model's performance beyond simple accuracy.
    * **Sub-action:** Compute the F1-Score, AUROC, and the Random Forest Out-of-Bag (OOB) error.
    * **Deliverable:** A printed classification report detailing these specific metrics.
    * **Completion Criteria:** The script successfully outputs valid float scores (0.0 to 1.0) for F1, AUROC, and OOB error.

---

## Activity 4: CLI Development
**Goal:** Create a command-line interface that allows a user to type a protein sequence and get an immediate prediction.

### Tasks:
1.  **Task 4.1: Argument Parsing**
    * **Action:** Set up script/implement a library to handle user inputs.
    * **Sub-action:** Define a required argument that accepts a string.
    * **Deliverable:** A script that can be run.
    * **Completion Criteria:** The script accepts and stores the string in a variable.

2.  **Task 4.2: End-to-End Prediction**
    * **Action:** Connect the CLI input to the pre-trained model.
    * **Sub-action:** Pass the user's string through `feature_extractor.py`, then pass those numbers to the loaded model.
    * **Deliverable:** A printed statement to the console: "Prediction: Allergen (X% Confidence)".
    * **Completion Criteria:** Running the command on a known allergen sequence returns "Allergen".
