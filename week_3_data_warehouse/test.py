#i = 12
#month = '0'+str(i+1)+'asdsada'
#month = month[-2:]
#
#print(month)

init_url = []

for i in range(12): 
    month = '0'+str(i+1)
    month = month[-2:]
    init_url.append(f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{month}.parquet")

print(init_url)