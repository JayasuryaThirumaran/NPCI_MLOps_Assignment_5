import pandas as pd
import numpy as np

# hello
def preprocess_data(input_path: str, output_path: str):
    """Loads data, cleans it, and saves the processed version."""
    df = pd.read_csv(input_path)

    # Handling missing values
    df.fillna(value={'education': 'unknown', 'job': 'unknown', 'marital': 'unknown'}, inplace=True)

    # Convert categorical variables into dummy/indicator variables
    df = pd.get_dummies(df, columns=['job', 'marital', 'education', 'housing', 'loan', 'default', 'month'])

    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data("data/bank_marketing.csv", "data/processed_data.csv")
