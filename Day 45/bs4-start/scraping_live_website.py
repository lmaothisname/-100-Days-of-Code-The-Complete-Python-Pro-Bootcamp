from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")
articles = soup.find_all(name="tr",class_="athing")
articles_texts= []
articles_links = []
articles_points = []
for article in articles:
    title_tag=article.find(name="span",class_="titleline")
    title=title_tag.getText()
    articles_texts.append(title)
    link=title_tag.find("a").get("href")
    articles_links.append(link)
    subtext = article.find_next_sibling("tr")
    score_tag=subtext.find(name="span",class_="score")
    score = score_tag.get_text() if score_tag else "0 points"
    articles_points.append(score)

articles_points_number = [int(s.split()[0]) for s in articles_points]
# print(articles_texts)
# print(articles_links)
# print(articles_points_number)
highghest_point=max(articles_points_number)
highghest_index=articles_points_number.index(highghest_point)
print(articles_texts[highghest_index])
print(articles_links[highghest_index])
print(highghest_point)