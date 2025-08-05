import logging
import pandas as pd
from utils.logger import setup_logger

logger = setup_logger("E2EML", log_level=logging.INFO, console_level=logging.ERROR, stage_name="EDA-data inspection")

class DataInspector:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a pandas DataFrame.
        """
        self.df = df

    def data_shape(self):
        """Log and return the shape of the DataFrame."""
        shape = self.df.shape
        logger.info(f"📏 Data shape: {shape}")
        return shape

    def data_types(self):
        """Log and return the data types of each column."""
        dtypes = self.df.dtypes
        logger.info(f"🔠 Data types:\n{dtypes}")
        return dtypes

    def null_percentages(self):
        """Log and return the percentage of null values per column."""
        null_percent = self.df.isnull().mean() * 100
        logger.info(f"🕳️ Null percentages per column:\n{null_percent}")
        return null_percent

    def nulls_by_source_file(self):
        """
        Log and return null value percentage per column, grouped by 'source_file'.
        """
        if 'source_file' not in self.df.columns:
            logger.warning("⚠️ Column 'source_file' not found for per-file null analysis.")
            return None
        grouped = self.df.groupby('source_file')
        result = {}
        for name, group in grouped:
            nulls = (group.isnull().mean() * 100).round(2)
            logger.info(f"📂 Null percentages for source_file={name}:\n{nulls}")
            result[name] = nulls
        return result

    def inspect_all(self):
        """
        Run all inspection methods and return a dictionary with their results.
        Logs each step.
        Returns:
            dict: {
                "shape": tuple,
                "dtypes": pd.Series,
                "null_percentages": pd.Series,
                "nulls_by_source_file": dict or None
            }
        """
        logger.info("🔎 Running full data inspection...")
        results = {
            "shape": self.data_shape(),
            "dtypes": self.data_types(),
            "null_percentages": self.null_percentages(),
            "nulls_by_source_file": self.nulls_by_source_file()
        }
        logger.info("✅ Data inspection complete.")
        return results
# Example usage:
# from eda.data_ingester import DataIngestor
# ingestor = DataIngestor(data_dir='data')
# df = ingestor.load_data_file()
# inspector = DataInspector(df)