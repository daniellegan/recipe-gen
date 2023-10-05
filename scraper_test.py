from bs4 import BeautifulSoup
import requests
import re
import extruct
from recipe_scrapers import scrape_html, scrape_me

url = "https://www.kingarthurbaking.com/recipes/easy-cheesecake-recipe"
scraper = scrape_me(url)
ingredients, instructions = scraper.ingredients()[0], scraper.instructions()
text = "ingredients: {} \ninstructions: {}".format(ingredients, instructions)
# text = "ingredients: {} \ninstructions: {}".format(scraper.ingredients()[0], scraper.instructions())
print(text)
# textt = "ingredients: " + scraper.ingredients()[0] + "\ninstructions: " + scraper.instructions()
# print("ingredients: ", scraper.ingredients()[0], "\ninstructions: ", scraper.instructions())
# print(textt)
# print("".join("ingredients: ", scraper.ingredients()[0], "\ninstructions: ", scraper.instructions()))
# html = requests.get(url).content
# scraper2 = scrape_html(html=html, org_url=url)
# print(scraper2.ingredients())

def get_html(url):
    response = requests.get(url)
    return response.text, response.url

html_doc, url  = get_html("https://www.kingarthurbaking.com/recipes/easy-cheesecake-recipe")


# # print(html_doc, url )

# data = extruct.extract(html_doc, url, syntaxes=["json-ld"])
# print(data)
# print("json: ")
# print(data.get('json-ld'))
# print(data.get('json-ld')[0].get("@graph")[0].get("recipeInstructions"))
    #   ('recipeInstructions'))
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.find("li").get_text)

# for div in soup.find_all()