from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.schemas import BaseProductSchemas, BaseTypeProductSchemas, ReadTypeProductSchemas, ReadProductSchemas
from src.models.models import users, products, type_products, cart
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import update, insert, select
from src.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination.ext.sqlalchemy import paginate
from src.routes.router_product import router_product
from src.routes.router_type_product import router_type_product
from src.routes.router_cart import router_cart

app = FastAPI(
    title="НЕГРЫЫ ААА",
    description='CAMERA_BOT'
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_all_users")
async def get_all_users(
    session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(users)
        result = await session.execute(query)
        value = result.mappings().all()
        response = {
            "status": "success",
            "data": value,
            "details": "Пользователи успешно получены"
        }
        # return paginate(session, query)
        return response
    except:
        raise HTTPException(
            status_code=500,
            detail='Ошибка при получении пользователей'
        )



        

        

app.include_router(router_cart)
app.include_router(router_type_product)
app.include_router(router_product)
