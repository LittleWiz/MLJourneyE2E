import pandas as pd
import logging
from utils.logger import setup_logger

logger = setup_logger("E2EML", log_level=logging.INFO, console_level=logging.ERROR)

class DataPreprocessor:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a pandas DataFrame.
        """
        self.df = df

    def get_year_and_month_to_datetime(self, column='month'):
        """
        Convert the specified column to datetime format (YYYY-MM).
        Extracts 'year' and 'month' as separate columns and drops the original column.
        Args:
            column (str): The column name to convert. Default is 'month'.
        Returns:
            pd.DataFrame: DataFrame with 'year' and 'month' columns.
        """
        if column in self.df.columns:
            self.df[column] = pd.to_datetime(self.df[column], format='%Y-%m')
            self.df['year'] = self.df[column].dt.year
            self.df['month_num'] = self.df[column].dt.month
            self.df.drop(columns=[column], inplace=True)
            logger.info(f"📅 Extracted 'year' and 'month_num' from '{column}' and dropped the original column.")
        else:
            logger.warning(f"⚠️ Column '{column}' not found in DataFrame.")
        return self.df

    def extract_storey_range_features(self, column='storey_range'):
        """
        Extract numeric features from a storey range column.
        Adds 'storey_min', 'storey_max', and 'storey_mean' columns to the DataFrame.

        Args:
            column (str): The column name to process. Default is 'storey_range'.
        Returns:
            pd.DataFrame: DataFrame with new numeric columns.
        """
        if column in self.df.columns:
            try:
                self.df[['storey_min', 'storey_max']] = self.df[column].str.split(' TO ', expand=True).astype(int)
                self.df['storey_mean'] = self.df[['storey_min', 'storey_max']].mean(axis=1)
                self.df.drop(columns=[column], inplace=True)
                logger.info(f"🏢 Extracted 'storey_min', 'storey_max', and 'storey_mean' from '{column}'.")
            except Exception as e:
                logger.error(f"❌ Failed to extract storey range features: {e}")
        else:
            logger.warning(f"⚠️ Column '{column}' not found in DataFrame.")
        return self.df

    def process_remaining_lease(self, column='remaining_lease'):
        """
        Process the 'remaining_lease' column:
        - Replace NaN with -1000
        - Convert values like '61 years 04 months' to float years (e.g., 61.33)
        - Add a new column with '_years' suffix
        - Drop the original column

        Args:
            column (str): The column name to process. Default is 'remaining_lease'.
        Returns:
            pd.DataFrame: DataFrame with the processed column.
        """
        import numpy as np
        def parse_lease(val):
            if pd.isna(val):
                return -1000
            if isinstance(val, (int, float)):
                return float(val)
            if isinstance(val, str):
                years = 0
                months = 0
                if 'year' in val:
                    parts = val.split('year')
                    years = int(parts[0].strip())
                    if 'month' in parts[1]:
                        months_part = parts[1].split('month')[0]
                        months = int(''.join(filter(str.isdigit, months_part)))
                elif 'month' in val:
                    months = int(''.join(filter(str.isdigit, val)))
                return round(years + months / 12, 2)
            return -1000

        if column in self.df.columns:
            new_col = column + '_years'
            self.df[new_col] = self.df[column].apply(parse_lease)
            self.df.drop(columns=[column], inplace=True)
            logger.info(f"⏳ Processed '{column}' to '{new_col}' (years as float, NaN as -1000) and dropped original column.")
        else:
            logger.warning(f"⚠️ Column '{column}' not found in DataFrame.")
        return self.df

    def preprocess_all(self):
        """
        Run all preprocessing steps: convert month to datetime, extract storey range features,
        and process remaining lease. Returns the processed DataFrame.
        """
        logger.info("🚦 Starting full preprocessing pipeline...")
        self.get_year_and_month_to_datetime()
        self.extract_storey_range_features()
        self.process_remaining_lease()
        logger.info("✅ Preprocessing complete.")
        return self.df




