# Work Breakdown Structure (WBS)

## Activity 1: Compute First Feature
**Goal:** Compute the "Grand Average of Hydropathy" (GRAVY) score for a single input sequence using the Biopython library.

### Tasks:
1.  **Task 1.1: Environment Setup & Dependencies**
    * **Action:** Install the `biopython` library in the development environment.
    * **Deliverable:** A functional python environment where `from Bio.SeqUtils.ProtParam import ProteinAnalysis` executes without errors.
    * **Completion Criteria:** No error when running imports.

2.  **Task 1.2: Implement Calculation Logic (Biopython)**
    * **Action:** Create a file named `feature_extractor.py`.
    * **Sub-action:** Write a function that uses Biopython to calculate the hydrophobicity score.
    * **Deliverable:** A Python script containing a function that calculates the hydrophobicity score of a sequence.
    * **Completion Criteria:** The function accepts a string (sequence) and returns a float (hydrophobicity score).

3.  **Task 1.3: Validate Output**
    * **Action:** Create a `if __name__ == "__main__":` block to test edge cases.
    * **Sub-action:** Test a sequence of known hydrophobicity and print the result.
    * **Deliverable:** Output showing the calculated score for a test sequence.
    * **Completion Criteria:** The script runs successfully and prints a valid numerical score (float) for the test sequence.

---

## Activity 2: Expand Feature Extraction Module
**Goal:** Update the code to calculate four more chemical numbers (Molecular weight, isoelectric point/charge, aromaticity/structure, and instability index) required for the Random Forest classifier.

### Tasks:
1.  **Task 2.1: Implement Weight and Charge Functions**
    * **Action:** Update `feature_extractor.py` to include molecular weight and isoelectric point.
    * **Sub-action:** Define two new functions that calculate molecular weight and isoelectric point.
    * **Deliverable:** The updated Python script containing these two additional function definitions.
    * **Completion Criteria:** Passing sequence returns a molecular weight.

2.  **Task 2.2: Implement Stability & Structural Functions**
    * **Action:** Add functions that estimate protein stability and structure.
    * **Sub-action:** Define functions for calculating aromaticity and instability index.
    * **Deliverable:** The updated Python script with the full set of 5 feature functions.
    * **Completion Criteria:** The instability index function returns a valid value for test sequences.

3.  **Task 2.3: Integrated Testing**
    * **Action:** Expand the main execution block (`if __name__ == "__main__":`) to validate all new features.
    * **Sub-action:** Add print statements to display the output of all 5 functions for a single test sequence.
    * **Deliverable:** Output showing all 5 numerical values when running the script.
    * **Completion Criteria:** The script runs without errors and produces valid floats for all 5 properties.

---

## Activity 3: Model Training Pipeline
**Goal:** Develop the machine learning engine that can read in numerical features and output a trained classification model.

### Tasks:
1.  **Task 3.1: Data Splitting**
    * **Action:** Implement dataset partitioning.
    * **Sub-action:** Write a function that randomly splits the data into 80% Training and 20% Testing sets.
    * **Deliverable:** Two separate variables/files ready for processing.
    * **Completion Criteria:** The row count of the training set is exactly 80% of the total input.

2.  **Task 3.2: Classifier Implementation**
    * **Action:** Implement and train a Random Forest Classifier.
    * **Sub-action:** Write a function that fits the model to the training data.
    * **Deliverable:** A python object containing the fitted model with learned weights.
    * **Completion Criteria:** The code executes without errors.

3.  **Task 3.3: Save Model**
    * **Action:** Save the trained model for later use.
    * **Sub-action:** Export the model object.
    * **Deliverable:** File of the exported model object.
    * **Completion Criteria:** The file exists on the disk and can be successfully loaded back into Python.

---

## Activity 4: Evaluation Metrics
**Goal:** Visualize the performance of the model to determine if it meets the project's accuracy goals.

### Tasks:
1.  **Task 4.1: Generate Predictions**
    * **Action:** Run the trained model against the 20% "held-out" Test set.
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
    * **Action:** Set up script/implement a library to handle user inputs.
    * **Sub-action:** Define a required argument that accepts a string.
    * **Deliverable:** A script that can be run.
    * **Completion Criteria:** The script accepts and stores the string in a variable.

2.  **Task 5.2: End-to-End Prediction**
    * **Action:** Connect the CLI input to the pre-trained model.
    * **Sub-action:** Pass the user's string through `feature_extractor.py`, then pass those numbers to the loaded model.
    * **Deliverable:** A printed statement to the console: "Prediction: Allergen (X% Confidence)".
    * **Completion Criteria:** Running the command on a known allergen sequence returns "Allergen".
