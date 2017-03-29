
import json 
import csv
import re
from decimal import Decimal 

#Reading from Json 
with open("total_results.json") as json_data:
  data = json.load(json_data)

#example json 
# test = {
#   u'url': u'151 Alice B. Toklas Pl #402\nSan Francisco, CA, 94109\n2 bd, 2 ba, $995,000\n2 co-owners\nMonthly cost\xb2 $1,866 + HOA\nYearly tax savings\xb2 $10,797',
#   u'name': u'151 Alice B. Toklas Pl #402\nSan Francisco, CA, 94109\n2 bd, 2 ba, $995,000\n2 co-owners\nMonthly cost\xb2 $1,866 + HOA\nYearly tax savings\xb2 $10,797'
# }
# print data["selection4"]

#regex examples
size_regex = re.compile(r'\d*\.?\d+')
price_regex = re.compile(r'\d+(?:,\d+)?')

#prepare csv
csvfile = open("total_results_3_28_17.csv", "w") 
field_names = ["address", "city_state_zip", "bedsize","bathsize", "price", "co_owners", "monthly_cost", "savings"]
writer = csv.DictWriter(csvfile, fieldnames=field_names)
writer.writeheader()

for json_listing in data["selection4"]:
  #Make this process a while loop 
  #split by newlines
  listing = json_listing['name'].encode('utf-8').strip().split("\n")
  #assign to new variables standing for the columns
  address = listing[0]
  city_state_zip = listing[1]
  bed_bath_price = listing[2].split(", ")
  bedsize = float(re.findall(size_regex, bed_bath_price[0])[0])
  bathsize = float(re.findall(size_regex, bed_bath_price[1])[0])
  price = int(bed_bath_price[2].strip("$").replace(',', ''))
  co_owners = int(re.findall(size_regex,listing[3])[0])
  monthly_cost = int(re.findall(price_regex,listing[4])[0].strip("$").replace(',', ''))
  savings = int(re.findall(price_regex,listing[5])[0].strip("$").replace(',', ''))
  # #Write to CSV
  writer.writerow({"address": address, "city_state_zip": city_state_zip, "bedsize": bedsize, "bathsize": bathsize, "price": price, "co_owners": co_owners, "monthly_cost": monthly_cost, "savings": savings})







