import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, roc_curve, auc

def evaluate_allergen_model(clf, X_test, y_test):
    """Generates standard ML evaluation metrics and charts."""
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)[:, 1] 

    print("Model Evaluation")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1-Score:  {f1_score(y_test, y_pred):.4f}")
    
    if hasattr(clf, 'oob_score_'):
        print(f"OOB Score: {clf.oob_score_:.4f}")

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                xticklabels=['Non-Allergen (0)', 'Allergen (1)'],
                yticklabels=['Non-Allergen (0)', 'Allergen (1)'])
    axes[0].set_ylabel('Actual Biological Label')
    axes[0].set_xlabel('Model Predicted Label')
    axes[0].set_title('Confusion Matrix Heatmap')

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    axes[1].plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    axes[1].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--') 
    axes[1].set_xlim([0.0, 1.0])
    axes[1].set_ylim([0.0, 1.05])
    axes[1].set_xlabel('False Positive Rate')
    axes[1].set_ylabel('True Positive Rate')
    axes[1].set_title('Receiver Operating Characteristic (ROC)')
    axes[1].legend(loc="lower right")

    plt.tight_layout()
    plt.show()

def plot_feature_importance(clf, feature_names):
    """Extracts and plots the importance of each feature."""
    importances = clf.feature_importances_
    std = np.std([tree.feature_importances_ for tree in clf.estimators_], axis=0)
    
    forest_importances = pd.Series(importances, index=feature_names).sort_values(ascending=True)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    forest_importances.plot.barh(xerr=std, ax=ax, color='teal', capsize=4)
    ax.set_title("Impact of Physiochemical Properties on Allergenicity")
    ax.set_xlabel("Mean Decrease in Impurity (Importance Score)")
    ax.set_ylabel("Extracted Feature")
    fig.tight_layout()
    plt.show()

def main():
    # 1. Load the data
    dataset_path = "data/master_dataset.csv"
    model_save_path = "data/allergen_rf_model.pkl"
    
    print(f"Loading dataset from {dataset_path}")
    df = pd.read_csv(dataset_path)
    
    # 2. Separate Features (X) and Labels (y)
    # We drop 'Label' to get features, and use 'Label' as our target
    X = df.drop(columns=['Label'])
    y = df['Label']
    feature_names = X.columns.tolist()

    # 3. Train/Test Split (80% training, 20% testing)
    print("Splitting data into 80% training and 20% testing")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Initialize and Train the Model
    print("Training the Random Forest Classifier")
    clf = RandomForestClassifier(
        n_estimators=100, 
        random_state=42, 
        oob_score=True,
        class_weight='balanced' 
    )
    clf.fit(X_train, y_train)

    # 5. Evaluate the Model (Prints metrics and shows charts)
    evaluate_allergen_model(clf, X_test, y_test)
    
    # 6. Plot Feature Importance
    plot_feature_importance(clf, feature_names)

    # 7. Save the trained model to disk
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    joblib.dump(clf, model_save_path)
    print(f"Model saved to: {model_save_path}")

if __name__ == '__main__':
    main()