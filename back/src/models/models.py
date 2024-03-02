from sqlalchemy import MetaData, Table, Column, String, ForeignKey, Integer, Boolean

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)


type_products = Table(
    "type_products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("price", String),
    Column("equipment", String),
    Column("count", Integer),
    Column("status", Boolean, default=False),
    Column("photo", String),
    
    Column("type_products_id", Integer, ForeignKey(type_products.c.id, ondelete="CASCADE")),
)


cart = Table(
    "cart",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", String),
    Column("product_id", Integer, ForeignKey(products.c.id,  ondelete="CASCADE")),
)