# Database Versi RAM
# produk_db = []

# def reset_db():
#     global produk_db
#     # produk_db = []
#     produk_db.clear()  # clear isi list, bukan bikin list baru

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./toko.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Produk(Base):
    __tablename__ = "produk"
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, nullable=False)
    harga = Column(Integer, nullable=False)
    stok = Column(Integer, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

init_db()