def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session):
    return db.query(models.Transaction).all()

def get_balance(db: Session):
    total = db.query(models.Transaction).with_entities(func.sum(models.Transaction.amount)).scalar() or 0
    return {"total": total}
