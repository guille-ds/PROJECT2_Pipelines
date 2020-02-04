import pandas as pd
import requests
import os
from dotenv import load_dotenv
import time
load_dotenv()
myapikey = os.getenv("my_api_key")

df = pd.read_csv("input/df.csv")

def countryFilter(x):
    country = df.loc[df["Country of Operator"] == x]
    return country

def yearFilter(y):
    date = dfCountry.loc[dfCountry["Year"] == int(y)]
    return date

print('Name a country or --help')
x = input()
print('Your chosen country is ' + x)
print("------------------------------------------------------")
dfCountry = countryFilter(x)
print(dfCountry.head())
print("------------------------------------------------------")

print('Name a year')
y = input()
print('Your chosen year is ' + y)
print("------------------------------------------------------")
dfYear = yearFilter(y)
print(dfYear.iloc[:,0:1])
print("------------------------------------------------------")

print("Type the index which satellite's location you are interested in")
index = input()
satellite = df.loc[int(index)]["NORAD Number"]
print("How many seconds would you like to track it? (max = 10)")
sec = input()

def getCoord(sat):
    print('Ok, our Oompa Loompas are searching in the sky... ')
    lat = 40.4165000
    long = -3.7025600
    apikey = myapikey
    url = f"https://www.n2yo.com/rest/v1/satellite/positions/{sat}/{lat}/{long}/0/{sec}/&apiKey={apikey}"
    response = requests.get(url)
    data = response.json()
    return data

def show(peticion):
    print('Here comes the info...')
    time.sleep(2)
    tabla = pd.DataFrame(peticion["positions"])
    tabla.columns=["Sat_Latitude", "Sat_Longitude", "Sat_Height(km)", "Azimuth", "Elevation", "ra", "dec", "timestamp",]
    print("------------------------------------------------------")
    print(tabla.iloc[:,0:3])
    print("------------------------------------------------------")

def report(x):
    satData = df.loc[int(x)]
    print(satData)

position = getCoord(satellite)
show(position)
report(index)