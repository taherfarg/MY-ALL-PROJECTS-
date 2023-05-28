from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# set the path for the Brave browser executable
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# create a Brave browser instance using the webdriver
options = webdriver.ChromeOptions()
options.binary_location = brave_path
driver = webdriver.Chrome(options=options)

# open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# wait for the user to scan the QR code
input("Please scan the QR code and press enter to continue")

# find the search box and type the phone number
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys("")
search_box.send_keys(Keys.ENTER)

# wait for the chat to load
time.sleep(5)

# find the input box and type the message
input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
input_box.send_keys("Hello, World!")
input_box.send_keys(Keys.ENTER)

# close the browser
driver.quit()


