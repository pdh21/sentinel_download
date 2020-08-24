# connect to the API
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

#read scihub credentials from scihub file
f = open("scihub", "r")
cred=f.read().splitlines()
f.close()

api = SentinelAPI(cred[0], cred[1], 'https://scihub.copernicus.eu/dhus')

# search by polygon, time, and SciHub query keywords
footprint = geojson_to_wkt(read_geojson('seaford.geojson'))
products = api.query(footprint,
                     date=('20171219', date(2020, 12, 29)),
                     platformname='Sentinel-2')

# convert to Pandas DataFrame
products_df = api.to_dataframe(products)

# sort and limit to first 5 sorted products
products_df_sorted = products_df.sort_values(['cloudcoverpercentage', 'ingestiondate'], ascending=[True, True])
#products_df_sorted = products_df_sorted.head(5)
products_df_sorted.to_csv('test_search.csv')

# download sorted and reduced products
#api.download_all(products_df_sorted.index)