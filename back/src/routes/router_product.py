
from src.schemas import BaseProductSchemas
from src.models.models import products
from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.models.models import cart


router_product = APIRouter(
    prefix="/product",
    tags=["Продукция"],
)

@router_product.get("/get_all_products")
async def get_all_products(
    session: AsyncSession = Depends(get_async_session),
):

        query = select(products)
        result = await session.execute(query)
        value = result.mappings().all()
        response = {
            "status": "success",
            "data": value,
            "details": "Продукты успешно получены"
        }
        # return paginate(session, query)
        return response

@router_product.get("/get_products/{type_products_id}")
async def get_products_by_type(
        type_products_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(products).where(
        products.c.type_products_id == type_products_id
        )
        result = await session.execute(query)
        value = result.mappings().all()
        response = {
            "status": "success",
            "data": value,
            "details": "Продукты успешно получены"
        }
        # return paginate(session, query)
        return response
    except:
        raise HTTPException(
            status_code=500,
            detail='Ошибка при получении типов продуктов'
        )

@router_product.post("/add_products")
async def add_products(
    new_products: BaseProductSchemas,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        stmt = insert(products).values(**new_products.model_dump()).returning(products.c.id)
        result = await session.execute(stmt)
        await session.commit()
        value_id = result.first()[0]
        query = select(products).where(
            products.c.id == value_id
        )
        result = await session.execute(query)
        value = result.mappings().first()
        return {
            "status": "success",
            "data": value,
            "details": "Продукт успешно добавлен"
        }
    except:
        raise HTTPException(
            status_code=500,
            detail='Ошибка при добавлении продуктов'
        )

@router_product.delete("/delete_product/{id}") 
async def delete_product( 
        id: int, 
        session: AsyncSession = Depends(get_async_session), 
): 
    try: 
        query = delete(products).where( 
            products.c.id == id 
        ) 
        # query_s = delete(cart).where( 
        #     cart.c.product_id == id 
        # ) 
        result = await session.execute(query) 
        # result_s = await session.execute(query) 
        await session.commit() 
        return { 
            "status": "success", 
            "details": "Продукт удален и из корзин пользователей тоже" 
        } 
    except: 
        raise HTTPException( 
            status_code=500, 
            detail='Ошибка при удалении корзины' 
        )