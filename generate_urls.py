##Build urls

import re, string 

#read file 
with open("scrape_home_4_5_17.txt","r") as f:
  total = f.read().splitlines()

total_urls = []
base_url = "https://app.realtaasa.com/homes/property/CA/San-Francisco/"
regex = re.compile(r".+San Francisco, CA.+")
second_regex = re.compile(r"(.+)San\sFrancisco,\sCA,\s(\d+)")

#Iterate over read file 
for line in range(1,len(total),15):
    data = total[line]
    address = re.findall(second_regex,data)
    params = "-".join((address[0][0].lstrip() + " " + address[0][1].strip()).replace("#","").split(" "))
    url = (base_url + params).replace('"','')
    total_urls.append(url)
    

print total_urls

#Next step is to add the prop-ID from the a-tags for each listing at the end 
#of URL 




