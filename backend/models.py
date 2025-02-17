class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    amount = Column(Float)
    category = Column(String)
    date = Column(DateTime)
