from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

# Class de base pour créer les models
Base= declarative_base()

# Les ORM sont des classes python basée sur les tables de notre base de données
class Products(Base):
    __tablename__= "product"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    model = Column(String, nullable=False)
    color = Column(String, nullable=False)
    featured = Column(String, nullable=False) # server_default permet de donner une valeur par default
    

class Customers(Base):
    __tablename__="customer"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    create_at= Column(TIMESTAMP(timezone=True), nullable=False, server_default='now()')  

class Transactions(Base):
    __tablename__="transaction"
    id= Column(Integer, primary_key=True, nullable=False)
    customer_id= Column(Integer, ForeignKey("customer.id", ondelete="RESTRICT"), nullable=False)  # Les Foreign Keys sont basés sur les clé principales des autres tables mais ce n'est pas obligatoire
    product_id = Column(Integer, ForeignKey("product.id", ondelete="RESTRICT"), nullable=False) # ondelete permet de choisir la cascade d'action suite à la suppression (supprimer une transation, doit-elle suppimer le customer ou le produit?)
    transaction_date=Column(TIMESTAMP(timezone=True), nullable=False, server_default="now()")