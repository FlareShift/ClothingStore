import requests

class NetworkHelper:
    BASE_URL = 'http://127.0.0.1:8000/api/'

    @staticmethod
    def delete_product(product_id):
        response = requests.delete(f'{NetworkHelper.BASE_URL}products/{product_id}/')
        return response.status_code
