# tmmin_vision_invoice_digital

# Cara Menjalankan Program Python di Windows

Dokumentasi ini menjelaskan langkah-langkah untuk menjalankan program Python di Windows. Program ini akan membaca data dari file CSV, mengenkripsi data menggunakan algoritma AES, dan menghasilkan QR code dari data terenkripsi dengan nama file yang dinamis berdasarkan data CSV.

## Prasyarat

Pastikan Anda sudah memiliki:
- Sistem operasi Windows.
- Akses ke Command Prompt.
- Akses ke internet untuk mengunduh Python dan pustaka yang diperlukan.

## Langkah 1: Instalasi Python

1. **Unduh Python**:
   - Kunjungi situs resmi Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Unduh versi terbaru dari Python dan pilih versi yang sesuai dengan sistem operasi Windows Anda.

2. **Instal Python**:
   - Jalankan file instalasi yang sudah diunduh.
   - Pastikan untuk mencentang opsi **"Add Python to PATH"** agar Python dapat diakses dari Command Prompt.
   - Klik **"Install Now"** dan ikuti instruksi hingga instalasi selesai.

3. **Verifikasi Instalasi**:
   - Setelah instalasi selesai, buka **Command Prompt** dengan menekan `Windows + R`, ketik `cmd`, lalu tekan `Enter`.
   - Di dalam Command Prompt, ketik perintah berikut untuk memeriksa apakah Python sudah terinstal:
     ```bash
     python --version
     ```
   - Jika Python sudah terinstal dengan benar, Anda akan melihat versi Python yang terpasang.

## Langkah 2: Instalasi Pustaka (Library) yang Dibutuhkan

Program ini membutuhkan beberapa pustaka tambahan yang harus diinstal. Anda dapat menginstalnya dengan menggunakan **pip**, manajer paket Python.

1. **Buka Command Prompt**:
   - Ketik `cmd` di kolom pencarian Windows dan tekan Enter untuk membuka Command Prompt.

2. **Instal pustaka-pustaka yang dibutuhkan**:
   - Jalankan perintah berikut satu per satu untuk menginstal pustaka yang diperlukan:
     ```bash
     pip install cryptography
     pip install qrcode[pil]
     pip install pillow
     ```

## Langkah 3: Menyiapkan Program Python

1. **Buat File Program Python**:
   - Buat sebuah file Python baru bernama `tmmin.py` dan salin kode berikut ke dalam file tersebut:

     ```python
     # Program Python yang sudah diberikan sebelumnya
     ```

2. **Buat File Konfigurasi (config.json)**:
   - Buat sebuah file bernama `config.json` dengan isi berikut:
     ```json
     {
       "encryption_key": "VISION4000007301"
     }
     ```

3. **Buat File CSV (data.csv)**:
   - Buat file CSV dengan satu baris data seperti ini:
     ```
     VISION|52401845|27501000.00|30526110.00|3025110.00|0100072463479302
     ```

## Langkah 4: Menjalankan Program

1. **Buka Command Prompt**:
   - Navigasikan ke direktori tempat Anda menyimpan file Python, `config.json`, dan `data.csv`. Gunakan perintah `cd` untuk berpindah ke direktori tersebut:
     ```bash
     cd C:\Users\NamaAnda\Documents\PythonProject
     ```

2. **Jalankan Program**:
   - Setelah berada di direktori yang benar, jalankan program dengan perintah berikut:
     ```bash
     python tmmin.py
     ```

3. **Hasil Program**:
   - Program akan melakukan beberapa hal:
     - Membaca data dari `data.csv`.
     - Mengenkripsi data menggunakan algoritma AES-CBC dengan kunci dari `config.json`.
     - Menghasilkan pesan terenkripsi dalam format Base64 dan mencetaknya di Command Prompt.
     - Membuat QR code dari pesan terenkripsi dan menyimpannya sebagai file gambar dengan nama dinamis berdasarkan bagian kedua dari data CSV (misalnya: `QR_52401845.png`).

## Langkah 5: Verifikasi Hasil

1. **Pesan Terenkripsi**:
   - Setelah program selesai, Anda akan melihat pesan terenkripsi di Command Prompt dalam format Base64.

2. **QR Code**:
   - Program akan menghasilkan file QR code dengan nama yang dinamis berdasarkan data dari CSV. File ini akan disimpan di direktori yang sama dengan program Python. Contoh: `QR_52401845.png`.

3. **Memeriksa QR Code**:
   - Anda dapat membuka file gambar QR code ini untuk memeriksa bahwa data terenkripsi telah diubah menjadi QR code.

## Troubleshooting

Jika Anda menghadapi masalah saat menjalankan program, berikut adalah beberapa hal yang bisa diperiksa:
1. Pastikan semua pustaka sudah diinstal dengan benar menggunakan `pip`.
2. Periksa apakah Python sudah ditambahkan ke PATH jika muncul pesan bahwa Python tidak dikenali sebagai perintah.
3. Pastikan semua file (`tmmin.py`, `config.json`, dan `data.csv`) berada di direktori yang sama.

Jika ada masalah lain, pastikan Anda menjalankan perintah di direktori yang benar dan semua file yang diperlukan sudah tersedia.

