from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from sqlalchemy import text
from sqlalchemy.orm import Session

from database.dependency import get_db
from schemas.respons import ResponseSchema

from core.exception import AppException
from api.category import router as category_router
from api.unit import router as unit_router
from api.transactionType import router as transaction_type_router
from api.product import router as product_router
from api.transaction import router as transaction_router
from api.transactionItem import router as transaction_item_router
from api.productSupplier import router as product_supplier_router
from api.supplier import router as supplier_router




app = FastAPI()
# menjalankan perintah uvicorn main:app --reload untuk menjalankan server
app.include_router(category_router)
app.include_router(unit_router)
app.include_router(transaction_type_router)
app.include_router(product_router)
app.include_router(transaction_router)
app.include_router(transaction_item_router)
app.include_router(product_supplier_router)
app.include_router(supplier_router)

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