
from src.schemas import BaseTypeProductSchemas
from src.models.models import type_products
from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.auth import get_api_key
from fastapi.security.api_key import APIKey


router_type_product = APIRouter(
    prefix="/type_product",
    tags=["Типы продукции"],
)


@router_type_product.get("/get_all_type_products")
async def get_all_type_products(
    session: AsyncSession = Depends(get_async_session),
    api_key: APIKey = Depends(get_api_key)
):
    try:
        query = select(type_products)
        result = await session.execute(query)
        value = result.mappings().all()
        response = {
            "status": "success",
            "data": value,
            "details": "Типы продуктов успешно получены"
        }
        # return paginate(session, query)
        return response
    except:
        raise HTTPException(
            status_code=500,
            detail='Ошибка при получении типов продуктов'
        )
        

@router_type_product.post("/add_type_products")
async def add_type_products(
    # new_type_products: BaseTypeProductSchemas,
    session: AsyncSession = Depends(get_async_session),
    api_key: APIKey = Depends(get_api_key)
):
    try:
        fake_types = [
            {"name": "Камеры", "description": "Чтобы фотать"},
            {"name": "Объективы", "description": "Чтобы фотать"},
            #3,"name": "Стабилизация и штативы", "description": "Чтобы фотать"},
            #4,"name": "Операторское оборудование", "description": "Чтобы фотать"},
            #5,"name": "Световое оборудование", "description": "Чтобы фотать"},
            #6,"name": "Звуковое оборудование", "description": "Чтобы фотать"},
            #7,"name": "Аксессуары", "description": "Чтобы фотать"},
            # {"name": "Транспорт", "description": "Чтобы фотать"},
            
            {"name": "Электроные стабилизаторы", "description": "Чтобы фотать"},
            {"name": "Штативы и моноподы", "description": "Чтобы фотать"},
            {"name": "Механическая стабилизация", "description": "Чтобы фотать"},
            
            {"name": "Видеомониторы", "description": "Чтобы фотать"},
            {"name": "Сендеры", "description": "Чтобы фотать"},
            {"name": "Суфлеры", "description": "Чтобы фотать"},
            {"name": "Компендиумы", "description": "Чтобы фотать"},
            {"name": "Фильтры", "description": "Чтобы фотать"},
            {"name": "Коммутация", "description": "Чтобы фотать"},
            {"name": "Камерный обвес", "description": "Чтобы фотать"},
            
            {"name": "LED - приборы", "description": "Чтобы фотать"},
            {"name": "Стойки и грипп", "description": "Чтобы фотать"},
            {"name": "Светоформирующие насадки", "description": "Чтобы фотать"},
        
            {"name": "Рекордеры", "description": "Чтобы фотать"},
            {"name": "Петличные системы", "description": "Чтобы фотать"},
            {"name": "Накамерные микрофоны", "description": "Чтобы фотать"},
            {"name": "Направленные микрофоны", "description": "Чтобы фотать"},
            {"name": "Комплектующие", "description": "Чтобы фотать"},
        
            {"name": "Карты памяти", "description": "Чтобы фотать"},
            {"name": "Спецэффекты", "description": "Чтобы фотать"},
            {"name": "Услуги", "description": "Чтобы фотать"},
            {"name": "Кабеля", "description": "Чтобы фотать"},
            {"name": "Аккумуляторы", "description": "Чтобы фотать"},
        
            {"name": "Технические машины", "description": "Чтобы фотать"},
            {"name": "Машины для съемочной группы", "description": "Чтобы фотать"},
            
        ]

        stmt = insert(type_products).values(fake_types)
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "details": "Тип продукта успешно добавлен"
        }
    except:
        raise HTTPException(
            status_code=500,
            detail='Ошибка при получении типов продуктов'
        )