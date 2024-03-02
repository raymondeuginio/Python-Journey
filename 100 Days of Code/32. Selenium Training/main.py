from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program finishes
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome()
# memerlukan jembatan yang menghubungkan antara selenium dengan browser yang kita gunakan
driver.get("https://www.tokopedia.com/distrilapid/apple-macbook-air-m2-chip-2023-15-inch-512gb-256gb-ram-8gb-not-pro-512gb-inter-midnight-a68e5?extParam=ivf%3Dtrue&src=topads")
harga = driver.find_element(By.CLASS_NAME, value = "price")
print(harga.text)
print(harga.screenshot(filename="./32. Selenium Training/screenshot.png"))
# driver.close() #close the active tab particular page
driver.quit() #quit the entire browser/program
