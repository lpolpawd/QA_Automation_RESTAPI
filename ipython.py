import sqlite3
conn = sqlite3.connect("toko.db")
cursor = conn.cursor()

# 1. Ambil semua produk
cursor.execute("SELECT * FROM produk")
print(cursor.fetchall())

# 2. Cari produk tertentu
cursor.execute("SELECT * FROM produk WHERE nama = 'Baju'")
print(cursor.fetchall())

# 3. Cari produk dengan harga di atas 200000
cursor.execute("SELECT * FROM produk WHERE harga > 200000")
print(cursor.fetchall())

# 4. Cari produk yang namanya mengandung kata 'Baju'
cursor.execute("SELECT * FROM produk WHERE nama LIKE '%Baju%'")
print(cursor.fetchall())

# 5. Urutkan produk dari harga termurah
cursor.execute("SELECT * FROM produk ORDER BY harga ASC")
print(cursor.fetchall())

# 6. Hitung total produk
cursor.execute("SELECT COUNT(*) FROM produk")
print(cursor.fetchall())

# 7. Hitung total nilai stok semua produk
cursor.execute("SELECT SUM(harga * stok) FROM produk")
print(cursor.fetchall())