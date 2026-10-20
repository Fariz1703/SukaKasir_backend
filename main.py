from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from sqlalchemy import text
from sqlalchemy.orm import Session

from database.dependency import get_db
from schemas.common.respons import ResponseSchema

from core.exception import AppException

#web router
from api.web.category import router as web_category_router
from api.web.unit import router as web_unit_router
from api.web.transactionType import router as web_transaction_type_router
from api.web.product import router as web_product_router
from api.web.transaction import router as web_transaction_router
from api.web.transactionItem import router as web_transaction_item_router
from api.web.productSupplier import router as web_product_supplier_router
from api.web.supplier import router as web_supplier_router
from api.web.createTransaction import router as web_create_transaction_router

#mobile route
from api.mobile.V1.createTransaction import router as create_transaction_router
from api.mobile.V1.product import router as mobile_product_router
from api.mobile.V1.category import router as mobile_category_router
from api.mobile.V1.supplier import router as mobile_supplier_router
from api.mobile.V1.unit import router as mobile_unit_router
from api.mobile.V1.transactionType import router as mobile_transactionType_router


app = FastAPI()
# menjalankan perintah uvicorn main:app --reload untuk menjalankan server
app.include_router(web_category_router)
app.include_router(web_unit_router)
app.include_router(web_transaction_type_router)
app.include_router(web_product_router)
app.include_router(web_transaction_router)
app.include_router(web_transaction_item_router)
app.include_router(web_product_supplier_router)
app.include_router(web_supplier_router)
app.include_router(web_create_transaction_router)

#Mobile Route
app.include_router(create_transaction_router)
app.include_router(mobile_product_router)
app.include_router(mobile_category_router)
app.include_router(mobile_supplier_router)
app.include_router(mobile_unit_router)
app.include_router(mobile_transactionType_router)


@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    response = ResponseSchema(
        success=False,
        status_code=exc.status_code,
        message=exc.message,
        data=exc.data,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(),
    )

@app.get("/")
def root():
    return {
        "message": "API is running"
    }


@app.get("/test-db")
def test_db(
    db: Session = Depends(get_db),
):
    result = db.execute(text("SELECT 1"))

    return {
        "database": result.scalar()
    }