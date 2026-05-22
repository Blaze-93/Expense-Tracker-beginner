import os
import sys
from fastapi import FastAPI, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse
from sqlalchemy.orm import Session

# 1. Path setup
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 2. Local imports
from app.database import engine, Base, get_db
from app import models, crud
import pandas as pd

# 3. Initialize App
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 4. Create database tables
Base.metadata.create_all(bind=engine)

# --- ROUTES ---

@app.get("/")
def read_root(request: Request, view: str = "Monthly", db: Session = Depends(get_db)):
    # 1. Fetch all expenses for the history table
    expenses = crud.get_expenses(db)
    
    # 2. Get the specific math for the selected timeframe (Daily, Weekly, or Monthly)
    remaining, total_spent, budget_limit = crud.get_remaining_budget(db, timeframe=view)
    
    # 3. Render the page with the 'current_view' passed to the HTML
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "expenses": expenses,
            "remaining": remaining,
            "total_spent": total_spent,
            "budget_limit": budget_limit,
            "current_view": view  # This tells the HTML which button to highlight
        }
    )

@app.post("/add-expense/")
def add_expense(description: str = Form(...), amount: float = Form(...), db: Session = Depends(get_db)):
    crud.create_expense(db, description, amount)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete-expense/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    crud.delete_expense(db, expense_id)
    return RedirectResponse(url="/", status_code=303)

@app.post("/set-budget/")
def set_budget(amount: float = Form(...), limit_type: str = Form(...), db: Session = Depends(get_db)):
    crud.set_budget(db, amount, limit_type)
    return RedirectResponse(url="/", status_code=303)

@app.get("/export-csv/")
def export_csv(db: Session = Depends(get_db)):
    expenses = crud.get_expenses(db)
    data = [{"ID": e.id, "Description": e.description, "Amount": e.amount, "Date": e.timestamp} for e in expenses]
    df = pd.DataFrame(data)
    
    export_path = os.path.join(project_root, "data", "exports")
    if not os.path.exists(export_path):
        os.makedirs(export_path)
        
    file_full_path = os.path.join(export_path, "my_expenses.csv")
    df.to_csv(file_full_path, index=False)
    return FileResponse(file_full_path, filename="my_expenses.csv")