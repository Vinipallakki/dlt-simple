import dlt
from google.cloud import storage
import csv
import io
from datetime import datetime

def gcs_data_source(bucket_name: str, file_name: str):
    # Initialize GCS client
    client = storage.Client()

    # Access bucket and file
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Read file content into memory
    data = blob.download_as_text()

    # Parse CSV data
    csv_reader = csv.DictReader(io.StringIO(data))
    for row in csv_reader:
        yield row

def minimal_transformation(data):
    for row in data:
        # Example transformation: Add a new field with current UTC time
        row["loaded_at"] = datetime.utcnow().isoformat()  # Use Python's datetime module
        yield row

if __name__ == "__main__":
    # Initialize the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="gcs_to_bq_pipeline",
        destination="bigquery",
        dataset_name="dlt_gcs"  # Your dataset name in BigQuery
    )

    # Define GCS bucket and file details
    bucket_name = "banded-edge-437103-i9"  # Your GCS bucket name
    file_name = "sales_data.csv"  # File name in GCS

    # Fetch data from GCS without using decorators
    sales_data = gcs_data_source(bucket_name, file_name)

    # Apply minimal transformations
    transformed_sales_data = minimal_transformation(sales_data)

    # Run the pipeline and load data into BigQuery
    load_info = pipeline.run(transformed_sales_data)

    print(f"Data loaded to BigQuery: {load_info}")
