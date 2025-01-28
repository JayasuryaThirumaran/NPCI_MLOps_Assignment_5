import pickle
import numpy as np
from sklearn.metrics import mean_squared_error

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Dummy test data
X_test = np.random.rand(20, 1)
y_test = 3 * X_test.squeeze() + np.random.rand(20)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save evaluation metrics
with open("metrics.txt", "w") as f:
    f.write(f"Mean Squared Error: {mse}")
