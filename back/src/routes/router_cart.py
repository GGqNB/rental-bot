
from src.schemas import BaseCartSchemas
from src.models.models import cart, products
from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session


router_cart = APIRouter(
    prefix="/cart",
    tags=["Корзина"],
)

@router_cart.get("/get_all_cart")
async def get_all_cart(
    session: AsyncSession = Depends(get_async_session),
):
    query = select(cart)
    result = await session.execute(query)
    value = result.mappings().all()
    response = {
        "status": "success",
            "data": value,
            "details": "Продукты успешно получены"
        }
        # return paginate(session, query)
    return response

@router_cart.get("/get_cart/{user_id}")
async def get_cart_by_user(
        user_id: str,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(cart).where(
        cart.c.user_id == user_id
        )
        result = await session.execute(query)
        value = result.mappings().all()
        
        carts_w_product = []
        
        for elem in value:
            new_elem = dict(elem)
            query2 = select(products).where(
            products.c.id == elem['product_id']
            )
            result2 = await session.execute(query2)
            value2 = result2.mappings().all()
            new_elem['product'] = value2[0]
            carts_w_product.append(new_elem)
            
        response = {
            "status": "success",
            "data": carts_w_product,
            "details": "Продукты успешно получены"
        }
        # return paginate(session, query)
        return response
    except:
        raise HTTPException(
            status_code=500,
            detail='Ошибка при получении типов продуктов'
        )



@router_cart.post("/add_carts")
async def add_cart(
    new_products: BaseCartSchemas,
    session: AsyncSession = Depends(get_async_session),
):
    # try:
        stmt = insert(cart).values(**new_products.model_dump()).returning(cart.c.id)
        result = await session.execute(stmt)
        await session.commit()
        value_id = result.first()[0]
        query = select(cart).where(
            cart.c.id == value_id
        )
        result = await session.execute(query)
        value = result.mappings().first()
        return {
            "status": "success",
            "data": value,
            "details": "Продукт успешно добавлен"
        }
    # except:
    #     raise HTTPException(
    #         status_code=500,
    #         detail='Ошибка при добавлении продуктов'
    #     )

@router_cart.delete("/delete_cart/{cart_id}") 
async def delete_cart( 
        cart_id: int, 
        session: AsyncSession = Depends(get_async_session), 
): 
    try: 
        query = delete(cart).where( 
            cart.c.id == cart_id 
        ) 
        result = await session.execute(query) 
        await session.commit() 
        return { 
            "status": "success", 
            "details": "Корзина успешно удалена" 
        } 
    except: 
        raise HTTPException( 
            status_code=500, 
            detail='Ошибка при удалении корзины' 
        )
        
@router_cart.delete("/delete_cart_user/{user_id}") 
async def delete_all_carts_by_user( 
        user_id: str, 
        session: AsyncSession = Depends(get_async_session), 
): 
    try: 
        query = delete(cart).where( 
            cart.c.user_id == user_id 
        ) 
        result = await session.execute(query) 
        await session.commit() 
        return { 
            "status": "success", 
            "details": "Корзина успешно удалена1231" 
        } 
    except: 
        raise HTTPException( 
            status_code=500, 
            detail='Ошибка при удалении корзины' 
        )

@router_cart.delete("/delete_cart_product/{product_id}") 
async def delete_all_carts_by_product( 
        product_id: int, 
        session: AsyncSession = Depends(get_async_session), 
): 
    try: 
        query = delete(cart).where( 
            cart.c.product_id == product_id 
        ) 
        result = await session.execute(query) 
        await session.commit() 
        return { 
            "status": "success", 
            "details": "Корзина для удаления картов по продуктам" 
        } 
    except: 
        raise HTTPException( 
            status_code=500, 
            detail='Ошибка при удалении корзины' 
        )
        
        
# @router_cart.get("/get_cart/{user_id}")
# async def get_cart_by_user(
#     user_id: int,
#     session: AsyncSession = Depends(get_async_session),
# ):
#     # try:
#         query = select(cart).where(
#             cart.c.user_id == user_id
#         )
#         result = await session.execute(query)
#         value = result.mappings().all()

#         product_ids = [item['product_id'] for item in value]

#         # Fetch product information for the product IDs in the cart
#         product_query = select(products).where(
#             products.c.id.in_(product_ids)
#         )
#         product_result = await session.execute(product_query)
#         product_mapping = {item['id']: item for item in product_result.mappings().all()}

#         # Match the product information with the cart items
#         for item in value:
#             product_id = item['product_id']
#             product_info = product_mapping.get(product_id)
#             item['product'] = product_info

#         response = {
#             "status": "success",
#             "data": value,
#             "details": "Продукты успешно получены"
#         }

#         return response
#     # except:
#     #     raise HTTPException(
#     #         status_code=500,
#     #         detail='Ошибка при получении типов продуктов'
#     #     )