gfromlink = "https://forms.gle/YAJpSozFYDzunPe59"
zillowclone = "https://appbrewery.github.io/Zillow-Clone/"

from bs4 import BeautifulSoup
import requests

response = requests.get(zillowclone)
soup = BeautifulSoup(response.text, "html.parser")
harga = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
alamat = soup.find_all(name="address")
link = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")

pricelist = [each.getText().split("+")[0].split("/")[0] for each in harga]
linklist = [each.get("href") for each in link]
addresslist = [each.getText().strip().replace("|", "") for each in alamat]

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_opt = Options()
chr_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get(gfromlink)



for i in range(44):
    addressinput = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    priceinput = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    linkinput = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submitbutton = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    
    addressinput.send_keys(addresslist[i])
    priceinput.send_keys(pricelist[i])
    linkinput.send_keys(linklist[i])
    submitbutton.click()
    time.sleep(1)
    driver.refresh()
    time.sleep(3)

