import os
import sys
import joblib
import pandas as pd
import warnings

# Suppress routine warnings for a cleaner terminal experience
warnings.filterwarnings('ignore')

# Import feature extractor
try:
    from allergen_predictor.feature_extractor import extract_all_features
except ModuleNotFoundError:
    print("Error: Could not find the 'allergen_predictor' module.")
    print("Ensure you are running this script from the root directory of the project.")
    sys.exit(1)

def main():
    print("Allergen-Predictor: Command Line Interface")

    model_path = os.path.join("data", "allergen_rf_model.pkl")

    print("\nLoading production Random Forest model.")
    try:
        prod_clf = joblib.load(model_path)
        print("Model loaded successfully. Engine ready.\n")
    except FileNotFoundError:
        print(f"Error: Could not find the trained model at {model_path}.")
        print("Please run model_pipeline.py first to generate the .pkl file.")
        sys.exit(1)

    # Use a while loop so the tool stays open for multiple tests
    while True:
        test_sequence = input("Paste an amino acid sequence to test (or type 'quit' to exit):\n> ").strip().upper()

        if test_sequence == 'QUIT' or test_sequence == 'Q':
            print("\nAllergen-Predictor successfully quit.")
            break

        if not test_sequence:
            print("Error: No sequence entered. Please try again.")
            continue

        try:
            print("\nExtracting physicochemical properties via Biopython.")
            
            # Extract features
            test_features = pd.DataFrame([extract_all_features(test_sequence)])
            
            # Make prediction
            prediction = prod_clf.predict(test_features)
            probabilities = prod_clf.predict_proba(test_features)[0] 
            
            allergen_prob = probabilities[1]
            safe_prob = probabilities[0]
            
            print("\n" + "=" * 30 + " RESULTS " + "=" * 30)
            
            if prediction[0] == 1:
                print("Prediction: Allergen")
            else:
                print("Prediction: Non-Allergen")
            
            # Print the percentage split
            print(f"Model percentage split: {safe_prob * 100:.1f}% Safe  |  {allergen_prob * 100:.1f}% Allergen")
            
            print("=" * 69 + "\n")
                
        except Exception as e:
            print(f"\nError: Failed to process sequence.")
            print(f"Details: {e}\n")

if __name__ == "__main__":
    main()