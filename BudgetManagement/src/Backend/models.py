from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Users", back_populates="categories")

class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Users", back_populates="budget")

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Users", back_populates="expenses")

Users.categories = relationship("Category", order_by=Category.id, back_populates="user")
Users.budget = relationship("Budget", uselist=False, back_populates="user")
Users.expenses = relationship("Expense", order_by=Expense.id, back_populates="user")
Category.expenses = relationship("Expense", order_by=Expense.id, back_populates="category")
