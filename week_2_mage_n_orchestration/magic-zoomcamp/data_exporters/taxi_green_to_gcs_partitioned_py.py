import pyarrow as pa #used parition the data set
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/terraform-demo-411911-c14680156a1e.json"

bucket_name = 'mage-zoomcamp-demo-go'
project_id = 'terraform-demo-411911'

table_name="nyc_taxi_data_green"

root_path= f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    table = pa.Table.from_pandas(data) # reading our data to pyarrow table (defining our table)

    gcs = pa.fs.GcsFileSystem() #defines a file system object and automatically uses our GOOGLE_APPLICATION_CREDENTIALS environment variable (defining what our file system is)

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )