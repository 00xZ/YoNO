from selenium import webdriver
from random import randint
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
code = raw_input("Code: ")
sendto = raw_input("SPAM: ")
browser= webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
count = 0
while (count < 100):
	count = count + 1
	browser.get("http://onyolo.com/m/" + code + "?w=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")
	time.sleep(6)
	email_field = browser.find_element_by_id('text')
	email_field.send_keys(sendto)
	print("SENT: "+sendto+ ":" + str(count))
	submit = browser.find_element_by_id('send-button') #browser.find_element_by_xpath('//button[normalize-space()="Send anonymously"]')  ##('//*[@id="react-root"]/section/main/article/div[2]/div[1]/d>
	submit.click()
	time.sleep(3)
else:
	print("Done")
