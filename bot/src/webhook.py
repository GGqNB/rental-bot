import requests
from config import BACK_URL
from config import API_KEY

headers = {'Access_token': API_KEY}

async def request_product(id : str):
    response = requests.get(BACK_URL+'/product/get_products/'+id, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return data

async def my_cart(user_id : str):
    response = requests.get(BACK_URL+'/cart/get_cart/'+user_id, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
        
    else:
        return data

async def add_cart(product_id, user_id, headers=headers):
    # print(user_id)
    # print('ПРОДУКТ'+product_id)
    url = BACK_URL + '/cart/add_carts'
    data = {
        'product_id': product_id,
        'user_id': str(user_id)
    }
    response = requests.post(url, json=data)
    print(response)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

async def clear_cart(user_id):
    response = requests.delete(BACK_URL+'/cart/delete_cart_user/'+user_id, headers=headers)
    
    if response.status_code == 200:
        print(response)
        data = response.json()
        
        return data
    else:
        return data