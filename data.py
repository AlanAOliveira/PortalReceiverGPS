import requests
from bs4 import BeautifulSoup

# Define the URL of the web page to scrape
url = 'https://toyotabrasil.sharepoint.com/sites/memorial_dwg_materiais_gps/_api/search/query?querytext=%27YG79140013*.pdf%27&querytemplatepropertiesurl=%27spfile://webroot/queryparametertemplate.xml%27'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(response.content, 'lxml-xml')

print(soup)

# Accessing the root element
root = soup.data

# Finding all 'item' tags
items = soup.find_all('item')

# Accessing children and attributes
for item in items:
    item_id = item['id']
    name = item.name.text
    price = item.price.text
    print(f"ID: {item_id}, Name: {name}, Price: {price}")