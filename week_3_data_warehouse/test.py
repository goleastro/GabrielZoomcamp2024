#i = 12
#month = '0'+str(i+1)+'asdsada'
#month = month[-2:]
#
#print(month)

init_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data'
year = '2022'
service = 'green'

for i in range(12):
    
    # sets the month part of the file_name string
    month = '0'+str(i+1)
    month = month[-2:]

    # csv file_name
    file_name = f"{service}_tripdata_{year}-{month}.parquet"

    # download it using requests via a pandas df
    request_url = f"{init_url}/{file_name}"
    print(request_url)

   #https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet
   #https://d37ci6vzurychx.cloudfront.net/trip-data/green/green_tripdata_2022-01.parquet