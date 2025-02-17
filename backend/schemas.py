from pydantic import BaseModel
from datetime import datetime

class TransactionBase(BaseModel):
    type: str
    amount: float
    category: str
    date: datetime

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    class Config:
        from_attributes = True

class Balance(BaseModel):
    total: float
