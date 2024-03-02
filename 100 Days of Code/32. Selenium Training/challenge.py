from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://www.python.org")
eventname = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")
time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu time")
eventnamelist = [item.text for item in eventname]
timelist = [item.get_attribute('datetime').split('T')[0] for item in time]

dictionary = {}
for each in range(len(timelist)):
    insidedict = {'time':timelist[each], 'name':eventnamelist[each]}
    dictionary[each] = insidedict

print(dictionary)