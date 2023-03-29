
import requests 
import csv
import json
import datetime
import xmltodict
import os
#For any earthquake that happens in the United States or off the coast, this code will generate real-time data.
#The magnitude, date, and time, coordinates, and location of the earthquake will all be gathered and given as data.
times = []
if os.path.exists("output.csv"):
  with open("output.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
      times.append(row[0])

api_call = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")

if api_call:
  call_results = json.loads(api_call.text)

  for i in call_results["features"]:
    orig_time = i["properties"]["time"]
    #Convert milliseconds to seconds
    orig_time_sec = orig_time / 1000
    #Convert Unix epoch time to datetime object
    datetime_timestamp = datetime.datetime.utcfromtimestamp(orig_time_sec)
    #Subtract 7 hours to adjust for time zone difference
    datetime_adj_timestamp = datetime_timestamp - datetime.timedelta(hours = 7)
    #Convert to human-interpretable string
    #String would say: “September 01, 2022 at 12:00:00 AM”
    time_str = datetime_adj_timestamp.strftime("%B %d, %Y at %I:%M:%S %p")
    #Get magnitude and coordinates
    magnitute = i["properties"]["mag"]
    longitude = i["geometry"]["coordinates"][0]
    latitude = i["geometry"]["coordinates"][1]
    api_call = requests.get("https://api.opencagedata.com/geocode/v1/xml?q="+str(latitude)+"+"+str(longitude)+"&key=55ef96be5a154fd89f762a23280441f5")
    if api_call:
      call_results = xmltodict.parse(api_call.text)
      #Get county and state
      try:
        if "county" in call_results["response"]["results"]["result"]["components"]:
          county = call_results["response"]["results"]["result"]["components"]["county"]
          state = call_results["response"]["results"]["result"]["components"]["state"]
          print("Magnitude", magnitute, "earthquake on", time_str,"and located at (",longitude,"," , latitude,")", "in", county, "," , state)
        #If location isn't within United States
        else:
          print("Magnitude", magnitute, "earthquake on", time_str,"and located at (",longitude,"," , latitude,")", "in Ocean")
          county = "N/A"
          state = "N/A"
        with open("output.csv", "a") as file:
          writer = csv.writer(file)
          #Write into CSV file
          if time_str not in times:
            writer.writerow([time_str, magnitute, longitude, latitude, county, state])
      except:
          print("Magnitude", magnitute, "earthquake on", time_str,"and located at (",longitude,"," , latitude,")", "in Ocean")
    else:
      print("There is an error during the call please try again.")
else:
  print("There is an error during the call please try again.")