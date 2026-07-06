# def test_fitur_saya(client):
    # 1. Arrange (Siapkan data)
    
    # 2. Act (Tembak fiturnya)
    
    # 3. Assert (Cek hasilnya)

def test_get_produk_kosong(client):
    response = client.get("/produk")
    assert response.status_code == 200
    assert response.json() == []

def test_tambah_produk(client):
    payload = {"nama": "Baju", "harga": 150_000, "stok": 10}
    response = client.post("/produk", json=payload)
    assert response.status_code == 201
    assert response.json()["harga"] == 150_000

def test_get_produk_by_id(client):
    client.post("/produk", json={"nama": "Sepatu", "harga": 300_000, "stok": 5})
    response = client.get("/produk/1")
    assert response.status_code == 200
    assert response.json()["nama"] == "Sepatu"

def test_get_produk_tidak_ditemukan(client):
    response = client.get("/produk/99")
    assert response.status_code == 404

def test_hapus_produk(client):
    client.post("/produk", json={"nama": "Celana", "harga": 200_000, "stok": 3})
    response = client.delete("/produk/1")
    assert response.status_code == 200

def test_hapus_produk_tidak_ditemukan(client):
    response = client.delete("/produk/99")
    
    assert response.status_code == 404

def test_update_produk_sukses(client):
    # Langkah 1: Masukkan data awal dulu (Sepatu, harga 300rb, stok 5)
    client.post("/produk", json={"nama": "Sepatu", "harga": 300_000, "stok": 5})
    
    # Langkah 2: Ubah data di ID 0 jadi "Sepatu Roda", harga naik jadi 450rb
    data_baru = {"nama": "Sepatu Roda", "harga": 450_000, "stok": 5}
    response = client.put("/produk/1", json=data_baru)
    
    # Langkah 3: Periksa hasilnya (Assert)
    assert response.status_code == 200
    assert response.json()["message"] == "Produk berhasil diubah!"
    
    # Langkah 4: Opsional tapi bagus, kita GET lagi ID buat mastiin di database-nya beneran berubah
    response_get = client.get("/produk/1")
    assert response_get.json()["nama"] == "Sepatu Roda"
    assert response_get.json()["harga"] == 450_000

def test_update_produk_gagal_id_tidak_ada(client):
    # Langkah 1: Langsung tembak PUT ke ID 99 tanpa isi data apa-apa dulu di database
    data_update = {"nama": "Baju Baru", "harga": 100_000, "stok": 10}
    response = client.put("/produk/99", json=data_update)
    
    # Langkah 2: Periksa apakah satpam 404 kita bekerja dengan baik
    assert response.status_code == 404
    assert "tidak ditemukan" in response.json()["detail"]

def test_update_produk_stok_berubah(client):
    client.post("/produk", json={"nama": "Baju", "harga": 100_000, "stok": 3})
    response = client.put("/produk/1", json={"nama": "Baju", "harga": 100_000, "stok": 10})
    assert response.status_code == 200
    response_get = client.get("/produk/1")
    assert response_get.json()["stok"] == 10

# tidak bisa, hapus by column
# def test_hapus_produk_by_column(client):
#     client.post("/produk/", json={"nama": "Baju Vintage", "harga": 700_000, "stok": 5})
#     response = client.delete("/produk/0", json={"nama": "Baju Vintage"})
#     assert response.status_code == 200
#     response_get = client.get("/produk/0")
#     assert response_get.json()["nama"] == "Baju Vintage"

# json disini berfungsi sebagai pembuat data, yang berjalan di RAM.
# params disini berfungsi sebagai query parameter, jadi params dipakai kalau query saja
def test_query_by_nama(client):
    client.post("/produk", json={"nama": "Baju Besar", "harga": 900_000, "stok": 3})
    response = client.get("/produk/cari", params={"nama" : "baju"})
    assert response.status_code == 200
    # Mastiin kalau data yang kembali adalah list dan isinya ada kata "Baju Besar"
    assert response.json()[0]["nama"] == "Baju Besar"

def test_query_kosong(client):
    response = client.get("/produk/cari")
    assert response.status_code == 422  # wajib isi nama, kalau kosong FastAPI tolak


def test_query_by_nama_tidak_lengkap(client):
    client.post("/produk/", json = {"nama": "Baju Besar", "harga": 900_000, "stok": 3})
    response = client.get("/produk/cari", params={"nama": "Besar"})
    assert response.status_code == 200
    assert response.json()[0]["nama"] == "Baju Besar"