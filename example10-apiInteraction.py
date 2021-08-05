#!/usr/bin/python
"""RZFeeser | API example
   Interaction with requests and API."""

API = "http://api.open-notify.org/astros.json"

# python3 -m pip install requests
import requests

def main():

    # send an HTTP GET to our API
    resp = requests.get(API)

    # use the .json() method from the requests object "resp"
    spacedata = resp.json()

    # show our data
    print(spacedata)

    # show how many folks are in space
    print(f"There are currently {spacedata.get('number')} people in space.")

if __name__ == "__main__":
    main()
