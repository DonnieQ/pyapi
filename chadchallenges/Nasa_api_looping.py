#!/usr/bin/python3

import requests


def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=nHeRJUgf4eVMyMdRRXZusR8zKXTrxUbBGwrwhanT").json()

    for rov in roverresp["photos"]:
       print("Rover: " + rov["rover"]["name"]+"\n" + "DATE: "+ rov["earth_date"]+ "\n" + rov["img_src"])

if __name__ == "__main__":
    main()
