# 💰 Personal Expense Tracker

A sleek, performance-focused personal finance web application built using **FastAPI**, **SQLAlchemy (SQLite)**, and **Bootstrap 5**. Designed specifically to manage tight budget limits (e.g., ₹8,000) with dynamic calculations across multiple timeframes.

## ✨ Features
* **Multi-Timeframe Filters:** Instantly toggle between **Daily**, **Weekly**, and **Monthly** overviews to track exactly where your budget goes.
* **Visual Budget Usage:** Dynamic progress bar that monitors spending percentage and automatically turns **Red** when you breach 90% of your limit.
* **Robust Local Database:** Data persists locally in a reliable SQLite configuration utilizing automated absolute-path directory generation.
* **One-Click CSV Export:** Seamlessly convert your entire database history into a clean Excel-ready `.csv` file.

---

## 🛠️ Tech Stack
* **Backend:** FastAPI (Python 3.11+)
* **Database & ORM:** SQLite + SQLAlchemy
* **Frontend Template:** Jinja2 + Bootstrap 5 (Dark Standard)
* **Data Processing:** Pandas (for CSV exporting)

---


## 📂 Project Directory Structure
```text
Expense Tracker/
│
├── app/
│   ├── __init__.py
│   ├── database.py    # Engine generation & absolute data paths
│   ├── models.py      # SQLAlchemy entities (Expense, Budget tables)
│   ├── crud.py        # Algorithmic calculation engines & time operations
│   └── main.py        # Absolute path injectors & FastAPI endpoints
│
├── templates/
│   └── index.html     # Dark mode Jinja2 UI layout
│
├── data/
│   ├── expenses.db    # Auto-generated SQLite data repository (Ignored in Git)
│   └── exports/       # Local CSV ledger generation point
│
├── .gitignore         # Prevents deployment of private data/binaries
├── requirements.txt   # Global software dependency manifesto
└── README.md          # Implementation and operational guide
```
---


## 🚀 Getting Started & Installation

Follow these steps to get the project up and running locally on your Windows machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/expense-tracker.git](https://github.com/YOUR_USERNAME/expense-tracker.git)
cd expense-tracker
```
--
### 2. Isolation & Deployment Setup

Execute this setup block inside your terminal from your project root path (`D:\Projects\Expense Tracker>`):

```powershell
# Create the isolated virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Install all the required packages from the manifesto
pip install -r requirements.txt
```
### 3. Running the Application

Once your virtual environment is active and dependencies are installed, use **Uvicorn** (the ASGI web server) to launch the FastAPI application.

#### Standard Mode (With Auto-Reload for Development)
Run this command from your project root folder. The `--reload` flag tells Uvicorn to watch your files and automatically restart the server whenever you save changes to your code or HTML:

```powershell
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
