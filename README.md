# My QA Automation Project
![QA Automation](https://github.com/lpolpawd/QA_Automation_RESTAPI/actions/workflows/test.yml/badge.svg)
---

This project focuses on Testing a REST API using the FastApi as a backend framework, and sqlite as a database.Im using `pytest`, `pytest-playwright` to make the QA automation code, each of `tests/` file have different testing, and it functions according to the file names. **I use AAA formula to write this QA automation code**. you may see file like `main_ram.txt` and it also functions according to the file names, i'm using ram as the database, the reason why i change the format to .txt because it can messed up uvicorn server

## Tech Stack
- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- pytest
- GitHub Actions

## How to Run this project | Cara Menjalankan Project ini dan QA Automation Test
First you must be in the root projecy directory and install all the requirements.txt file with python 
> pip install -r requirements.txt


and after that you can run pytest using the command `python3 -m pytest tests/ -v`. If you want to try it manually, you can run the uvicorn server using the command `uvicorn app.main_db:app --reload`

**Kamu harus berada di root directory project**, lalu buat virtual environtment python, install requirements.txt menggunakan perintah `pip install -r requirements.txt` dan setelah itu bisa jalankan pytest menggunakan perintah `python3 -m pytest tests/ -v`. kalau mau mencoba manual bisa jalankan server uvicorn menggunakan perintah `uvicorn app.main_db:app --reload`

## Struktur Test

- `tests/test_api.py` — API endpoint testing + RAM database
- `tests/test_api_db.py` — API endpoint testing + verifikasi database
- `tests/test_browser.py` — Browser automation testing pakai Playwright

## Coverage

- CRUD API testing (GET, POST, PUT, DELETE)
- Data verification directly in a SQLite database
- Browser automation (form filling, navigation)
- Automated CI/CD via GitHub Actions

## Yang Dicakup

- CRUD API testing (GET, POST, PUT, DELETE)
- Verifikasi data langsung ke SQLite database
- Browser automation (form filling, navigation)
- CI/CD otomatis via GitHub Actions