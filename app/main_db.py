from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db, init_db, Produk as ProdukModel

app = FastAPI()

class ProdukSchema(BaseModel):
    nama: str
    harga: int
    stok: int

@app.get("/produk")
def get_semua_produk(db: Session = Depends(get_db)):
    return db.query(ProdukModel).all()

@app.get("/produk/cari")
def cari_produk(nama: str, db: Session = Depends(get_db)):
    hasil = db.query(ProdukModel).filter(
        ProdukModel.nama.ilike(f"%{nama}%")
    ).all()
    if not hasil:
        raise HTTPException(status_code=404, detail=f"Produk '{nama}' tidak ditemukan")
    return hasil

@app.get("/produk/{id}")
def get_produk(id: int, db: Session = Depends(get_db)):
    produk = db.query(ProdukModel).filter(ProdukModel.id == id).first()
    if not produk:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
    return produk

@app.post("/produk", status_code=201)
def tambah_produk(produk: ProdukSchema, db: Session = Depends(get_db)):
    db_produk = ProdukModel(**produk.model_dump())
    db.add(db_produk)
    db.commit()
    db.refresh(db_produk)
    return db_produk

@app.put("/produk/{id}")
def update_produk(id: int, produk: ProdukSchema, db: Session = Depends(get_db)):
    db_produk = db.query(ProdukModel).filter(ProdukModel.id == id).first()
    if not db_produk:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
    for key, value in produk.model_dump().items():
        setattr(db_produk, key, value)
    db.commit()
    db.refresh(db_produk)
    return {"message": "Produk berhasil diubah!"}

@app.delete("/produk/{id}", status_code=200)
def hapus_produk(id: int, db: Session = Depends(get_db)):
    db_produk = db.query(ProdukModel).filter(ProdukModel.id == id).first()
    if not db_produk:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
    db.delete(db_produk)
    db.commit()
    return {"pesan": "Produk berhasil dihapus"}