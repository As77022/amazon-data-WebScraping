import requests
import pandas as pd
from bs4 import BeautifulSoup
# Copy URL from that page, which you want to extract data from.
url="https://www.amazon.com/gp/bestsellers/handmade/ref=zg_bs_handmade_sm"
# To get header enter this url in your browser (https://httpbin.org/get)
header= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
source = requests.get(url,headers=header)
soup = BeautifulSoup(source.text,'html.parser')
page = soup.find('div',class_='p13n-gridRow _cDEzb_grid-row_3Cywl').find_all('div',class_='p13n-sc-uncoverable-faceout')
# Individuals create a list for each parameter and store the list in a variable.
product_name = []
for list in page:
    name = list.find('div',class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1').text
    product_name.append(name)
product_star = []
for list in page:
    star = list.find('a',class_='a-link-normal').text
    product_star.append(star)
product_rating = []
for list in page:
    rating = list.find('span',class_='a-size-small').text
    product_rating.append(rating)
product_price = []
for list in page:
    price = list.find('div',class_='a-row').text
    product_price.append(price)
# Convert this individual list into dataframe with the help of pandas library.
data = {"Product_name": product_name, "product_star": product_star,"product_rating":product_rating,"product_price":product_price}
df= pd.DataFrame(data)
# Store this extracted data into csv file for storage/ analysis purposes.
df.to_csv(r'C:\Users\AVATAR\Downloads\Amazon_product_data.csv')

