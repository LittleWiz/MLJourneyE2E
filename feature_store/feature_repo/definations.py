from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource, ValueType
from feast.types import Float32, Int64, String
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import PostgreSQLSource
import os

# Define the path to your feature data (for FileSource)
house_features_path = os.path.abspath(os.path.join("..", "data", "house_features.parquet"))
house_target_path = os.path.abspath(os.path.join("..", "data", "house_target.parquet"))

# FileSource for offline (batch) features
house_features_source = FileSource(
    path=house_features_path,
    event_timestamp_column="event_timestamp",
)

house_target_source = FileSource(
    path=house_target_path,
    event_timestamp_column="event_timestamp",
)

# PostgreSQLSource for direct DB integration
pg_source = PostgreSQLSource(
    name="house_features_sql",
    query="SELECT * FROM house_features_sql",
    timestamp_field="event_timestamp",
)

# Define the entity
house = Entity(
    name="house_id",
    join_keys=["house_id"],
    value_type=ValueType.INT64,
    description="Unique identifier for each house",
)

# FeatureView using FileSource (for batch/offline)
house_features_view = FeatureView(
    name="house_features",
    entities=[house],
    ttl=timedelta(days=365),
    schema=[
        Field(name="storey_min", dtype=Int64),
        Field(name="storey_max", dtype=Int64),
        Field(name="storey_mean", dtype=Float32),
        Field(name="floor_area_sqm", dtype=Float32),
        Field(name="lease_commence_date", dtype=Int64),
        Field(name="remaining_lease_years", dtype=Float32),
        Field(name="month", dtype=String),
        Field(name="town_freq", dtype=Float32),
        Field(name="flat_type_freq", dtype=Float32),
        Field(name="block_freq", dtype=Float32),
        Field(name="street_name_freq", dtype=Float32),
        Field(name="flat_model_freq", dtype=Float32),
    ],
    online=True,
    source=house_features_source,
    tags={"team": "ml", "project": "house_price"},
)

# FeatureView using PostgreSQLSource (for direct DB integration)
house_features_sql_view = FeatureView(
    name="house_features_sql",
    entities=[house],
    ttl=timedelta(days=365),
    schema=[
        Field(name="storey_min", dtype=Int64),
        Field(name="storey_max", dtype=Int64),
        Field(name="storey_mean", dtype=Float32),
        Field(name="floor_area_sqm", dtype=Float32),
        Field(name="lease_commence_date", dtype=Int64),
        Field(name="remaining_lease_years", dtype=Float32),
        Field(name="month", dtype=String),
        Field(name="town_freq", dtype=Float32),
        Field(name="flat_type_freq", dtype=Float32),
        Field(name="block_freq", dtype=Float32),
        Field(name="street_name_freq", dtype=Float32),
        Field(name="flat_model_freq", dtype=Float32),
    ],
    online=True,
    source=pg_source,
    tags={"team": "ml", "project": "house_price"},
)

# Optionally, define a FeatureView for targets if needed
house_target_view = FeatureView(
    name="house_target",
    entities=[house],
    ttl=timedelta(days=365),
    schema=[
        Field(name="resale_price", dtype=Float32),
    ],
    online=False,
    source=house_target_source,
    tags={"team": "ml", "project": "house_price"},
)