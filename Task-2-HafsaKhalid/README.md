# Basic Data Classification Model

This repository contains a simple machine learning classification workflow developed as part of an assignment for Decode Labs. The project demonstrates core supervised learning steps including dataset inspection, train-test splitting, and model evaluation using Python.

## Key Features & Workflow

* **Data Ingestion:** Loaded and inspected the target dataset using Pandas to understand feature distributions.
* **Preprocessing:** Preparsed input features and performed train-test splitting to prevent data leakage.
* **Model Training:** Applied a supervised classification algorithm (Scikit-Learn) to learn patterns from the training set.
* **Evaluation:** Tested model performance on unseen test data using accuracy and standard classification evaluation metrics.

## Repository Contents

* `classification_model.py` — Core Python script executing the classification pipeline.
* `classification_model.ipynb` — Jupyter Notebook detailing step-by-step exploration and model testing.
* `requirements.txt` — Python package dependencies needed to run the project.
* `.gitignore` — Standard exclusion list for temporary cache and environment files.

## Setup and Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hafxakhalid9/Task-2-Hafsa-Khalid.git
   cd Task-2-Hafsa-Khalid
   ```
   **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
**Run the model:**
   ```bash
   python classification_model.py
```
## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn
- **IDE/Tools:** Visual Studio Code, Jupyter Notebook