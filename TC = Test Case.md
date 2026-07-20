# TC = Test Case

```contoh
ID : TC-001
Judul : Tambah produk dengan data valid
Precondition : Database kosong
Langkah : 1. Kirim POST /produk dengan nama, harga, stok yang valid
Ekspektasi : Status 201, response berisi data produk yang ditambahkan
Hasil Aktual : (diisi setelah test)
Status : Pass / Fail
```

---

ID : TC-001
Judul : Tambah produk dengan data valid
Precondition : Database kosong
Langkah : 1. Kirim POST /produk dengan nama, harga, stok yang valid
Ekspektasi : Status 201, response berisi data produk yang ditambahkan
Hasil Aktual : Status 201, response berisi data produk yang ditambahkan
Status : Pass

---

ID : TC-002
Judul : ambil semua produk saat database kosong
Precondition : Database kosong
Langkah : 1. Kirim GET /produk
Ekspektasi : Status 200, response berisi array kosong []
Hasil Aktual : Status 200, response berisi []
Status : Pass

---

ID : TC-003
Judul : ambil produk dengan ID
Precondition : Database kosong
Langkah : 1. Kirim POST /produk dengan data yang valid, 2. Kirim GET /produk/0
Ekspektasi : Status 200, response berisi data dengan id nomor 0
Hasil Aktual : Status 200, response berisi data dengan id nomor 0
Status : Pass

---

ID : TC-004
Judul : ambil produk dengan ID yang tidak ada
Precondition : Database Ada
Langkah : 1. Kirim GET /produk/99 (ID yang tidak ada di database)
Ekspektasi : Status 404, response not found
Hasil Aktual : Status 404, response not found
Status : Pass

ID            : TC-005
Judul         : Verifikasi produk tersimpan di database setelah POST
Precondition  : Database kosong
Langkah       : 1. Kirim POST /produk dengan data valid
                2. Query langsung ke database: SELECT * FROM produk WHERE nama = 'Jaket'
Ekspektasi    : Data ditemukan di database dengan nama, harga, stok yang sesuai
Hasil Aktual  : Data ditemukan di database
Status        : Pass

---

ID            : TC-006
Judul         : Verifikasi produk terhapus dari database setelah DELETE
Precondition  : Database berisi minimal 1 produk
Langkah       : 1. Kirim DELETE /produk/{id}
                2. Query langsung ke database: SELECT * FROM produk WHERE id = {id}
Ekspektasi    : Data tidak ditemukan di database (hasil query NULL)
Hasil Aktual  : Data tidak ditemukan di database
Status        : Pass
