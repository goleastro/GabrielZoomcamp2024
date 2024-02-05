import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    #list of URLS
    urls =['https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',
    'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',
    'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz']

    # Initialize an empty list to store dataframes
    dfs = []

    for url in urls:
        response = requests.get(url)

        taxi_dtypes = {
            'VendorID': pd.Int64Dtype(),
            'passenger_count': pd.Int64Dtype(),
            'trip_distance': float,
            'RatecodeID':pd.Int64Dtype(),
            'store_and_fwd_flag':str,
            'PULocationID':pd.Int64Dtype(),
            'DOLocationID':pd.Int64Dtype(),
            'payment_type': pd.Int64Dtype(),
            'fare_amount': float,
            'extra':float,
            'mta_tax':float,
            'tip_amount':float,
            'tolls_amount':float,
            'improvement_surcharge':float,
            'total_amount':float,
            'congestion_surcharge':float
            }
        
        parse_dates = ['lpep_pickup_datetime','lpep_dropoff_datetime']

        # Read the content of the response into a Pandas DataFrame
        df = pd.read_csv(url,",",compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
        
        # Append the DataFrame to the list
        dfs.append(df)

    # Concatenate the dataframes along the rows
    final_df = pd.concat(dfs, ignore_index=True)

    # Print or manipulate the concatenated dataframe as needed
    return final_df


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
