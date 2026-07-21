# My QA Automation Project
![QA Automation](https://github.com/lpolpawd/QA_Automation_RESTAPI/actions/workflows/test.yml/badge.svg)
---

# English
---
## Summary
This project focuses on Testing a REST API using the FastApi as a backend framework, and sqlite as a database.Im using `pytest`, `pytest-playwright` to make the QA automation code, each of `tests/` file have different testing, and it functions according to the file names. **I use AAA formula to write this QA automation code**.

### 💡 Architecture Note: In-Memory Testing vs Real DB

This project provides two backend implementation variants for testing:
1. **SQLite Database Variant (`app/main_db.py`):** Used for full integration tests, including direct database verification via SQL queries.
2. **In-Memory RAM Variant (`main_ram.txt`):** An isolated, lightweight service using RAM-based data storage for ultra-fast API unit testing without database side effects. 

*Note: The RAM variant is stored as `.txt` to prevent Uvicorn CLI auto-discovery conflicts, ensuring clean application entry points when running `uvicorn app.main_db:app`.*

## Tech Stack
- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- pytest
- GitHub Actions

and after that you can run pytest using the command `python3 -m pytest tests/ -v`. If you want to try it manually, you can run the uvicorn server using the command `uvicorn app.main_db:app --reload`

## Test Structure

- `tests/test_api.py` — API endpoint tests using in-memory mock data
- `tests/test_api_db.py` — Integration tests verifying API responses directly against the SQLite database.
- `tests/test_browser.py` — E2E browser automation using Playwright

## Coverage

- CRUD API testing (GET, POST, PUT, DELETE)
- Data verification directly in a SQLite database
- Browser automation (form filling, navigation)
- Automated CI/CD via GitHub Actions

## 🚀 How to Run the Project

### 1. Prerequisites
Clone the repository and navigate to the project root directory:
```bash
git clone https://github.com/lpolpawd/QA_Automation_RESTAPI.git
cd QA_Automation_RESTAPI
```

### 2. Setup Virtual Environment & Install Dependencies
```Bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Automated Tests
Execute all test cases with verbose output:
```
Bash
python3 -m pytest tests/ -v
4. (Optional) Run Application Server Manually
If you want to test the endpoints manually via Swagger UI ([http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)):

Bash
uvicorn app.main_db:app --reload
```