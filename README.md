# Hasil Dari Pembelajaran QA Automation
![QA Automation](https://github.com/lpolpawd/QA_Automation_RESTAPI/actions/workflows/test.yml/badge.svg)
---

Project ini berfokus pada pembuatan REST API menggunakan framework FastApi, dan sqlite sebagai Database

## Tech Stack
- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- pytest
- GitHub Actions

## Cara Menjalankan Project ini dan QA Automation Test
**Kamu harus berada di root directory project**, lalu buat virtual environtment python, install requirements.txt menggunakan perintah `pip install -r requirements.txt` dan setelah itu bisa jalankan pytest menggunakan perintah `python3 -m pytest tests/ -v`. kalau mau mencoba manual bisa jalankan server uvicorn menggunakan perintah `uvicorn app.main_db:app --reload`