
# print "Hello"

# Plan of action: 
# import requests and lxml 

#grab names for form fields for login 
#from realtassa 

# <input type="text" name="email" 
# id="email" placeholder="Email address" fieldrequired="1" 
# autofocus="" required="" data-schema-key="email" 
# class="input input--default d-block mbm">

# <input type="password" name="password" 
# id="password" placeholder="Password (min 6 chars)" 
# fieldrequired="1" required="" data-schema-key="password" 
# class="input input--default d-block mbm">

# grab the csrfmiddleware token

#Web scraper example 

### Version one 

# import requests
# import sys
# from lxml import html

# USERNAME = "bsteve5205@gmail.com"
# PASSWORD = "Rowing525"

# LOGIN_URL = "http://app.realtaasa.com/signin"
# URL = "https://app.realtaasa.com/sockjs/757/1cg0t2o5/websocket"
# SOCKET_URL = "wss://app.realtaasa.com/sockjs/349/y7z72tfh/websocket"
# REGULAR_URL = "https://app.realtaasa.com/homes/property/CA/San-Francisco/171-Ledyard-St-94124/60e09901d9e1376cfafd"

# def main():
#     session_requests = requests.session()

#     # Get login csrf token
#     result = session_requests.get(LOGIN_URL)
#     tree = html.fromstring(result.text)
#     # authenticity_token = session_requests.get(LOGIN_URL).cookies['csrftoken']

#     # Create payload
#     payload = {
#         "username": USERNAME, 
#         "password": PASSWORD, 
#     }

#     # Perform login
#     result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

#     headers = {
#       "Connection": "Upgrade",
#       "Pragma": "no-cache",
#       "Cache-Control" : "no-cache",
#       "Upgrade": "websocket",
#       "Origin": "https://app.realtaasa.com",
#       "Sec-WebSocket-Version": "13",
#       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
#       "Accept-Encoding": "gzip, deflate, sdch, br",
#       "Accept-Language": "en-US,en;q=0.8",
#       "Cookie": "ajs_anonymous_id=%22ffc402b4-b197-443f-ac18-fe46def85c1e%22; galaxy-sticky=!LuRNGRp7LaxEuEAmi-5nsx; ajs_user_id=%22FMCoPMNPq5noXNKzE%22; ajs_group_id=null; _ga=GA1.2.1382259158.1490751534; _gat=1",
#       "Host": "app.realtaasa.com",
#       "Sec-WebSocket-Key": "cMiXyMltgSNIxv8GkYmfYw==",
#       "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
#     }

#     # Scrape url
#     result = session_requests.get(URL, headers = headers)
#     # tree = html.fromstring(result.content)
#     # bucket_names = tree.xpath("//div[@class='nav-homes']/text()")
#     print result.json

#     second_result = dir(result)

#     print second_result

# if __name__ == '__main__':
#     main()

#Sample url 
# Accept-Encoding:gzip, deflate, sdch, br
# Accept-Language:en-US,en;q=0.8
# Cache-Control:no-cache
# Connection:Upgrade
# Cookie:ajs_anonymous_id=%22ffc402b4-b197-443f-ac18-fe46def85c1e%22; galaxy-sticky=!LuRNGRp7LaxEuEAmi-5nsx; ajs_user_id=%22FMCoPMNPq5noXNKzE%22; ajs_group_id=null; _ga=GA1.2.1382259158.1490751534; _gat=1
# Host:app.realtaasa.com
# Origin:https://app.realtaasa.com
# Pragma:no-cache
# Sec-WebSocket-Extensions:permessage-deflate; client_max_window_bits
# Sec-WebSocket-Key:cMiXyMltgSNIxv8GkYmfYw==
# Sec-WebSocket-Version:13
# Upgrade:websocket
# User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36


# Sample GET Request to the socket

# GET wss://app.realtaasa.com/sockjs/139/9vl65556/websocket HTTP/1.1


## Version 2 

import selenium.webdriver
driver = selenium.webdriver.PhantomJS()
driver.get('http://google.com')

driver.quit()
