# dlt-simple
**README.md**

### **Project: Data Ingestion Pipeline with DLT**

**Overview:**

This project demonstrates a simple data ingestion pipeline using the Data Lineage Toolkit (DLT) to load sample data into a BigQuery dataset. The pipeline fetches data from a specified source (in this case, an in-memory list) and transforms it before loading it into the target BigQuery dataset.

**Prerequisites:**

- **Google Cloud Platform (GCP) Account:** Ensure you have a GCP account and a project set up.
- **DLT:** Install the DLT library using pip:
  ```bash
  pip install dlt
  ```
- **Google Cloud SDK (gcloud):** Install and initialize gcloud to authenticate with your GCP project.

**Configuration:**

- **BigQuery Dataset:** Replace `"dlt"` in the `dataset_name` parameter with your desired dataset name.
- **Sample Data:** Modify the `sample_data` list to include your specific data.

**Running the Pipeline:**

1. **Navigate to the Project Directory**
2. **Run the Pipeline:**
   ```bash
   python dlt_etl.py
   ```

**DLT Pipeline Configuration:**

The DLT pipeline is configured to:

- **Fetch Data:** Reads data from the `sample_data` list.
- **Transform Data:** Applies a minimal transformation to add a `loaded_at` timestamp to each row.
- **Load Data:** Loads the transformed data into the specified BigQuery dataset.

**Additional Considerations:**

- **Error Handling:** Consider implementing error handling mechanisms to gracefully handle exceptions and log errors.
- **Data Validation:** Implement data validation checks to ensure data quality and consistency.
- **Pipeline Optimization:** Explore DLT's optimization techniques to improve pipeline performance and efficiency.
- **Security:** Ensure proper security measures are in place to protect sensitive data, such as using service accounts with appropriate permissions.

**For more information on DLT, refer to the official documentation:** [invalid URL removed]

**Feel free to customize and extend this pipeline to fit your specific data ingestion needs.**
