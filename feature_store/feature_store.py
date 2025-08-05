from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage
import pandas as pd
from datetime import datetime, timedelta


class FeastFeatureStore:
    def __init__(self, path):
        """
        Initialize the Feast Feature Store.

        Args:
            path (str): Path to the feature_repo directory containing feature_store.yaml.
        """
        self.store = FeatureStore(repo_path=path)
        self.retrievalJob = None

    def get_entity_dataframe(self, path) -> pd.DataFrame:
        """
        Read a Parquet file as an entity DataFrame.

        Args:
            path (str): Path to the Parquet file.

        Returns:
            pd.DataFrame: Loaded entity DataFrame.
        """
        entity_df = pd.read_parquet(path=path)
        return entity_df

    def get_historical_features(self, entity_df: pd.DataFrame, features) -> pd.DataFrame:
        """
        Fetch historical features for a given entity DataFrame.

        Args:
            entity_df (pd.DataFrame): DataFrame containing entity columns and event_timestamp.
            features (List[str]): List of feature references (e.g., ["house_features:storey_min"]).

        Returns:
            pd.DataFrame: DataFrame with historical features.
        """
        self.retrievalJob = self.store.get_historical_features(
            entity_df=entity_df,
            features=features
        )
        return self.retrievalJob.to_df()
    
    def save_dataset(self, file_name, path):
        """
        Save the last retrieved historical features as a SavedDataset.

        Args:
            file_name (str): Name for the saved dataset.
            path (str): Path where the dataset will be stored.
        """
        self.store.create_saved_dataset(
            from_=self.retrievalJob,
            name=file_name,
            storage=SavedDatasetFileStorage(path)
        )
        print(str.format("File {0} saved successfully", file_name))

    def materialize(self, end_date, start_date=None, increment=False):
        """
        Materialize features from offline to online store.

        Args:
            end_date (datetime): End date for materialization.
            start_date (datetime, optional): Start date for materialization (required if increment=False).
            increment (bool): If True, perform incremental materialization up to end_date.
        """
        if not increment:
            # Load features to online store between two dates
            self.store.materialize(
                end_date=end_date,
                start_date=start_date)
        else:
            self.store.materialize_incremental(end_date=end_date)

    def get_online_features(self, entity_rows, features) -> pd.DataFrame:
        """
        Fetch online features for given entity rows.

        Args:
            entity_rows (List[Dict]): List of dicts with entity keys and values.
            features (List[str]): List of feature references (e.g., ["house_features:storey_min"]).

        Returns:
            pd.DataFrame: DataFrame with online feature values.
        """
        retrievalJob = self.store.get_online_features(
            entity_rows=entity_rows,
            features=features
        )
        return retrievalJob.to_df()