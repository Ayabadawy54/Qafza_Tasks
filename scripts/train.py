import mlflow
import mlflow.sklearn
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Enable MLflow autologging
mlflow.autolog()

# Load dataset
data = pd.read_csv("D:\AI\Projects\QafzaProjects\MLFlow\data\BankNote_Authentication.csv")
X = data.drop("class", axis=1)  # Features: variance, skewness, curtosis, entropy
y = data["class"]  # Target: 0 or 1

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models and hyperparameters
models = {
    "RandomForest": RandomForestClassifier,
    "LogisticRegression": LogisticRegression,
    "SVM": SVC
}

hyperparameters = {
    "RandomForest": {
        "n_estimators": [50, 100, 200],
        "max_depth": [5, 10, None]
    },
    "LogisticRegression": {
        "C": [0.1, 1.0, 10.0],
        "solver": ["liblinear"]
    },
    "SVM": {
        "C": [0.1, 1.0, 10.0],
        "kernel": ["linear", "rbf"]
    }
}

# Run experiments
for model_name, model_class in models.items():
    param_grid = hyperparameters[model_name]
    param_combinations = list(itertools.product(*param_grid.values()))

    for params in param_combinations:
        param_dict = dict(zip(param_grid.keys(), params))
        
        with mlflow.start_run():
            print(f"Training {model_name} with {param_dict}")
            
            # Initialize model
            model = model_class(**param_dict)
            model.fit(X_train, y_train)

            # Predict
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            # Log hyperparameters and metrics
            mlflow.log_params(param_dict)
            mlflow.log_metric("accuracy", accuracy)

            # Save model
            mlflow.sklearn.log_model(model, model_name)

print("Training completed. Check MLflow UI for details.")
