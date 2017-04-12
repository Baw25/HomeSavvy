import csv, requests, csv, json, sys, math
from urllib import urlencode
from collections import defaultdict

# Read the data from the Final_Scrape_Output
columns = defaultdict(list)
with open("mlax_links_output_test_3.csv","r") as f:
  reader = csv.DictReader(f)
  for row in reader: 
    for (k,v) in row.items():
      columns[k].append(v)

# # Open and write initial column
csvfile = open("get_images_from_images.csv", "w") 
field_names = ["address","image"]
writer = csv.DictWriter(csvfile, fieldnames=field_names)
writer.writeheader()

i = 0 
while i < len(columns['image']): 
  address = columns["source_Address"][i]
  main_img = columns["image"][i].split(" ")[0]
  writer.writerow({"address": address, "image": main_img})
  i += 1

print "Complete"



 
