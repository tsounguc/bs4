from bs4 import BeautifulSoup
with open('website.html', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.string)

print(soup.prettify())

print(soup.a)

all_anchor_tags = soup.find_all(name="a")

anchor_tags_texts = [tag.getText() for tag in all_anchor_tags]
print(anchor_tags_texts)

anchor_tags_links = [tag.get("href") for tag in all_anchor_tags]
print(anchor_tags_links)

heading = soup.find(name="h1", id="name")

print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a").get("href")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
