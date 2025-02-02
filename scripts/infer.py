import mlflow
import mlflow.sklearn
import pandas as pd
import argparse

# Define function to load model and make predictions
def predict(input_data_path, model_name):
    # Load the best model from MLflow
    model = mlflow.sklearn.load_model(f"models:/{model_name}/latest")
    
    # Load input data
    data = pd.read_csv(input_data_path)
    
    # Make predictions
    predictions = model.predict(data)
    
    # Save predictions
    output_path = "predictions.csv"
    pd.DataFrame(predictions, columns=["Predicted_Class"]).to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")

# Parse command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run inference using the best MLflow model")
    parser.add_argument("--input_data", type=str, required=True, help="Path to the input CSV file")
    parser.add_argument("--model_name", type=str, default="RandomForest", help="Name of the trained model")
    args = parser.parse_args()
    
    predict(args.input_data, args.model_name)
