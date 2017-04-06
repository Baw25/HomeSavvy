import csv, requests, csv, json, sys, math
from urllib import urlencode
from collections import defaultdict


# Read the data from the Final_Scrape_Output
columns = defaultdict(list)
with open("final_coord.csv","r") as f:
  reader = csv.DictReader(f)
  row0 = reader.next()
  
  # for row in reader: 
  #   for (k,v) in row.items():
  #     columns[k].append(v)


# # Open and write initial column
# csvfile = open("Final_Scrape_Output.csv", "w") 
# field_names = ["address","lat","lng"]
# writer = csv.DictWriter(csvfile, fieldnames=field_names)
# writer.writeheader()

# i = 132
# collection = []
# while i < len(columns["Address"]) and i < len(columns["City-State-Zip"]):
#   print i 
#   address = columns["Address"][i].replace("\xe5_",'') + " " + columns["City-State-Zip"][i]
#   coordinates = __grab_address_coordinates(address)
#   writer.writerow({"address": address, "lat": coordinates[0], "lng": coordinates[1]})
#   collection.append([address,coordinates])
#   i += 1

# address = columns["Address"][131].replace("\xe5_",'') + " " + columns["City-State-Zip"][131]
# print address
# print __grab_address_coordinates(address)
print "Complete"

