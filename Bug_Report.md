# Bug Report

---

ID            : BR-001
Judul         : Endpoint DELETE /produk/{id} mengembalikan status code yang salah
Tanggal       : 2026-07-02
Reporter      : (nama kamu)
Severity      : Medium
Status        : Open

## Deskripsi
Endpoint DELETE /produk/{id} mengembalikan status code 204 
padahal seharusnya 200.

## Langkah Reproduksi
1. Tambah produk via POST /produk dengan data valid
2. Kirim request DELETE /produk/0
3. Lihat status code response

## Hasil yang Diharapkan
Status code 200 dengan response {"pesan": "Produk berhasil dihapus"}

## Hasil Aktual
Status code 204, response body kosong

## Bukti
(paste output pytest yang failed di sini)

## Root Cause
status_code di decorator @app.delete diset ke 204 
seharusnya 200