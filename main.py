from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# article_text = soup.select_one(selector=".titleline a" ).getText()

article_text = soup.select_one(selector=".titleline a" ).getText()

print(article_text)
articles = soup.find_all(name="span", class_="titleline")

articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(f"votes: {articles_upvotes}")

articles_dic = [{f"{article.find(name='a').getText()}": article.find(name='a').get("href")} for article in articles]
print(articles_dic)

largest_number = max(articles_upvotes)
print(largest_number)

index_of_largest_number = articles_upvotes.index(largest_number)
print(index_of_largest_number)

article_of_largest_number = articles_dic[index_of_largest_number]
print(article_of_largest_number)






# with open('website.html', encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string)
#
# print(soup.prettify())
#
# print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
#
# anchor_tags_texts = [tag.getText() for tag in all_anchor_tags]
# print(anchor_tags_texts)
#
# anchor_tags_links = [tag.get("href") for tag in all_anchor_tags]
# print(anchor_tags_links)
#
# heading = soup.find(name="h1", id="name")
#
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a").get("href")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)
