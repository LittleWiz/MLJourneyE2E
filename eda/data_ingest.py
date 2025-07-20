import os
import zipfile
import pandas as pd

class DataIngestor:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def _find_zip_file(self) -> str:
        """Find the first zip file in the data directory."""
        for file in os.listdir(self.data_dir):
            if file.endswith('.zip'):
                return os.path.join(self.data_dir, file)
        raise FileNotFoundError("No zip file found in the data directory.")

    def load_first_file_to_df(self) -> pd.DataFrame:
        """Extract the first file from the zip and load it into a DataFrame."""
        zip_path = self._find_zip_file()
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            if not file_list:
                raise ValueError("Zip file is empty.")
            first_file = file_list[0]
            with zip_ref.open(first_file) as f:
                if first_file.endswith('.csv'):
                    df = pd.read_csv(f)
                elif first_file.endswith('.xlsx'):
                    df = pd.read_excel(f)
                else:
                    raise ValueError(f"Unsupported file type: {first_file}")
        return df

# Example usage:
# ingestor = DataIngestor(data_dir='data')
# df = ingestor.load_first_file_to_df()
# print(df.head())