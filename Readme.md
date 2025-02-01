# CI/CD Pipeline for Bank Marketing Data using GitHub Actions 🚀

##  Project Overview  
This project implements a **CI/CD pipeline using GitHub Actions** to process **bank marketing data** and train a machine learning model.  
The pipeline includes:  
- **Data Preprocessing**: Cleaning & transforming raw data.  
- **Model Training**: Training a classification model.  
- **Automated Testing**: Using `pytest` for test cases.  
- **CI/CD Integration**: Automating workflow using GitHub Actions.  

---
 
## Assignment Tasks

**1. Understanding the Given Files**

You are provided with the following:
* Dataset: Required for preprocessing and model training.
* Preprocessing script (preprocessing.py): Cleans and prepares the data.
* Model training script (train_model.py): Trains and saves a machine learning model.
* Test scripts (tests/): Validates the preprocessing and model performance.

**2. Setting Up the CI/CD Pipeline**
* You need to create a GitHub Actions workflow to automate the ML pipeline when code is pushed to the main branch or a pull request is made.

**Steps to Include in ml_pipeline.yml**

* Trigger the Workflow: Run the pipeline on push and pull requests to the main branch.

* Set Up the Environment:
Use Ubuntu-latest as the runner.

* Install Python 3.8 and required dependencies (pandas, numpy,scikit-learn,, pytest).

* Run Preprocessing: Execute preprocessing.py to clean and transform the dataset.
* Train the Model: Run train_model.py to train and save the model.
* Run Unit Tests: Use pytest to verify correctness.

**3. Implementing the Workflow**
* You need to define the ml_pipeline.yml file in the .github/workflows/ directory, ensuring it includes:

* Checking out the repository
* Installing dependencies
* Running preprocessing and model training
*Executing tests



