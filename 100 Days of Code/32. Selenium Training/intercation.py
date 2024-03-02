from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_opt = Options()
chrome_opt.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.set_window_size(1080,1000)
driver.get("https://secure-retreat-92358.herokuapp.com/")
# number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# number.click()

Fname = driver.find_element(By.NAME, value="fName")
Fname.send_keys("Johannes")
Lname = driver.find_element(By.NAME, value="lName")
Lname.send_keys("Karl")
email = driver.find_element(By.NAME, value="email")
email.send_keys("Johanneskarl35@gmail.com")

signbutton = driver.find_element(By.CSS_SELECTOR, value=".btn")
signbutton.click()

time.sleep(1000)