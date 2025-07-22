# Project Development Process

1. **Environment Setup**  
   The project environment was initialized using Poetry. All dependencies were managed through the `pyproject.toml` file for reproducibility.

2. **Data Acquisition**  
   Relevant data was downloaded and placed in the `data` folder, typically as zipped files for easy management.

3. **Logger Setup**  
   A reusable logger was implemented in `utils/logger.py` to provide consistent logging across all modules. Log files are stored in the `logs` directory.

4. **Data Ingestion**  
   The `eda/data_ingest.py` module was created to read zipped data files and load the first file into a pandas DataFrame, using the logger for process tracking.