from datetime import datetime 

def product_text(product : object):
    print(product)
    # return 'Строкая'
    return f'Название: {product["name"]} \nОписание: {product["description"]} \nСтоимость в смену: {product["price"]}руб. \nКомплектация: {product["equipment"]} \nКоличество в шт: {product["count"]}шт.'
#   
    # return f'Наименование: {product['name']} \nСтоимость в смену: {product['price']} \nКомплектакция: {product['equipment']} \n Наличие: {product['equipment']}шт.'
# return f'Наименование: {product.name} \n Стоимость в смену: {product.price} \n Комплектакция: {product.equipment} \n Наличие: {product.equipment}шт.'

async def cart_entry(cart):
    mes = ''
    if (cart) :
        for index, val in enumerate(cart):
            mes += f'{index + 1}. {val["product"]["name"]}  {val["product"]["description"]}\n' 
        return mes 
    else:
        return 'Ошибка какая-то'
    

async def cart_push(cart, fio, tag, comment):
    newdate = datetime.now()  
    newdate = newdate.strftime("%d.%m.%Y")
    mes = ''
    if (cart) :
        for index, val in enumerate(cart):
            mes += f'{index + 1}. {val["product"]["name"]}\n' 
        return f'Пользователь,  \n{fio} оформил заказ  {newdate}:\n{mes} \nДля связи - @{tag}\nКомментарий пользователя: {comment}'
    else:
        return 'Ошибка какая-то'