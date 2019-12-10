from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from time import sleep
import sys

browser = webdriver.Firefox()
delay = 60
try:
    print("trying to connect...")
    browser.get("https://gmail.com")
    print('connected')
except selenium.common.exceptions.WebDriverException:
    print("Please check You Internet Connection")

# try:
elemEmail = browser.find_element_by_id('identifierId')
elemEmail.send_keys('liba1925@gmail.com')
emailNext = browser.find_element_by_id('identifierNext')
nextEmailElem = WebDriverWait(browser,delay).until(EC.presence_of_element_located((By.ID,'identifierNext')))
WebDriverWait(browser,delay).until(EC.element_to_be_clickable((By.ID,'identifierNext')))
emailNext.click()
myElem = WebDriverWait(browser,delay).until(EC.presence_of_element_located((By.NAME,'password')))
WebDriverWait(browser,delay).until(EC.visibility_of(myElem))
pwdElem = browser.find_element_by_name('password')
# browser.execute_script("arguments[0].click();", pwdElem)
# pwdElem.click()
pwdElem.send_keys("8410955075")
# sleep(3)
# pwdElem.send_keys(Keys.ENTER)
nextElem = browser.find_element_by_id('passwordNext')
WebDriverWait(browser,delay).until(EC.visibility_of(nextElem))
WebDriverWait(browser,delay).until(EC.element_to_be_clickable((By.ID,'passwordNext')))
nextElem.click()

# WebDriverWait(browser,60).until(EC.presence_of_element_located((By.CLASS_NAME,'T-I J-J5-Ji T-I-KE L3')))
composeElem = browser.find_element_by_class_name('z0')
WebDriverWait(browser,delay).until(EC.visibility_of(composeElem))
WebDriverWait(browser,delay).until(EC.element_to_be_clickable((By.CLASS_NAME,'z0')))
composeElem.click()
# except Exception as err:
#     print("Something Went Wrong!!",str(err))
recElem = WebDriverWait(browser,delay).until(EC.presence_of_element_located((By.NAME,'to')))
WebDriverWait(browser,delay).until(EC.visibility_of(recElem))
toElem = browser.find_element_by_name("to")
toElem.send_keys(''.join(sys.argv[1]))
subElem = WebDriverWait(browser,delay).until(EC.presence_of_element_located((By.NAME,'subjectbox')))
subjectElem = browser.find_element_by_name("subjectbox")
subjectElem.send_keys(''.join(sys.argv[2]))
mesgElem = WebDriverWait(browser,delay).until(EC.presence_of_element_located((By.ID,':rj')))
msgElem = browser.find_element_by_id(':rj')
msgElem.send_keys(' '.join(sys.argv[3:]))
sendElem = browser.find_element_by_id(':q4')
WebDriverWait(browser,delay).until(EC.element_to_be_clickable((By.ID,':q4')))
sendElem.click()




