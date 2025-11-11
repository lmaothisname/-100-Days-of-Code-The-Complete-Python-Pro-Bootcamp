import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")
title_movie = soup.find_all(name="h3",class_="title")
title_all=[]
title_all.reverse()
for title in title_movie:
    title_all.append(title.getText())
title_all.reverse()
with open(r"D:\Python\Day 45\Starting Code - 100 movies to watch start\movies.txt","w",encoding="utf-8") as file:
    for index in range(len(title_all)):
        file.write(title_all[index]+"\n")
