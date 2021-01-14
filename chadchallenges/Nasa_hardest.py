#!/usr/bin/python3

import requests


def main():
    print("""
    Which Mars rover camera?
    FHAZ = Front Hazard Avoidance Camera
    RHAZ = Rear Hazard Avoidance Camera
    MAST = Mast Camera
    CHEMCAM = Chemistry and Camera Complex
    NAVCAM = Navigation Camera
    """)

    cameras= ["FHAZ","RHAZ","MAST","CHEMCAM","NAVCAM"]
    ans=""
    while ans not in cameras:
        ans = input(">").strip().upper()
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=nHeRJUgf4eVMyMdRRXZusR8zKXTrxUbBGwrwhanT").json()

    

if __name__ == "__main__":
    main()
