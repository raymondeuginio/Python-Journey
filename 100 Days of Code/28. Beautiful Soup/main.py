from bs4 import BeautifulSoup
import requests

# response = requests.get("https://news.ycombinator.com/")
# yc_web = response.text

# soup = BeautifulSoup(yc_web, "html.parser")
# articles = soup.select(selector=".titleline a")
# article_texts = []
# article_links = []

# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)

# article_upvotes = [int(score.getText().split()[0]) for score in soup.select(selector="span .score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)
# largestpoint = max(article_upvotes)
# print(largestpoint)
# gabungin 3 list jadi 1 dictionary / list 

# listangka = [172, 540, 540, 54, 69, 138, 158, 100, 63, 163, 57, 260, 60, 12, 5, 76, 205, 187, 223, 173, 116, 142, 144, 49, 119, 376, 116, 47, 286, 96, 409]
# tb = max(listangka)
# indextb = listangka.index(tb)
# print(tb)
# print(indextb)






# import lxml
with open ("./28. Beautiful Soup/website.html", encoding="utf8") as file:
    text= file.read()

soup = BeautifulSoup(text, 'html.parser')
# # print(f"soup.title = {soup.title}")
# # print(f"soup.title.name = {soup.title.name}")
# # print(f"soup.title.string = {soup.title.string}")

# # print(f"soup = {soup.prettify()}")

# # print(f"soup.h3 = {soup.h3}")
# print(f"soup.find_all() = {soup.find_all('a')}")
sf = soup.find('h1', id='name')
ss = soup.select('h1, #name')
print(f"soup.find = {sf} dan tipenya = {type(sf)}")
print(f"soup.select = {ss} dan tipenya = {type(ss)}")
