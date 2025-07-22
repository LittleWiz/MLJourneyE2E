import logging
import os
import zipfile
import pandas as pd
from utils.logger import setup_logger

logger = setup_logger("E2EML", log_level=logging.INFO, console_level=logging.ERROR, stage_name="EDA")

class DataIngestor:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def _find_zip_file(self) -> str:
        """Find the first zip file in the data directory."""
        logger.info(f"Searching for zip files in {self.data_dir}")
        for file in os.listdir(self.data_dir):
            if file.endswith('.zip'):
                zip_path = os.path.join(self.data_dir, file)
                logger.info(f"Found zip file: {zip_path}")
                return zip_path
        logger.error("No zip file found in the data directory.")
        raise FileNotFoundError("No zip file found in the data directory.")

    def load_first_file_to_df(self) -> pd.DataFrame:
        """Extract the first file from the zip and load it into a DataFrame."""
        
        zip_path = self._find_zip_file()
        logger.info(f"Opening zip file: {zip_path}")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            if not file_list:
                logger.error("Zip file is empty.")
                raise ValueError("Zip file is empty.")
            first_file = file_list[0]
            logger.info(f"Loading file from zip: {first_file}")
            with zip_ref.open(first_file) as f:
                if first_file.endswith('.csv'):
                    df = pd.read_csv(f)
                elif first_file.endswith('.xlsx'):
                    df = pd.read_excel(f)
                else:
                    logger.error(f"Unsupported file type: {first_file}")
                    raise ValueError(f"Unsupported file type: {first_file}")
        logger.info(f"Loaded DataFrame with shape: {df.shape}")
        return df

# Example usage:
# ingestor = DataIngestor(data_dir='data')
# df = ingestor.load_first_file_to_df()
# print(df.head())