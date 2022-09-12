from requests_html import HTMLSession
import pandas as pd
from unidecode import unidecode


df = pd.DataFrame()

session = HTMLSession()

url = 'https://www.amazon.com.br/gp/bestsellers/?ref_=nav_cs_bestsellers'

r = session.get(url)

r.html.render(sleep=1)


product_name = r.html.find(
    '.p13n-sc-truncate-desktop-type2'
)

price = r.html.find(
    "._p13n-zg-list-carousel-desktop_price_p13n-sc-price__3mJ9Z"
)

links = r.html.find(
    '.a-link-normal'
)

# print(links[0].absolute_links)
product_list = []
for i, j in enumerate(product_name):
    try:
        product_name_text = product_name[i].text

        price_text = price[i].text

        price_text = price_text.replace('R$', '')

        print(product_name_text, price_text)
        info = {
            "product_name": unidecode(product_name_text),
            "price": unidecode(price_text),
        }
        product_list.append(info)
    except:
        pass

df = df.append(product_list, ignore_index=True)

df.to_csv('Amazon_BestSellers.csv')
