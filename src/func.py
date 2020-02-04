import pandas as pd
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()
myapikey = os.getenv("my_api_key")

df = pd.read_csv("input/df.csv")

# Filter the dataset by country:
def countryFilter(x):
    country = df.loc[df["Country of Operator"] == x]
    return country

# Filter the Dataset by year:
def yearFilter(y, dfCountry):
    date = dfCountry.loc[dfCountry["Year"] == y[0]]
    return date

# Request coordinates to the API:
def getCoord(sat, sec):
    print('Ok, our Oompa Loompas are searching in the sky... ')
    lat = 40.4165000
    long = -3.7025600
    apikey = myapikey
    url = f"https://www.n2yo.com/rest/v1/satellite/positions/{sat}/{lat}/{long}/0/{sec}/&apiKey={apikey}"
    response = requests.get(url)
    data = response.json()
    return data

# Display the API response:
def show(a):
    print('Here comes the info...')
    time.sleep(1)
    tabla = pd.DataFrame(a["positions"])
    tabla.columns=["Sat_Latitude", "Sat_Longitude", "Sat_Height(km)", "Azimuth", "Elevation", "ra", "dec", "timestamp",]
    print("--------------------------------------------------")
    print(tabla.iloc[:,0:3])
    print("--------------------------------------------------")

# Display the Dataset info:
def report(x):
    satData = df.loc[int(x)]
    print(satData)

# Lead the process:
def play(country, year, sec):
    x = country
    print('Your chosen country is ' + x)
    print("--------------------------------------------------")
    dfCountry = countryFilter(x)
    print(dfCountry.head())
    print("--------------------------------------------------")

    y = year
    print('Your chosen year is ' + str(y[0]))
    print("--------------------------------------------------")
    dfYear = yearFilter(y, dfCountry)
    print(dfYear.iloc[:,0:1])
    print("--------------------------------------------------")

    z = sec
    print("Type the index which satellite's location you are interested in")
    index = input()
    satellite = df.loc[int(index)]["NORAD Number"]
    print("Tracking the next " + str(z[0]) + " positions")
    

    # Llamada a ejecución de otras funciones:
    position = getCoord(satellite, str(z[0]))
    show(position)
    report(index)