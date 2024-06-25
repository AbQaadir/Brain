# Kidney Disease Tumor or Normal Classification

## Project Overview
This project aims to develop a machine learning model to classify kidney images as either tumor or normal. Early and accurate classification is crucial for the effective treatment of kidney diseases.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/AbQaadir/Kidney-Disease-Classification.git
    cd kidney-tumor-classification
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Pipeline

### Individual Pipeline Steps
1. **Data Ingestion:**
    ```sh
    python src/KDC/pipeline/step_01_data_ingestion.py
    ```

2. **Prepare Base Model:**
    ```sh
    python src/KDC/pipeline/step_02_prepare_base_model.py
    ```

3. **Model Training:**
    ```sh
    python src/KDC/pipeline/step_03_model_training.py
    ```

4. **Model Evaluation:**
    ```sh
    python src/KDC/pipeline/step_04_model_evaluation.py
    ```

### Running the Complete Pipeline
To run the entire pipeline from data preprocessing to model evaluation, use the following command:

```sh
python main.py
```

### Experiment Management
We use Data Version Control (DVC) for experiment management. To reproduce experiments, run:

```sh
dvc repro
```

### Experiment Tracking
For detailed experiment tracking, See the DagsHub Repo (mlflow)
```sh
https://dagshub.com/AbQaadir/Kidney-Disease-Classification
```


### Additional Notes
* Ensure that you have all necessary data files in the correct directories before running the pipelines.

* If you encounter any issues, please refer to the `logs/` directory for detailed logs of each pipeline step.