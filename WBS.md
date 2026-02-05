# Work Breakdown Structure (WBS)

## Activity 1: Compute First Feature
**Goal:** Successfully compute the "Grand Average of Hydropathy" (GRAVY) score for a single input sequence using the standard Biopython library.

### Tasks:
1.  **Task 1.1: Environment Setup & Dependencies**
    * **Action:** Install the `biopython` library in the development environment.
    * **Deliverable:** A functional python environment where `from Bio.SeqUtils.ProtParam import ProteinAnalysis` executes without errors.
    * **Completion Criteria:** No `ModuleNotFoundError` when running imports.

2.  **Task 1.2: Implement Calculation Logic (Biopython)**
    * **Action:** Create a file named `feature_extractor.py`.
    * **Sub-action:** Define a function `calculate_hydrophobicity(sequence)` that initializes a `ProteinAnalysis` object and returns `.gravy()`.
    * **Deliverable:** A Python script containing the wrapper function for Biopython's GRAVY calculation.
    * **Completion Criteria:** The function accepts a string (sequence) and returns a float (gravy score).

3.  **Task 1.3: Validate Output**
    * **Action:** Create a `if __name__ == "__main__":` block to test edge cases.
    * **Sub-action:** Test a sequence of known hydrophobicity and print the result.
    * **Deliverable:** Output showing the calculated score for a test sequence.
    * **Completion Criteria:** The script runs and prints a value that matches the expected Kyte-Doolittle scale average.

---

## Activity 2: Expand Feature Extraction Module
**Goal:** Enhance the feature extraction script to calculate the full suite of physicochemical properties (Molecular Weight, Isoelectric Point, Aromaticity, and Instability Index) required for the Random Forest classifier.

### Tasks:
1.  **Task 2.1: Implement Physical Property Functions**
    * **Action:** Update `feature_extractor.py` to include physical descriptors.
    * **Sub-action:** Define two new functions that calculate molecular weight and isoelectric point.
    * **Deliverable:** The updated Python script containing these two additional function definitions.
    * **Completion Criteria:** Passing sequence "AAA" returns a molecular weight of ~231.2 Daltons.

2.  **Task 2.2: Implement Stability & Structural Functions**
    * **Action:** Add functions that estimate protein stability and structure.
    * **Sub-action:** Define functions for calculating aromaticity and instability index.
    * **Deliverable:** The updated Python script with the full set of 5 feature functions.
    * **Completion Criteria:** The instability index function returns a value > 40 (unstable) or < 40 (stable) for test sequences.

3.  **Task 2.3: Integrated Testing**
    * **Action:** Expand the main execution block (`if __name__ == "__main__":`) to validate all new features.
    * **Sub-action:** Add print statements to display the output of all 5 functions for a single test sequence.
    * **Deliverable:** Output showing a list of 5 distinct numerical values when running the script.
    * **Completion Criteria:** The script runs without errors and produces valid floats for all 5 properties.

---

## Activity 3: Model Training Pipeline
**Goal:** Develop the machine learning engine that can ingest numerical features and output a trained classification model.

### Tasks:
1.  **Task 3.1: Data Splitting**
    * **Action:** Implement dataset partitioning.
    * **Sub-action:** Write a function that divides the master dataframe into 80% Training and 20% Testing sets.
    * **Deliverable:** Two separate variables/files ready for processing.
    * **Completion Criteria:** The row count of the training set is exactly 80% of the total input.

2.  **Task 3.2: Classifier Implementation**
    * **Action:** Implement and train a Random Forest Classifier.
    * **Sub-action:** Write a function that fits the model to the training data.
    * **Deliverable:** A python object containing the fitted model with learned weights.
    * **Completion Criteria:** The code executes without errors.

3.  **Task 3.3: Model Serialization**
    * **Action:** Save the trained model to the hard drive for later use.
    * **Sub-action:** Export the model object.
    * **Deliverable:** File of the exported model object.
    * **Completion Criteria:** The file exists on the disk and can be successfully loaded back into Python.

---

## Activity 4: Evaluation Metrics
**Goal:** specific visualize the performance of the model to determine if it meets the project's accuracy goals.

### Tasks:
1.  **Task 4.1: Generate Predictions**
    * **Action:** Run the trained model against the "held-out" Test set.
    * **Sub-action:** Create a list of predicted labels for the test data.
    * **Deliverable:** An array of integers representing the model's guesses.
    * **Completion Criteria:** The length of the prediction array matches the length of the test.

2.  **Task 4.2: Confusion Matrix Visualization**
    * **Action:** Create a visual representation of True Positives vs False Positives.
    * **Sub-action:** Generate a heatmap.
    * **Deliverable:** A PNG image file.
    * **Completion Criteria:** The image is generated and displays all four quadrants (TP, TN, FP, FN).

---

## Activity 5: CLI Development
**Goal:** Create a command-line interface that allows a user to type a protein sequence and get an immediate prediction.

### Tasks:
1.  **Task 5.1: Argument Parsing**
    * **Action:** Implement a library to handle user inputs.
    * **Sub-action:** Define a required argument that accepts a string.
    * **Deliverable:** A script that can be run.
    * **Completion Criteria:** The script accepts and stores the string in a variable.

2.  **Task 5.2: End-to-End Prediction**
    * **Action:** Connect the CLI input to the pre-trained model.
    * **Sub-action:** Pass the user's string through `feature_extractor.py`, then pass those numbers to the loaded model.
    * **Deliverable:** A printed statement to the console: "Prediction: Allergen (X% Confidence)".
    * **Completion Criteria:** Running the command on a known allergen sequence returns "Allergen".
