import requests
import json

def getPurpose(medData):
    info = requests.get("https://api.fda.gov/drug/label.json?search=purpose:" + medData)
    JSONinfo = info.json()
    return JSONinfo

def main():
    i = input("Enter a medication to view its purpose: ")
    drug_info = getPurpose(i)
    purpose = drug_info['results'][0]['purpose'][0]
    print(purpose)
main()
