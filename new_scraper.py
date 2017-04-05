#!/bin/python
# -*- coding: utf-8 -*-

# Droplet Name: ubuntu-512mb-sfo2-01
# IP Address: 138.68.252.152
# Username: root
# Password: fbe29a96430704766b5054c4d9
# New Password: Rowing525

# https://medium.com/@hoppy/how-to-test-or-scrape-javascript-rendered-websites-with-python-selenium-a-beginner-step-by-c137892216aa

from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display

class RealTassaSpider():

  def __init__(self):
    self.url_to_crawl = "https://app.realtaasa.com/homes"
    self.url_login = "http://app.realtaasa.com/signin"
    self.all_items = []

  # Open headless chromedriver
  def start_driver(self):
    print 'starting driver...'
    self.display = Display(visible=0, size=(800, 600))
    self.display.start()
    self.driver = webdriver.Chrome()
    sleep(4)

  # Close chromedriver
  def close_driver(self):
    print 'closing driver...'
    self.display.stop()
    self.driver.quit()
    print 'closed!'

  # Tell the browser to get a page
  def get_page(self, url):
    print 'getting page...'
    self.driver.get(url)
    sleep(randint(2,3))

# <button type="submit" class="input mbs button--primary">Continue</button>

  # Getting past login 
  def login(self):
    print 'getting pass the gate page...' 
    try:
      form = self.driver.find_element_by_xpath('//*[@id="signInForm"]')
      form.find_element_by_xpath('.//*[@id="email"]').send_keys('bsteve5205@gmail.com')
      form.find_element_by_xpath('.//*[@id="password"]').send_keys('Rowing525')
      form.find_element_by_xpath('.//*[@class="input.mbs.button--primary"]').click()
      sleep(randint(3,5))
    except Exception:
      pass

  def get_login_then_homes(self,url):
    print 'logging in...'
    self.driver.get(url_login)
    print 'getting pass the gate page...' 
    try:
      form = self.driver.find_element_by_xpath('//*[@id="signInForm"]')
      form.find_element_by_xpath('.//*[@id="email"]').send_keys('bsteve5205@gmail.com')
      form.find_element_by_xpath('.//*[@id="password"]').send_keys('Rowing525')
      form.find_element_by_xpath('.//*[@class="input.mbs.button--primary"]').click()
      sleep(randint(3,5))
    except Exception:
      pass
    home_button = self.driver.find_element_by_xpath('//*[@id="nav-homes"]')
    home_button.click()

    # <div class="desk--ten-twelfths push--desk--one-twelfth">

    url for mlax
    address 1
    address 2
    Neighborhood 1
    Building type 
    BedBath 
    Price 
    Coowners
    Monthly cost 
    Tax savings
    Down payment
    Description

    div#content --> main content area for all content

    div.grid__item one-whole > span.grid__item > a#more-photos

    div.one-whole > div.one-whole > div.prop-info > div.grid_item 

    h1.alpha --> address  
    div.beta --> address
    div.beta --> neighborhood 

    div.grid__item.desk--one-third.lap--one-third.one-whole.pln --> select all 
    div.delta.mbn.tc-cove.fw-500 --> select all 
    div.delta.mbs --> select all 

    div.grid__item.one-whole.pln --> select all 

  def grab_a_tags(self):
    print 'grabbing list of items...'
    for a in self.driver.find_elements_by_xpath('//*[@class="desk--ten-twelfths push--desk--one-twelfth"]//a'):
      data = self.process_elements(a)
      if data:
        self.all_items.append(data)
      else:
        pass

  def process_elements(self, a):
    url = ''
    address_1 = ''
    address_2 = ''
    prd_price = ''
    neighborhood = ''
    building_type = ''
    bedbath =''
    price = ''
    coowners = ''
    monthly_cost = ''
    tax_savings = ''
    down_payment = ''
    description = ''

    try:
      url = a.find_element_by_xpath('.//*[@id="more-photos"]').get_attribute('href')
      address_1 = a.find_element_by_xpath('.//*[@class="alpha mbn fw-500"]').text
      address_2 = a.find_element_by_xpath('.//*[@class="beta fw-300]').text
      prd_price = a.find_element_by_xpath('.//*[@class="price ng-scope ng-binding"]').text
    except Exception:
      pass

    if prd_image and prd_title and prd_price:
      single_item_info = {
        'image': prd_image.encode('UTF-8'),
        'title': prd_title.encode('UTF-8'),
        'price': prd_price.encode('UTF-8')
      }
      return single_item_info
    else:
      return False

  def parse(self):
    self.start_driver()

    self.get_page(self.url_login)
    self.login()
    self.grab_a_tags()

    self.close_driver()

    if self.all_items:
      return self.all_items
    else:
      return False


# Run spider
RealTassa = RealTassaSpider()
items_list = RealTassa.parse()

# Do something with the data touched
for item in items_list:
  print item
