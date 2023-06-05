from pdp_elements import PDPElements


class PriceTable:

    @staticmethod
    def main(soup):
        price = PDPElements.price(soup)
        title = PDPElements.title(soup)
        variants = []
        variant_ = {
            'price': price,
            'product_name': title
        }
        variants.append(variant_)
        return variants
