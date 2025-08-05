import pandas as pd
import logging
from utils.logger import setup_logger

logger = setup_logger("E2EML", log_level=logging.INFO, console_level=logging.ERROR)

class DataEncoder:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a pandas DataFrame.
        """
        self.df = df

    def encode_categorical(self):
        """
        Identify categorical columns (object dtype) and apply one-hot encoding.
        Returns:
            pd.DataFrame: DataFrame with categorical variables encoded.
        """
        cat_cols = self.df.select_dtypes(include='object').columns.tolist()
        if not cat_cols:
            logger.info("🔎 No categorical columns found for encoding.")
            return self.df
        logger.info(f"🏷️ Identified categorical columns for encoding: {cat_cols}")
        self.df = pd.get_dummies(self.df, columns=cat_cols, drop_first=True)
        logger.info("🔄 Applied one-hot encoding to categorical columns.")
        return self.df
