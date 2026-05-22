from sqlalchemy.orm import Session
from app import models
from datetime import datetime, timedelta

# --- EXPENSE LOGIC ---

def get_expenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Expense).offset(skip).limit(limit).all()

def create_expense(db: Session, description: str, amount: float):
    db_expense = models.Expense(description=description, amount=amount)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if expense:
        db.delete(expense)
        db.commit()
    return expense

# --- BUDGET & CALCULATION LOGIC ---

def get_budget(db: Session):
    return db.query(models.Budget).first()

def set_budget(db: Session, amount: float, limit_type: str):
    db_budget = db.query(models.Budget).first()
    if db_budget:
        db_budget.amount = amount
        db_budget.limit_type = limit_type
    else:
        db_budget = models.Budget(amount=amount, limit_type=limit_type)
        db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def get_remaining_budget(db: Session, timeframe: str = "Monthly"):
    budget = get_budget(db)
    if not budget:
        return 0, 0, 0

    now = datetime.utcnow()
    
    # Logic to determine the "start date" based on timeframe
    if timeframe == "Daily":
        start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elif timeframe == "Weekly":
        # Get the start of the current week (Monday)
        start_date = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    else:  # Monthly (Default)
        start_date = datetime(now.year, now.month, 1)
    
    # Sum expenses from that start date onwards
    total_spent = db.query(models.Expense).filter(
        models.Expense.timestamp >= start_date
    ).with_entities(models.Expense.amount).all()
    
    sum_spent = sum([item[0] for item in total_spent])
    remaining = budget.amount - sum_spent
    
    return remaining, sum_spent, budget.amount