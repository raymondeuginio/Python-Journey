import requests
from bs4 import BeautifulSoup

# make a request to get html txt
amazonurl = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
acceptlang = "en-US,en;q=0.9,id;q=0.8,fr;q=0.7"

header = {
    # "User-Agent" : useragent
    "Accept-language" : acceptlang
    # "sec-ch-ua-platform":"Windows",
    # "Accept-Encoding":"gzip, deflate, br",
    # "Cookie":"_ga=GA1.2.141175145.1705291038; _ga_VL41109FEB=GS1.2.1705291038.1.0.1705291038.0.0.0"
}

response = requests.get(url=amazonurl, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
pricelist = soup.find_all(name="span", class_="a-price-whole")
realprice = int(price[1].getText())
