import requests
from bs4 import BeautifulSoup

from common import Common
from db import DBManagement as db
from get_all_brands_url import GetAllBrandsURL
from woker import Worker


class GetBrandsURL:

    @staticmethod
    def main(brand: dict):
        url = brand[2]
        brand = brand[1]
        print(f'start crawling {brand}')
        re = requests.get(url)
        soup = BeautifulSoup(re.content, "html.parser")
        params = {
            'brand': brand,
            'url': url,
            'soup': soup
        }
        GetAllBrandsURL(params=params)

    def __init__(self):
        max_worker = Common.max_worker()
        brands_url = db.fetch_datas(db_file=db.db_file(), table_name=db.db_table()[1], all_columns=True)
        '''
        for i in range(len(brands_url)):
            brand_name = brands_url[i][1]
            brand_url = brands_url[i][2]
            if brand_url != '' or brand_url is not None:
                brand = {'brand': brand_name, 'url_address': brand_url}
                self.main(brand)
        '''
        Worker(fn=self.main, data=brands_url, max_worker=max_worker)
