# 🦉 Feast Feature Store Setup Guide

This guide will help you set up and use [Feast](https://feast.dev/) as a feature store for your ML projects.  
It is written for first-timers and assumes you have already set up PostgreSQL and pgAdmin (see `PGSQL_GUIDE.md`).

---

## 1️⃣ Install Feast

Activate your project environment and run:
```sh
pip install feast[postgres]
```
or, if using Poetry:
```sh
poetry add "feast[postgres]"
```

---

## 2️⃣ Initialize a Feast Feature Store

From your project directory, run:
```sh
feast init feature_store -t postgres
```
- When prompted, enter your PostgreSQL connection details (host, port, database, user, password).
- Make sure the database exists (see `PGSQL_GUIDE.md`).

---

## 3️⃣ Configure Your Feature Store

Edit `feature_store/feature_repo/feature_store.yaml` to match your database settings:
```yaml
project: MLJourneyE2E
provider: local
registry:
    registry_type: sql
    path: postgresql+psycopg://postgres:"your_password"@localhost:5432/feast_registry
    cache_ttl_seconds: 60000
online_store:
    type: postgres
    host: localhost
    port: 5432
    database: feast_online
    db_schema: public
    user: postgres
    password: "your_password"
offline_store:
    type: postgres
    host: localhost
    port: 5432
    database: feast_offline
    db_schema: public
    user: postgres
    password: "your_password"
entity_key_serialization_version: 3
```
**Note:** All passwords must be in quotes.

---

## 4️⃣ Define Entities and Feature Views

Edit `feature_store/feature_repo/definations.py` to define your entities and feature views.  
Example:
```python
from feast import Entity, FeatureView, Field, FileSource, ValueType
from feast.types import Float32, Int64, String
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import PostgreSQLSource
from datetime import timedelta
import os

house_features_path = os.path.abspath(os.path.join("..", "data", "house_features.parquet"))

house_features_source = FileSource(
    path=house_features_path,
    event_timestamp_column="event_timestamp",
)

house = Entity(
    name="house_id",
    join_keys=["house_id"],
    value_type=ValueType.INT64,
    description="Unique identifier for each house",
)

house_features_view = FeatureView(
    name="house_features",
    entities=[house],
    ttl=timedelta(days=365),
    schema=[
        Field(name="storey_min", dtype=Int64),
        Field(name="storey_max", dtype=Int64),
        # ... add all your feature fields ...
    ],
    online=True,
    source=house_features_source,
)
```

---

## 5️⃣ Apply Your Feature Store Definitions

From the `feature_repo` directory, run:
```sh
feast apply
```
This will register your entities and feature views with Feast.

---

## 6️⃣ Explore with Feast CLI

- List entities:
  ```sh
  feast entities list
  ```
- List feature views:
  ```sh
  feast feature-views list
  ```

---

## 7️⃣ Launch the Feast UI

Start the UI server:
```sh
feast ui --port 9000
```
Then open [http://localhost:9000](http://localhost:9000) in your browser.

---

## 8️⃣ Troubleshooting

- **FileNotFoundError:**  
  Make sure your Parquet/CSV files are in the correct path as referenced in your `definations.py`.
- **Password errors:**  
  Passwords in `feature_store.yaml` must be strings (in quotes).
- **Multiple timestamp columns:**  
  Only one column should be used as the event timestamp in your data sources.

---

## 9️⃣ References

- [Feast Documentation](https://docs.feast.dev/)
- [PGSQL_GUIDE.md](../PGSQL_GUIDE.md) for PostgreSQL setup

---

You are now ready to use Feast as a feature store for