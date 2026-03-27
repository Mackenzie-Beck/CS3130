 
import requests
from bs4 import BeautifulSoup
import pandas
from urllib.parse import urljoin

url = 'https://scrapeme.live/shop/'
data=[]



while True:
    response = requests.get(url)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'html.parser') 
    product_list = soup.select('.products li')
    for product in product_list:
        product_item={}
        product_item['Name'] = product.select_one('h2.woocommerce-loop-product__title').text  # Attribute selector
        product_item['Price'] = product.select_one('span.woocommerce-Price-amount').text # class selector
        data.append(product_item)
    if next_page := soup.select_one('.next'):
        url = urljoin(url, next_page['href'])
    else:
        break
df = pandas.DataFrame(data)
df.to_csv("Products.csv", index=False, sep="|")
df.to_excel('Products.xlsx', index=False)



