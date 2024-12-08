import dlt
import datetime

# Sample data (replace with your actual data)
sample_data = [
    {"product_id": 1, "product_name": "Product A", "price": 10.99},
    {"product_id": 2, "product_name": "Product B", "price": 19.99},
    {"product_id": 3, "product_name": "Product C", "price": 29.99}
]

# Minimal transformation (optional)
def minimal_transformation(data):
    for row in data:
        # Add a new field with current UTC timestamp
        row["loaded_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        yield row

if __name__ == "__main__":
    # Initialize the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="sample_data_to_bq_pipeline",
        destination="bigquery",
        dataset_name="dlt"  # Your dataset name in BigQuery
    )

    # Directly pass the sample data to the transformation function
    transformed_data = minimal_transformation(sample_data)

    # Run the pipeline and load data into BigQuery
    load_info = pipeline.run(transformed_data)

    print(f"Data loaded to BigQuery: {load_info}")