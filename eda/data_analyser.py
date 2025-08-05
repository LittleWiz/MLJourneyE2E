import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.logger import setup_logger

logger = setup_logger("E2EML", log_level=logging.INFO, console_level=logging.ERROR, stage_name="EDA-data analysis")

class DataAnalyser:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a pandas DataFrame.
        """
        self.df = df

    def identify_columns(self):
        """
        Identify numeric and categorical columns.
        Returns:
            tuple: (list of numeric columns, list of categorical columns)
        """
        numeric_cols = self.df.select_dtypes(include='number').columns.tolist()
        category_cols = self.df.select_dtypes(include='object').columns.tolist()
        logger.info(f"🔢 Numeric columns: {numeric_cols}")
        logger.info(f"🏷️ Categorical columns: {category_cols}")
        return numeric_cols, category_cols

    def print_category_values(self):
        """
        Print unique values for each categorical column.
        """
        _, category_cols = self.identify_columns()
        for col in category_cols:
            unique_vals = self.df[col].unique()
            logger.info(f"🔍 Column '{col}' unique values: {unique_vals}")
            print(f"{col}: {unique_vals}")

    def plot_numeric(self):
        """
        Plot histograms for all numeric columns.
        """
        numeric_cols, _ = self.identify_columns()
        for col in numeric_cols:
            plt.figure(figsize=(6, 4))
            self.df[col].hist(bins=30)
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.tight_layout()
            plt.show()
            logger.info(f"📊 Plotted histogram for {col}")

    def plot_categorical(self):
        """
        Plot bar charts for all categorical columns.
        """
        _, category_cols = self.identify_columns()
        for col in category_cols:
            plt.figure(figsize=(8, 4))
            self.df[col].value_counts().plot(kind='bar')
            plt.title(f"Bar Chart of {col}")
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.tight_layout()
            plt.show()
            logger.info(f"📈 Plotted bar chart for {col}")

    def plot_covariance_heatmap(self):
        """
        Plot a heatmap of the correlation matrix for numeric columns.
        """
        numeric_cols, _ = self.identify_columns()
        corr = self.df[numeric_cols].corr()
        logger.info("🧮 Plotting covariance (correlation) heatmap for numeric columns.")
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Heatmap of Numeric Columns")
        plt.tight_layout()
        plt.show()
        logger.info("✅ Covariance heatmap plotted successfully.")

# Usage in notebook:
# analyser.plot_covariance_heatmap()