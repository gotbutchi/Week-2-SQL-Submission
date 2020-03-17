from loguru import logger
from database import Database
from model import Category, Product
import configparser
from flask import Flask, render_template 

BASE_URL = 'https://tiki.vn/'

def get_categories():
    pass

def get_products_by_category():
    pass

def get_product(save_db=False):
    query = """
    SELECT id, name, url FROM categories
    WHERE parent_id BETWEEN 100 AND 113;
    """
    try:
        cur.execute(query)
    except Exception as err:
        print('ERROR BY SELECT TABLE', err)

    rows = cur.fetchall()
    
    for i in rows:
        id = i[0]
        name = " ".join(i[1].strip().split()[:-1])
        url = i[2].strip()
        for page in range(1,4):
            page_url = url + "&page=" + str(page)
#             print(page_url)
            page_html = get_url(page_url)
            try:
                products_wrapper_div = page_html.find_all('div', class_='product-box-list')[0]
            except Exception as err:
                 print('ERROR BY DIV FINDALL: ', err)
            if products_wrapper_div:
                products_div = products_wrapper_div.find_all('div', class_='product-item')
                result = []
                if len(products_div) > 0:
                    for product_div in products_div:
                        product_id = None
                        title = product_div.a['title']
                        url = product_div.a['href']
                        img_url = product_div.img['src']
                        regular_price = product_div.find('span', class_='price-regular').text
                        final_price = product_div.find('span', class_='final-price').text.split()[0]
                        sale_tag = product_div.find('span', class_='sale-tag').text
                        comment = product_div.find('p', class_='review').text.split()[0] + ' review(s))'
                        if product_div.find('span', class_='rating-content'):
                            rating = product_div.find('span', class_='rating-content').find('span')['style'].split(":")[-1]
                        else:
                            rating = '0%'
                        product = Product(product_id, name, url, img_url, regular_price, final_price, sale_tag, comment, rating, id)

                        if save_db:
                            product.save_into_db()
                            print(f'SAVE {title} INTO DB')
                        result.append(product)
                else:
                    break

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")

    app = Flask(__name__)
    app.config['TESTING'] = config["DEFAULT"]["Debug"]

    @app.route('/')
    def index():
        return render_template('index.html')

    app.run(host="127.0.0.1", port=8000, debug=True)
    logger.debug("Flash server is running!")
