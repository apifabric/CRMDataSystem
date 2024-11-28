# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Customer(Base):
    """description: This table stores customer information."""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    date_joined = Column(DateTime)



class Product(Base):
    """description: This table stores product details that are available for sale."""
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    stock = Column(Integer)



class Order(Base):
    """description: This table records each order placed by a customer."""
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    date_placed = Column(DateTime)
    total_amount = Column(Integer)



class OrderItem(Base):
    """description: This table captures the products in each order."""
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)



class SalesRep(Base):
    """description: This table stores information about sales representatives."""
    __tablename__ = 'sales_rep'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)



class CustomerContact(Base):
    """description: This table records customer contacts and interactions."""
    __tablename__ = 'customer_contact'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    sales_rep_id = Column(Integer, ForeignKey('sales_rep.id'))
    contact_date = Column(DateTime)
    notes = Column(String)



class Category(Base):
    """description: This table stores product categories."""
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)



class ProductCategory(Base):
    """description: This table maps products to categories."""
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    category_id = Column(Integer, ForeignKey('category.id'))



class Discount(Base):
    """description: This table defines available discounts for products."""
    __tablename__ = 'discount'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    discount_amount = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)



class Return(Base):
    """description: This table records product returns by customers."""
    __tablename__ = 'return'

    id = Column(Integer, primary_key=True)
    order_item_id = Column(Integer, ForeignKey('order_item.id'))
    return_date = Column(DateTime)
    refund_amount = Column(Integer)



class Supplier(Base):
    """description: This table stores supplier information."""
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)



class ProductSupplier(Base):
    """description: This junction table maps products to suppliers."""
    __tablename__ = 'product_supplier'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))



# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    customer1 = Customer(first_name='John', last_name='Doe', email='johndoe@example.com', phone_number='1234567890', date_joined=date(2023, 1, 15))
    customer2 = Customer(first_name='Jane', last_name='Smith', email='janesmith@example.com', phone_number='0987654321', date_joined=date(2023, 2, 20))
    customer3 = Customer(first_name='Alice', last_name='Brown', email='alicebrown@example.com', phone_number='1122334455', date_joined=date(2023, 3, 10))
    customer4 = Customer(first_name='Bob', last_name='White', email='bobwhite@example.com', phone_number='5566778899', date_joined=date(2023, 4, 25))
    product1 = Product(name='Laptop', description='14 inch laptop', price=1000, stock=20)
    product2 = Product(name='Smartphone', description='Latest Model Smartphone', price=800, stock=50)
    product3 = Product(name='Headphones', description='Noise Cancelling', price=150, stock=100)
    product4 = Product(name='Smartwatch', description='Fitness Smartwatch', price=250, stock=60)
    order1 = Order(customer_id=1, date_placed=date(2023, 5, 1), total_amount=1150)
    order2 = Order(customer_id=2, date_placed=date(2023, 5, 17), total_amount=800)
    order3 = Order(customer_id=3, date_placed=date(2023, 6, 3), total_amount=250)
    order4 = Order(customer_id=4, date_placed=date(2023, 6, 10), total_amount=150)
    order_item1 = OrderItem(order_id=1, product_id=1, quantity=1)
    order_item2 = OrderItem(order_id=2, product_id=2, quantity=1)
    order_item3 = OrderItem(order_id=3, product_id=4, quantity=1)
    order_item4 = OrderItem(order_id=4, product_id=3, quantity=1)
    sales_rep1 = SalesRep(first_name='Emma', last_name='Brown', email='emma@example.com')
    sales_rep2 = SalesRep(first_name='Liam', last_name='Green', email='liam@example.com')
    sales_rep3 = SalesRep(first_name='Olivia', last_name='Red', email='olivia@example.com')
    sales_rep4 = SalesRep(first_name='Noah', last_name='Blue', email='noah@example.com')
    customer_contact1 = CustomerContact(customer_id=1, sales_rep_id=1, contact_date=date(2023, 5, 1), notes='Discussed new products.')
    customer_contact2 = CustomerContact(customer_id=2, sales_rep_id=2, contact_date=date(2023, 5, 5), notes='Assisted with order issues.')
    customer_contact3 = CustomerContact(customer_id=3, sales_rep_id=3, contact_date=date(2023, 5, 8), notes='Feedback on recent purchase.')
    customer_contact4 = CustomerContact(customer_id=4, sales_rep_id=4, contact_date=date(2023, 5, 10), notes='Interest in loyalty program.')
    category1 = Category(name='Electronics', description='Electronic gadgets and devices.')
    category2 = Category(name='Accessories', description='Electronic accessories.')
    category3 = Category(name='Home Appliances', description='Appliances for home use.')
    category4 = Category(name='Weables', description='Wearable technology devices.')
    discount1 = Discount(product_id=1, discount_amount=100, start_date=date(2023, 5, 1), end_date=date(2023, 5, 31))
    discount2 = Discount(product_id=2, discount_amount=150, start_date=date(2023, 6, 1), end_date=date(2023, 6, 15))
    discount3 = Discount(product_id=3, discount_amount=20, start_date=date(2023, 5, 5), end_date=date(2023, 5, 20))
    discount4 = Discount(product_id=4, discount_amount=50, start_date=date(2023, 6, 10), end_date=date(2023, 6, 25))
    return1 = Return(order_item_id=1, return_date=date(2023, 5, 3), refund_amount=50)
    return2 = Return(order_item_id=2, return_date=date(2023, 5, 20), refund_amount=75)
    return3 = Return(order_item_id=3, return_date=date(2023, 6, 5), refund_amount=25)
    return4 = Return(order_item_id=4, return_date=date(2023, 6, 15), refund_amount=30)
    supplier1 = Supplier(name='Global Inc.', address='123 Street, City', phone='111222333', email='contact@global.com')
    supplier2 = Supplier(name='Tech Corp.', address='456 Avenue, City', phone='444555666', email='info@techcorp.com')
    supplier3 = Supplier(name='Gadget Ltd.', address='789 Boulevard, City', phone='777888999', email='sales@gadget.com')
    supplier4 = Supplier(name='Device Co.', address='101 Road, City', phone='123123123', email='support@device.com')
    product_supplier1 = ProductSupplier(product_id=1, supplier_id=1)
    product_supplier2 = ProductSupplier(product_id=2, supplier_id=2)
    product_supplier3 = ProductSupplier(product_id=3, supplier_id=3)
    product_supplier4 = ProductSupplier(product_id=4, supplier_id=4)
    
    
    
    session.add_all([customer1, customer2, customer3, customer4, product1, product2, product3, product4, order1, order2, order3, order4, order_item1, order_item2, order_item3, order_item4, sales_rep1, sales_rep2, sales_rep3, sales_rep4, customer_contact1, customer_contact2, customer_contact3, customer_contact4, category1, category2, category3, category4, discount1, discount2, discount3, discount4, return1, return2, return3, return4, supplier1, supplier2, supplier3, supplier4, product_supplier1, product_supplier2, product_supplier3, product_supplier4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
