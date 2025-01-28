import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Dummy data
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + np.random.rand(100)

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model trained and saved as model.pkl")
