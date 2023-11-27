import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.amazon.com/gp/bestsellers/handmade/ref=zg_bs_handmade_sm"
headers= ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.9'})
source= requests.get(url,headers)
soup= BeautifulSoup(source.text,'html.parser')
products = soup.find('div',class_='product-list__inner').find_all('div',class_='product-item__info')
product_name = []
for product in products:
    name = product.find('a',class_='product-item-meta__title').text.replace('\n','')
    product_name.append(name)
product_price = []
for product in products:
    price = product.find('div',class_='product-item-meta__price-list-container').text.replace('Sale priceFrom','').replace('\n','')
    product_price.append(price)
dataset = {"product_name":(product_name),"product_price":(product_price)}
df = pd.DataFrame(dataset)
df.to_csv(r'C:\Users\pc-1\Downloads\Amazon_product_data.csv')
