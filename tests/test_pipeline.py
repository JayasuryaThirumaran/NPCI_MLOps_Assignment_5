import pandas as pd
import joblib
import pytest
from train_model import train_model

def test_preprocessing():
    """Tests whether the preprocessing script runs without errors."""
    try:
        df = pd.read_csv("data/processed_data.csv")
        assert not df.isnull().sum().any(), "Preprocessed data has missing values!"
        assert 'y' in df.columns, "Target variable missing!"
    except Exception as e:
        pytest.fail(f"Preprocessing test failed: {e}")

def test_model_training():
    """Tests if the model is successfully trained."""
    try:
        model = joblib.load("models/bank_model.pkl")
        assert model is not None, "Model failed to train!"
    except Exception as e:
        pytest.fail(f"Model training test failed: {e}")

if __name__ == "__main__":
    pytest.main()
