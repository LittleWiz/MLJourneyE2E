import logging
import os
import zipfile
import pandas as pd
from utils.logger import setup_logger

logger = setup_logger("E2EML", log_level=logging.INFO, console_level=logging.ERROR)

class DataIngestor:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def _find_zip_file(self) -> str:
        """Find the first zip file in the data directory."""
        logger.info(f"🔍 Searching for zip files in {self.data_dir}")
        for file in os.listdir(self.data_dir):
            if file.endswith('.zip'):
                zip_path = os.path.join(self.data_dir, file)
                logger.info(f"📦 Found zip file: {zip_path}")
                return zip_path
        logger.error("❌ No zip file found in the data directory.")
        raise FileNotFoundError("No zip file found in the data directory.")

    def load_data_file(self) -> pd.DataFrame:
        """
        Extract all files from the zip and concatenate them into a single DataFrame.
        Adds a column 'source_file' indicating the filename for each row.
        Assumes all files have the same columns.
        
        Returns:
            pd.DataFrame: Concatenated DataFrame from all files in the zip.
        """
        zip_path = self._find_zip_file()
        logger.info(f"🗂️ Opening zip file: {zip_path}")
        dfs = []
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            if not file_list:
                logger.error("⚠️ Zip file is empty.")
                raise ValueError("Zip file is empty.")
            for file_name in file_list:
                logger.info(f"📄 Loading file from zip: {file_name}")
                with zip_ref.open(file_name) as f:
                    if file_name.endswith('.csv'):
                        df = pd.read_csv(f)
                    elif file_name.endswith('.xlsx'):
                        df = pd.read_excel(f)
                    else:
                        logger.error(f"🚫 Unsupported file type: {file_name}")
                        raise ValueError(f"Unsupported file type: {file_name}")
                    df['source_file'] = file_name
                    dfs.append(df)
        if dfs:
            big_df = pd.concat(dfs, ignore_index=True)
            logger.info(f"✅ Loaded concatenated DataFrame with shape: {big_df.shape}")
            return big_df
        else:
            logger.error("❌ No supported files found in the zip.")
            raise ValueError("No supported files found in the zip.")

# Example usage:
# ingestor = DataIngestor(data_dir='data')
# df = ingestor.load_data_file()
# print(df.head())