# Work Breakdown Structure (WBS)

## Activity 1: Compute First Feature (Hydrophobicity/GRAVY)
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
