import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

class IntelligentTestSelector:
    """
    Intelligent Test Case Selection Engine for Industrial CI/CD.
    Implements research-based ML models to optimize regression testing.
    """
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=500)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False

    def train_on_history(self, change_logs, failure_labels):
        """
        Trains the model to predict test failure based on code change patterns.
        """
        X = self.vectorizer.fit_transform(change_logs)
        self.model.fit(X, failure_labels)
        self.is_trained = True
        print("Model trained on industrial change history.")

    def predict_impact(self, current_changes):
        """
        Predicts which tests are likely to fail given the current code changes.
        """
        if not self.is_trained:
            return "Error: Model must be trained before prediction."
        
        X_current = self.vectorizer.transform(current_changes)
        predictions = self.model.predict(X_current)
        probabilities = self.model.predict_proba(X_current)[:, 1]
        
        return {
            "test_selected": bool(predictions[0]),
            "risk_score": f"{probabilities[0]:.2%}"
        }

if __name__ == "__main__":
    selector = IntelligentTestSelector()
    # Mock data representing historic code changes and test results
    history = ["fix: updated java parser", "feat: added new auth endpoint", "docs: update readme"]
    labels = [1, 1, 0] # 1 means test failure occurred
    
    selector.train_on_history(history, labels)
    
    new_change = ["fix: modified parsing logic in java core"]
    result = selector.predict_impact(new_change)
    print(f"Selection Result: {result}")
