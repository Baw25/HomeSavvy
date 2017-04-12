
import csv, requests, csv, json, sys, math
from urllib import urlencode
from collections import defaultdict

def __grab_address_coordinates(address):
  address = urlencode({'address':address})
  params = "?%s&key=AIzaSyAvJ0XUybspx758yk7Np9J26r-HaH6Punw" % address
  query_string = 'https://maps.googleapis.com/maps/api/geocode/json%s' % params
  try:
      request = requests.post(query_string)
      response = request.json()
      lat = response['results'][0]['geometry']['location']['lat']
      lng = response['results'][0]['geometry']['location']['lng']
  except URLError, e: 
      print 'There was an error fetching the coordinates from googlemaps'
  return [lat,lng]

# print __grab_address_coordinates("370 Stoneridge Ln San Francisco, CA")

# Read the data from the Final_Scrape_Output
columns = defaultdict(list)
with open("Fourth_Scrape_Output.csv","r") as f:
  reader = csv.DictReader(f)
  for row in reader: 
    for (k,v) in row.items():
      columns[k].append(v)


# # Open and write initial column
csvfile = open("output_lat_lng.csv", "w") 
field_names = ["address","lat","lng"]
writer = csv.DictWriter(csvfile, fieldnames=field_names)
writer.writeheader()

# print columns["City_State-Zip "][0]
# print columns["Address"][0]

i = 403
collection = []
while i < len(columns["Address"]) and i < len(columns["City_State-Zip "]):
  print i 
  address = columns["Address"][i].replace("\xe5_",'') + " " + columns["City_State-Zip "][i]
  coordinates = __grab_address_coordinates(address)
  writer.writerow({"address": address, "lat": coordinates[0], "lng": coordinates[1]})
  collection.append([address,coordinates])
  i += 1

# address = columns["Address"][403].replace("\xe5_",'') + " " + columns["City_State-Zip "][403]
# print address
# print __grab_address_coordinates(address)

print "Complete"

