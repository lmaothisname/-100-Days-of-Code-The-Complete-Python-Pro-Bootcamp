from bs4 import BeautifulSoup
import lxml
with open(r"D:\python\Day 45\bs4-start\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify())
print(soup.title.string)
print(soup.title.name)  
all_anchor_tag=soup.find_all(name="a")
print(all_anchor_tag)

for tag in all_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))
heading = soup.find(name="h1",id="name")
print(heading)
section_heading = soup.find(name="h3",class_="heading")  
print(section_heading.getText())
company_url=soup.select_one(selector="p a")
print(company_url)
heading=soup.select(selector=".heading")
print(heading)