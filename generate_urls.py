##Build urls

import re, string, csv

#read file 
with open("scrape_home_4_5_17.txt","r") as f:
  total = f.read().splitlines()

total_urls = []
base_url = "https://app.realtaasa.com/homes/property/CA/San-Francisco/"
regex = re.compile(r".+San Francisco, CA.+")
second_regex = re.compile(r"(.+)San\sFrancisco,\sCA,\s(\d+)")

#Iterate over read file containing urls part one 
for line in range(1,len(total),15):
    data = total[line]
    address = re.findall(second_regex,data)
    params = "-".join((address[0][0].lstrip() + " " + address[0][1].strip()).replace("#","").split(" "))
    url = (base_url + params).replace('"','')
    total_urls.append(url)
  

#Next step is to add the prop-ID from the a-tags for each listing at the end 
#of URL 
with open("url-Ids.csv","r") as g:
  all_Ids = g.read().splitlines()

# Open and write initial urls
csvfile = open("total_urls_combined.csv", "w") 
field_names = ["urls"]
writer = csv.DictWriter(csvfile, fieldnames=field_names)
writer.writeheader()

#Write to new CSV for complete url

i = 0
j = 1
regex_id = re.compile(r'prop--(\w+)')
while j < len(all_Ids): 
  complete_id = re.findall(regex_id,all_Ids[j])
  complete_url = total_urls[i] + "/" + complete_id[0]
  # print complete_url
  writer.writerow({"urls": complete_url})
  i += 1
  j += 1
print "Complete"

#Write to a new line 




