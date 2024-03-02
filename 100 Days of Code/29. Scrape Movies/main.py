import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
soup = BeautifulSoup(response.text,"html.parser")
# movietitle = soup.select(selector="h3 .title") -> ini sama aja kea selector antara h3 dan .title bukan h3 yang memiliki title (notes: tidak bisa h3, .title) jadi harus pake find_all. 
movies = soup.find_all(name="h3", class_= "title")
movietitles = [title.getText() for title in movies]
movietitles.reverse()

with open("./29. Scrape Movies/movies.txt", mode="a", encode="utf-8") as file:
    for each in movietitles:
        file.write(f"{each}\n")