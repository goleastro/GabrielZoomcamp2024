select 
    LocationID,
    Borough,
    Zone,
    replace(service_zone,'Boro','Green Zone') as service_zone
from {{ ref('taxi_zone_lookup') }}