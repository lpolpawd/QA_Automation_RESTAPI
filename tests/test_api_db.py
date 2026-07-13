import sqlite3

def test_produk_tersimpan_di_database(client):
    # Tambah produk via API
    client.post("/produk", json={"nama": "Jaket", "harga": 500_000, "stok": 7})
    
    # Verifikasi langsung ke database
    conn = sqlite3.connect("toko.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produk WHERE nama = 'Jaket'")
    hasil = cursor.fetchone()
    conn.close()
    
    assert hasil is not None
    assert hasil[1] == "Jaket"
    assert hasil[2] == 500_000
    assert hasil[3] == 7

def test_produk_terhapus_dari_database(client):
    # Tambah dulu
    client.post("/produk", json={"nama": "Topi", "harga": 100_000, "stok": 5})
    
    # Ambil id dari database
    conn = sqlite3.connect("toko.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM produk WHERE nama = 'Topi'")
    id_produk = cursor.fetchone()[0]
    conn.close()
    
    # Hapus via API
    client.delete(f"/produk/{id_produk}")
    
    # Verifikasi di database memang sudah terhapus
    conn = sqlite3.connect("toko.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produk WHERE nama = 'Topi'")
    hasil = cursor.fetchone()
    conn.close()
    
    assert hasil is None

def test_produk_terupdate_di_database(client):
    # Tambah dulu
    client.post("/produk", json={"nama": "Sandal", "harga": 80_000, "stok": 10})
    
    # Ambil id
    conn = sqlite3.connect("toko.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM produk WHERE nama = 'Sandal'")
    id_produk = cursor.fetchone()[0]
    conn.close()
    
    # Update via API
    client.put(f"/produk/{id_produk}", json={"nama": "Sandal Jepit", "harga": 50_000, "stok": 20})
    
    # Verifikasi perubahan di database
    conn = sqlite3.connect("toko.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produk WHERE id = ?", (id_produk,))
    hasil = cursor.fetchone()
    conn.close()
    
    assert hasil[1] == "Sandal Jepit"
    assert hasil[2] == 50_000
    assert hasil[3] == 20

def test_jumlah_produk_di_database(client):
    # Tambah 3 produk
    client.post("/produk", json={"nama": "Kaos", "harga": 75_000, "stok": 15})
    client.post("/produk", json={"nama": "Kemeja", "harga": 120_000, "stok": 8})
    client.post("/produk", json={"nama": "Rok", "harga": 90_000, "stok": 12})
    
    # Verifikasi jumlah di database
    conn = sqlite3.connect("toko.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM produk")
    jumlah = cursor.fetchone()[0]
    conn.close()
    
    assert jumlah == 3