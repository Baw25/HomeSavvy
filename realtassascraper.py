
    # session_requests = requests.session()
    # # Get login csrf token
    # result = session_requests.get(LOGIN_URL)
    # tree = html.fromstring(result.text)
    # authenticity_token = session_requests.get(LOGIN_URL).cookies['csrftoken']

    # headers = {
    #   "Connection": "Upgrade",
    #   "Pragma": "no-cache",
    #   "Cache-Control" : "no-cache",
    #   "Upgrade": "websocket",
    #   "Origin": "https://app.realtaasa.com",
    #   "Sec-WebSocket-Version": "13",
    #   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    #   "Accept-Encoding": "gzip, deflate, sdch, br",
    #   "Accept-Language": "en-US,en;q=0.8",
    #   "Cookie": "ajs_anonymous_id=%22ffc402b4-b197-443f-ac18-fe46def85c1e%22; galaxy-sticky=!LuRNGRp7LaxEuEAmi-5nsx; ajs_user_id=%22FMCoPMNPq5noXNKzE%22; ajs_group_id=null; _ga=GA1.2.1382259158.1490751534; _gat=1",
    #   "Host": "app.realtaasa.com",
    #   "Sec-WebSocket-Key": "cMiXyMltgSNIxv8GkYmfYw==",
    #   "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    # }

    # Scrape url
    # result = session_requests.get(URL, headers = headers)
    # tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='nav-homes']/text()")

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

# def login():
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

    # headers = {
    #   "Connection": "Upgrade",
    #   "Pragma": "no-cache",
    #   "Cache-Control" : "no-cache",
    #   "Upgrade": "websocket",
    #   "Origin": "https://app.realtaasa.com",
    #   "Sec-WebSocket-Version": "13",
    #   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    #   "Accept-Encoding": "gzip, deflate, sdch, br",
    #   "Accept-Language": "en-US,en;q=0.8",
    #   "Cookie": "ajs_anonymous_id=%22ffc402b4-b197-443f-ac18-fe46def85c1e%22; galaxy-sticky=!LuRNGRp7LaxEuEAmi-5nsx; ajs_user_id=%22FMCoPMNPq5noXNKzE%22; ajs_group_id=null; _ga=GA1.2.1382259158.1490751534; _gat=1",
    #   "Host": "app.realtaasa.com",
    #   "Sec-WebSocket-Key": "cMiXyMltgSNIxv8GkYmfYw==",
    #   "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    # }

    # Scrape url
    # result = session_requests.get(URL, headers = headers)
    # tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='nav-homes']/text()")
    # print result.json

    # second_result = dir(result)

    # print second_result

# if __name__ == '__main__':
#     login()
# import requests
# import sys
# from lxml import html

import re, urlparse

from selenium import webdriver 
from bs4 import BeautifulSoup
from time import sleep 
import requests
import sys
from lxml import html

# link = "https://app.realtaasa.com/homes"

class RealTassaScraper(object): 
  def __init__(self):
    self.driver = webdriver.PhantomJS()
    self.driver.set_window_size(1120,50)

  def navigate_to_homes(self):
    USERNAME = "bsteve5205@gmail.com"
    PASSWORD = "Rowing525"
    LOGIN_URL = "http://app.realtaasa.com/signin"

    self.driver.get(LOGIN_URL)

    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
    }
    self.driver.find_element_by_id('email').sendKeys(payload["username"])
    self.driver.find_element_by_id('password').sendKeys(payload["password"])
    self.driver.find_element_by_class_name('input mbs button--primary').click()
    print "button click"
    sleep(5)
    print "Logged In"

  def scrape_listings(self): 
    #Logging in 
    USERNAME = "bsteve5205@gmail.com"
    PASSWORD = "Rowing525"
    LOGIN_URL = "http://app.realtaasa.com/signin"

    self.driver.get(LOGIN_URL)

    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
    }

    self.driver.find_element_by_id('email').send_keys(payload["username"])
    self.driver.find_element_by_id('password').send_keys(payload["password"])
    self.driver.find_element_by_tag_name('button').click()
    print "button click"
    sleep(5)
    print "Logged In"
    # print self.driver.page_source
    self.driver.find_element_by_id('nav-homes').click()
    print "Clicked homes"
    # link = "https://app.realtaasa.com/homes"
    # self.driver.get(link)
    sleep(5)
    print "On homes page"
    #Navigating to the homes page
    # self.driver.find_element_by_xpath("//div[@id='nav-homes']").click()
    # link = "https://app.realtaasa.com/homes"
    # self.driver.get(link)
    listings = []
    # pageno = 1
    page_count = 0 
    listing_count = 0

    while True: 
      s = BeautifulSoup(self.driver.page_source, "lxml")
      # soup = BeautifulSoup(html_doc, 'html.parser')
      r = re.compile(r"grid__item text--left desk--three-tenths lap--four-tenths eleven-twelfths prop-tile")
      aID = re.compile(r"prop--.{1,20}")
      # print s.findAll(id=link)
      print s.findAll("a")
      for a in s.findAll("a", class_=r):        
        # if a['id'] == aID:
        # print "Hey"
        print "a %s" % a 
        listing = {}
        #click the link 
        # link = driver.find_element_by_css_selector('[href^=#0]')
        a.click()
        mlaxlink = s.findAll('a', href=link)
        listing["link"] = mlaxlink
        listing["content"] = s.get_text()
        listings.append(listing)
        listing_count += 1
        print "listings: %s" % listing_count

      break 
      # next_page_elem = self.driver.find_element_by_id('loadMore')
      # # next_page_link = s.find('a', text='%d' % pageno)
      # if next_page_elem: 
      #   next_page_elem.click()
      #   sleep(2)
      #   page_count += 1
      #   print "pages: %s" % page_count
      # else:
      #   print "Finished"
      #   break 

    return listings

  def scrape(self):
    listings = self.scrape_listings()
    print listings
    for listing in listings: 
      print listing 

    self.driver.quit()

if __name__ == "__main__":
  scraper = RealTassaScraper()
  scraper.scrape()






