# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 28, 2024 16:57:25
# Database: sqlite:////tmp/tmp.qoei0Rmt0w-01JDSV6CZ04DRE8CXWZ4W7BV5P/CRMDataSystem/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    """
    description: This table stores product categories.
    """
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductCategoryList : Mapped[List["ProductCategory"]] = relationship(back_populates="category")



class Customer(SAFRSBaseX, Base):
    """
    description: This table stores customer information.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    date_joined = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerContactList : Mapped[List["CustomerContact"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Product(SAFRSBaseX, Base):
    """
    description: This table stores product details that are available for sale.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    stock = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    DiscountList : Mapped[List["Discount"]] = relationship(back_populates="product")
    ProductCategoryList : Mapped[List["ProductCategory"]] = relationship(back_populates="product")
    ProductSupplierList : Mapped[List["ProductSupplier"]] = relationship(back_populates="product")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="product")



class SalesRep(SAFRSBaseX, Base):
    """
    description: This table stores information about sales representatives.
    """
    __tablename__ = 'sales_rep'
    _s_collection_name = 'SalesRep'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerContactList : Mapped[List["CustomerContact"]] = relationship(back_populates="sales_rep")



class Supplier(SAFRSBaseX, Base):
    """
    description: This table stores supplier information.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductSupplierList : Mapped[List["ProductSupplier"]] = relationship(back_populates="supplier")



class CustomerContact(SAFRSBaseX, Base):
    """
    description: This table records customer contacts and interactions.
    """
    __tablename__ = 'customer_contact'
    _s_collection_name = 'CustomerContact'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    sales_rep_id = Column(ForeignKey('sales_rep.id'))
    contact_date = Column(DateTime)
    notes = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("CustomerContactList"))
    sales_rep : Mapped["SalesRep"] = relationship(back_populates=("CustomerContactList"))

    # child relationships (access children)



class Discount(SAFRSBaseX, Base):
    """
    description: This table defines available discounts for products.
    """
    __tablename__ = 'discount'
    _s_collection_name = 'Discount'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    discount_amount = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("DiscountList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: This table records each order placed by a customer.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    date_placed = Column(DateTime)
    total_amount = Column(Integer)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class ProductCategory(SAFRSBaseX, Base):
    """
    description: This table maps products to categories.
    """
    __tablename__ = 'product_category'
    _s_collection_name = 'ProductCategory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    category_id = Column(ForeignKey('category.id'))

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("ProductCategoryList"))
    product : Mapped["Product"] = relationship(back_populates=("ProductCategoryList"))

    # child relationships (access children)



class ProductSupplier(SAFRSBaseX, Base):
    """
    description: This junction table maps products to suppliers.
    """
    __tablename__ = 'product_supplier'
    _s_collection_name = 'ProductSupplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    supplier_id = Column(ForeignKey('supplier.id'))

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ProductSupplierList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("ProductSupplierList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: This table captures the products in each order.
    """
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    product_id = Column(ForeignKey('product.id'))
    quantity = Column(Integer)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)
    ReturnList : Mapped[List["Return"]] = relationship(back_populates="order_item")



class Return(SAFRSBaseX, Base):
    """
    description: This table records product returns by customers.
    """
    __tablename__ = 'return'
    _s_collection_name = 'Return'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_item_id = Column(ForeignKey('order_item.id'))
    return_date = Column(DateTime)
    refund_amount = Column(Integer)

    # parent relationships (access parent)
    order_item : Mapped["OrderItem"] = relationship(back_populates=("ReturnList"))

    # child relationships (access children)
