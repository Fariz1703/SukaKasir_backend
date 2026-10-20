from fastapi import APIRouter, Depends, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.common.respons import ResponseSchema
from schemas.common.createTransaction import (
    CreateTransactionCreate,
    CreateTransactionResponse,
)
from service.createTranscation import (
    CreateCreateTransaction,
)

router = APIRouter(
    prefix="/api/v1/create_transactions",
    tags=["create_transactions Movile V1"]
)

@router.post(
    "",
    response_model=ResponseSchema[CreateTransactionResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    create_transaction_data:CreateTransactionCreate,
    db: Session = Depends(get_db)
):
    create_transaction = CreateCreateTransaction(db,create_transaction_data)

    if create_transaction is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create Product"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "Product created succesfully",
        "data" : create_transaction
    }