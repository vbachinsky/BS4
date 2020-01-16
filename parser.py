from bs4 import BeautifulSoup
import requests

URL = 'https://oliopizza.com.ua/product-category/pitstsa/'

response = requests.get(URL)

content = response.text

soup = BeautifulSoup(content, 'lxml')

arr_1 = soup.find_all("div", {"class": "product-card"})

full_dict = []

for row in arr_1:
    temp_dict = {}
    name = row.find("span", {"class": "name"})
    price= row.find("span", {"class": "woocommerce-Price-amount amount"})
    text = row.find("span", {"class": "description"})
    if row.img:
    	image_url = row.img['src']
    temp_dict["name"] = str(name.contents[0]).strip()
    temp_dict["price"] = str(price.contents[0])[:-1]
    temp_dict["text"] = str(text.contents[0]).strip()
    temp_dict["image_url"] = str(image_url)
    full_dict.append(temp_dict)

print(full_dict)
