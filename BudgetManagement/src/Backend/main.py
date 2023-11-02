from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List, Annotated
from models import Users, Category, Expense, Budget
from database import engine, SessionLocal 
from sqlalchemy.orm import Session
import auth
from auth import get_current_user
import models
from fastapi.responses import RedirectResponse



app = FastAPI()
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


class QuestionBase(BaseModel):
    question_text: str 
    choices: List[ChoiceBase]


class CategoryBase(BaseModel):
    name: str


class ExpenseBase(BaseModel):
    amount: float
    category_id: int

class BudgetBase(BaseModel):
    amount: float

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated [dict, Depends (get_current_user)]







# CRUD operations

def get_user_by_username(username: str, db):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if user:
        return {"id": user.id, "username": user.username}
    return None



def create_user(db, username: str, password: str):
    db_user = Users(username=username, hashed_password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_category(db, user_id: int, name: str):
    db_category = Category(name=name, user_id=user_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db, user_id: int):
    return db.query(Category).filter(Category.user_id == user_id).all()


def create_budget(db, user_id: int, amount: float):
    db_budget = Budget(amount=amount, user_id=user_id)  # Update 'user_id' to 'users_id'
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget


def get_budget(db, user_id: int):
    return db.query(Budget).filter(Budget.user_id == user_id).first()


def create_expense(db, user_id: int, category_id: int, amount: float):
    db_expense = Expense(amount=amount, user_id=user_id, category_id=category_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


def get_expenses(db, user_id: int):
    return db.query(Expense).filter(Expense.user_id == user_id).all()

def get_db():
    db = SessionLocal ()
    try:
        yield db 
    finally:
        db.close()



db_dependency = Annotated [Session, Depends (get_db)]







@app.post("/categories")
async def create_category_route(name: str, current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    if current_user:
        category = create_category(db, current_user["id"], name)
        return {"name": category.name, "user_id": category.user_id}
    else:
        raise HTTPException(status_code=401, detail="User not found")

# Endpoint pour récupérer le nom de toutes les catégories
@app.get("/categories")
async def get_categories(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Assurez-vous que 'id' est présent dans le dictionnaire 'current_user'
    if 'id' not in current_user:
        raise HTTPException(status_code=401, detail="User ID not found")

    user_id = current_user['id']
    categories = db.query(Category).filter(Category.user_id == user_id).all()
    return [{"id": category.id, "name": category.name} for category in categories]





@app.post("/budget")
async def create_budget_route(amount: float, current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    if current_user:
        budget = create_budget(db, current_user["id"], amount)
        return {"amount": budget.amount, "user_id": budget.user_id}
    else:
        raise HTTPException(status_code=401, detail="User not found")

@app.get("/budget")
async def get_budget_route(current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    if current_user:
        budget = get_budget(db, current_user["id"])
        return {"amount": budget.amount, "user_id": budget.user_id}
    else:
        raise HTTPException(status_code=401, detail="User not found")


# Endpoint pour créer une dépense ou dépenser de l'argent
@app.post("/expenses")
async def create_or_spend_money(amount: float, is_spending: bool = False, category_name: str = "Default", current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user:
        # Vérifier si l'utilisateur a un budget
        budget = get_budget(db, current_user["id"])
        if not budget:
            raise HTTPException(status_code=404, detail="Budget not found for the current user.")

        # Vérifier si le montant dépensé ne dépasse pas le budget
        if is_spending and amount > budget.amount:
            raise HTTPException(status_code=400, detail="Amount spent exceeds the budget.")

        # Récupérer l'ID de la catégorie en fonction du nom
        category = db.query(Category).filter(Category.name == category_name, Category.user_id == current_user['id']).first()
        if not category:
            raise HTTPException(status_code=404, detail=f"Category '{category_name}' not found for the current user.")

        if is_spending:
            # Dépenser de l'argent
            expense = Expense(amount=amount, category_id=category.id, user_id=current_user['id'])
            db.add(expense)
            db.commit()
            db.refresh(expense)

            # Mettre à jour le budget
            budget.amount -= amount
            db.commit()
            db.refresh(budget)

            return {"message": "Expense created and budget updated successfully.", "expense_id": expense.id}
        else:
            # Créer une dépense sans dépenser de l'argent
            expense = Expense(amount=amount, category_id=category.id, user_id=current_user['id'])
            db.add(expense)
            db.commit()
            db.refresh(expense)

            return {"message": "Expense created successfully.", "expense_id": expense.id}
    else:
        raise HTTPException(status_code=401, detail="User not found")



    
# Endpoint pour récupérer toutes les dépenses de l'utilisateur connecté
@app.get("/expenses/")
async def get_expenses(current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    expenses = db.query(Expense).filter(Expense.user_id == current_user.id).all()
    return expenses







@app.get("/", status_code=status.HTTP_200_OK) 
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return {"User": user}








@app.post("/questions/")
async def create_questions(question: QuestionBase, db: db_dependency):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = models.Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id
        )
        db.add(db_choice)
    db.commit()
