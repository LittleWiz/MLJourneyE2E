# Project Development Process

1. **Environment Setup**  
   The project environment was initialized using Poetry. All dependencies were managed through the `pyproject.toml` file for reproducibility. The Poetry environment was also registered as a Jupyter kernel for interactive development.

2. **Data Acquisition**  
   Relevant data was downloaded and placed in the `data` folder, typically as zipped files for easy management.

3. **Logger Setup**  
   A reusable logger was implemented in `utils/logger.py` to provide consistent logging across all modules. Log files are stored in the `logs` directory. 

4. **Data Ingestion**  
   The `eda/data_ingestor.py` module was created to read zipped data files and load the first file into a pandas DataFrame, using the logger for process tracking.

5. **Data Inspection**  
   The `eda/data_inspector.py` module was developed to inspect the DataFrame, providing summary statistics and data quality checks.

6. **Data Analysis**  
   The `eda/data_analyser.py` module was implemented to:
   - Identify numeric and categorical columns.
   - Print unique values for categorical columns.
   - Plot histograms for numeric columns and bar charts for categorical columns.
   - Plot a correlation heatmap for numeric columns.
   - Plot grouped statistics (e.g., mean of numeric columns by category).

7. **Data Preprocessing**  
   The `eda/data_preprocessor.py` module was created to:
   - Convert month columns to datetime.
   - Extract numeric features from storey range columns.
   - Process the `remaining_lease` column into a numeric format.
   - Provide a `preprocess_all` method to run all preprocessing steps in sequence.

8. **Categorical Encoding**  
   The `eda/data_encoder.py` module was implemented to automatically identify categorical columns and apply one-hot encoding, with logging for each step.

9. **Database Integration**  
   SQLAlchemy was used to connect to a PostgreSQL database. Preprocessed features and targets are written to SQL tables for further use.

10. **Feature Store Setup**  
    PostgreSQL and pgAdmin were installed and configured. A dedicated database was created for Feast. The feature store was initialized using `feast init feature_store -t postgres`, and configuration was managed in `feature_store.yaml`.

11. **Documentation**  
    Step-by-step guides were created for Poetry (`POETRY_GUIDE.md`) and PostgreSQL/pgAdmin (`PGSQL_GUIDE.md`) setup, ensuring reproducibility and ease of onboarding for new contributors.

---
