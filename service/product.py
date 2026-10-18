from sqlalchemy.orm import Session

from models.product import Product
from schemas.product import ProductCreate, ProductUpdate,ProductResponse
from core.storage import get_image_url

def create_product(
    db: Session,
    product_data: ProductCreate,
    image_key: str
) -> ProductResponse:

    if image_key is not None:    
        product = Product(
            name=product_data.name,
            category_id=product_data.category_id,
            image_key = image_key,
            unit_id=product_data.unit_id,
            sku=product_data.sku,
            unit_size=product_data.unit_size,
            sell_price=product_data.sell_price,
        )
    else:
        product = Product(
            name=product_data.name,
            category_id=product_data.category_id,
            unit_id=product_data.unit_id,
            sku=product_data.sku,
            unit_size=product_data.unit_size,
            sell_price=product_data.sell_price,
        )

    db.add(product)
    db.commit()
    db.refresh(product)

    image_url=get_image_url(product.image_key)

    product_response = ProductResponse(
        id=product.id,
        name=product.name,
        category_id=product.category_id,
        unit_id=product.unit_id,
        sku=product.sku,
        unit_size=product.unit_size,
        sell_price=product.sell_price,
        stock=product.stock,
        created_at=product.created_at,
        updated_at=product.updated_at,
        image_url=image_url,
    )

    return product_response

def get_product(
    db: Session,
    product_id: int
) -> Product | None:

    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

def get_some_product(
    db: Session,
    product_id: list[int]
) -> list[ProductResponse]:

    Products=db.query(Product).filter(Product.id.in_(product_id)).all()

    product_data=[]

    for product in Products:
        image_url=get_image_url(product.image_key)

        product_response = ProductResponse(
            id=product.id,
            name=product.name,
            category_id=product.category_id,
            unit_id=product.unit_id,
            sku=product.sku,
            unit_size=product.unit_size,
            sell_price=product.sell_price,
            stock=product.stock,
            created_at=product.created_at,
            updated_at=product.updated_at,
            image_url=image_url,
        )

        product_data.append(product_response)

    return product_data



def get_products(
    db: Session
) -> list[ProductResponse]:

    Products= db.query(Product).all()
    product_data=[]

    for product in Products:
        image_url=get_image_url(product.image_key)

        product_response = ProductResponse(
            id=product.id,
            name=product.name,
            category_id=product.category_id,
            unit_id=product.unit_id,
            sku=product.sku,
            unit_size=product.unit_size,
            sell_price=product.sell_price,
            stock=product.stock,
            created_at=product.created_at,
            updated_at=product.updated_at,
            image_url=image_url,
        )

        product_data.append(product_response)

    return product_data




def update_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
) -> ProductResponse | None:

    product = get_product(db, product_id)


    if product is None:
        return None


    if product.image_key is not None:
        product.image_key = product_data.image_key
    if product_data.name is not None:
        product.name = product_data.name
    if product_data.category_id is not None:
        product.category_id = product_data.category_id
    if product_data.unit_id is not None:
        product.unit_id = product_data.unit_id
    if product_data.sku is not None:
        product.sku = product_data.sku
    if product_data.stock is not None:
        product.stock = product_data.stock
    if product_data.unit_size is not None:
        product.unit_size = product_data.unit_size
    if product_data.sell_price is not None:
        product.sell_price = product_data.sell_price

    db.commit()
    db.refresh(product)

    image_url=get_image_url(product.image_key)

    product_response = ProductResponse(
        id=product.id,
        name=product.name,
        category_id=product.category_id,
        unit_id=product.unit_id,
        sku=product.sku,
        unit_size=product.unit_size,
        sell_price=product.sell_price,
        stock=product.stock,
        created_at=product.created_at,
        updated_at=product.updated_at,
        image_url=image_url,
        )

    return product_response


def delete_product(
    db: Session,
    product_id: int
) -> Product | None:

    product = get_product(db, product_id)

    if product is None:
        return None

    db.delete(product)
    db.commit()

    return product