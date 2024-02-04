import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    print("Trips with 0 passengers:", data['passenger_count'].isin([0]).sum(), "; Trips with 0 distance:", data['trip_distance'].isin([0]).sum())
    #print("Trips with 0 distance:", data['trip_distance'].isin([0]).sum())

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Change column names by adding underscore before every uppercase letter (except the leading uppercase letter and consecutive uppercase letters)
    data.columns = [re.sub(r'(?<!^)(?<![A-Z])([A-Z])', r'_\1', col).lower() for col in data.columns]


    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    #check the output from above and if there are 0 rows where the passenger count is 0 then the test passes, else it fails
    assert output['passenger_count'].isin([0]).sum() == 0 , 'There are rides with 0 passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with 0 trip distance'
    assert 'vendor_id' in output.columns, "'vendor_id' is not one of the columns in the final dataframe"