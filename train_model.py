from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the trained model
joblib.dump({
    "model": model,
    "names": iris.target_names.tolist()
}, "model.pkl")

print("Model trained and saved successfully!")
