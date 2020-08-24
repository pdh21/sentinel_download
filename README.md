# sentinel_download

Downloading Sentinel data using the [Sentinelsat](https://sentinelsat.readthedocs.io/en/stable/index.html) Python package.

You can either use as module in python script or use commnand line interface.

To build docker image:
`
docker build -t pdh21/sentinel_download .
`
Example using docker image:
`
docker run -it --rm -v "$PWD":/usr/src/app -w /usr/src/app pdh21/sentinel_download:latest sentinelsat --user <user>
 --password <password> -g seaford.geojson -s 20200801 -e 20200817 --sentinel 2 --cloud 40 
 -d`
 
 * `--user`: user name for Copernicus Open Access Hub
 * `--password`: password for Copernicus Open Access Hub
 * `-g`: for using a geojson file to search for
 * `-s`: start date
 * `-e`: end date
 * `sentinel`: what sentinel? e.g. 1,2,3 etc
 * `--cloud`: maximum cloud cover percentage 
 * `-d`: download files that match search
 
 For other options see the [Sentinelsat](https://sentinelsat.readthedocs.io/en/stable/index.html) documentation.
 
 To use docker with custom scripts:
 `
docker run -it --rm -v "$PWD":/usr/src/app -w /usr/src/app pdh21/sentinel_download:latest python search_select_download.py`

I suggest you put your username and password for scihub in a file called `scihub` and read in where necessary.