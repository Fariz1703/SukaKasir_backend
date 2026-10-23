# SukaKasir Backend

**Backend REST API for SukaKasir — A Cashier and Transaction Management System**

SukaKasir Backend adalah layanan backend yang dikembangkan untuk mendukung aplikasi kasir SukaKasir. Proyek ini menyediakan API untuk mengelola data yang dibutuhkan dalam operasional sistem kasir, mulai dari produk, kategori, satuan, pemasok, hingga transaksi dan detail transaksi.

Backend ini dibangun menggunakan **Python, FastAPI, SQLAlchemy, dan PostgreSQL**, dengan Alembic untuk mengelola migrasi database.

Repository ini berfokus pada pengelolaan data dan penyediaan API yang dapat digunakan oleh frontend untuk berkomunikasi dengan database melalui backend.

Untuk versi android silakan mengunjungi link berikut https://github.com/LackFos/suka-kasir-mobile.git

## 🎯 Project Goals

Tujuan utama proyek ini adalah membangun backend yang terstruktur untuk mendukung proses pengelolaan data pada aplikasi kasir.

Beberapa tujuan pengembangannya meliputi:

- Menyediakan REST API untuk mengakses dan mengelola data aplikasi.
- Memisahkan logika backend dari antarmuka pengguna.
- Mengorganisasi model database, validasi data, dan endpoint API ke dalam struktur proyek yang terpisah.
- Mengelola relasi antarentitas seperti produk, kategori, satuan, pemasok, dan transaksi.
- Mempermudah pengembangan dan pemeliharaan aplikasi melalui penggunaan ORM dan database migration.

## ✨ Features

### 1. Category Management

Mengelola data kategori yang digunakan untuk mengelompokkan produk agar data produk lebih terorganisasi.

### 2. Unit Management

Mengelola satuan produk yang digunakan dalam pencatatan dan pengelolaan barang.

### 3. Product Management

Menyediakan modul pengelolaan data produk sebagai bagian utama dari sistem kasir.

### 4. Supplier Management

Mengelola data pemasok yang berkaitan dengan kebutuhan pendataan produk.

### 5. Product-Supplier Relationship

Menyediakan modul untuk mengelola hubungan antara produk dan pemasok.

### 6. Transaction Management

Mengelola data transaksi sebagai bagian dari proses pencatatan aktivitas penjualan atau transaksi pada sistem kasir.

### 7. Transaction Item Management

Mengelola detail item yang terkait dengan suatu transaksi, sehingga data transaksi dan item-itemnya dapat direpresentasikan secara terpisah.

### 8. Transaction Type Management

Mengelola tipe transaksi untuk mendukung pengelompokan transaksi berdasarkan jenisnya.

### 9. Database Integration

Menggunakan PostgreSQL sebagai database dan SQLAlchemy sebagai ORM untuk menghubungkan model aplikasi dengan data yang tersimpan.

### 10. Database Migration

Menggunakan Alembic untuk mengelola perubahan skema database secara terstruktur.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Bahasa pemrograman backend |
| FastAPI | Framework REST API |
| SQLAlchemy | Object-Relational Mapping (ORM) |
| PostgreSQL | Relational database |
| Alembic | Database schema migration |
| Pydantic | Validasi dan struktur data API |
| Uvicorn | ASGI server |

## 🏗️ Project Architecture

Proyek ini mengorganisasi kode ke dalam beberapa direktori berdasarkan tanggung jawabnya.

```text
SukaKasir_backend/
├── api/
│   ├── category.py
│   ├── unit.py
│   ├── product.py
│   ├── supplier.py
│   ├── productSupplier.py
│   ├── transaction.py
│   ├── transactionItem.py
│   └── transactionType.py
├── core/
├── database/
├── models/
├── schemas/
├── service/
├── alembic/
├── main.py
├── alembic.ini
└── requirements.txt
```

**Penjelasan direktori:**

- `api/` — modul router dan endpoint yang menangani request API.
- `core/` — konfigurasi inti dan komponen pendukung aplikasi.
- `database/` — komponen koneksi database dan pengelolaan session.
- `models/` — representasi entitas dan struktur data database.
- `schemas/` — schema untuk validasi dan representasi data API.
- `service/` — tempat untuk logika layanan aplikasi.
- `alembic/` — riwayat dan konfigurasi migrasi database.
- `main.py` — entry point aplikasi FastAPI.
- `requirements.txt` — daftar dependency Python.

Pemisahan ini membantu menjaga agar endpoint, struktur data, dan akses database tidak tercampur dalam satu file besar.

## 🔄 How It Works

Secara umum, alur komunikasi backend dapat digambarkan sebagai berikut:

```text
Frontend / API Client
        |
        | HTTP Request
        v
   FastAPI Router
        |
        v
 Validation & Schema
        |
        v
 Service / Application Logic
        |
        v
 SQLAlchemy ORM
        |
        v
   PostgreSQL
        |
        v
 HTTP Response
```

Frontend atau API client mengirimkan request HTTP ke endpoint yang tersedia. FastAPI menangani routing, schema digunakan untuk memvalidasi atau merepresentasikan data, dan komponen akses database digunakan untuk berinteraksi dengan PostgreSQL.

Respons kemudian dikirimkan kembali kepada client dalam format yang sesuai dengan implementasi endpoint.

Diagram tersebut menggambarkan alur konseptual; detail pemanggilan service dan validasi dapat berbeda pada setiap modul.

## 🚀 Getting Started

### Prerequisites

Pastikan perangkat sudah memiliki:

- Python
- pip
- PostgreSQL
- Git

### 1. Clone Repository

```bash
git clone https://github.com/Fariz1703/SukaKasir_backend.git

cd SukaKasir_backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Aktifkan environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Buat database PostgreSQL untuk aplikasi.

```sql
CREATE DATABASE sukakasir;
```

Sesuaikan konfigurasi koneksi database dengan mekanisme yang digunakan di dalam proyek, termasuk host, port, nama database, username, dan password.

Periksa konfigurasi pada direktori `database/`, `core/`, serta `alembic.ini` sebelum melanjutkan.

### 5. Run Database Migrations

Jika konfigurasi database dan Alembic telah siap, jalankan:

```bash
alembic upgrade head
```

Perintah ini menerapkan migrasi yang tersedia pada database.

### 6. Start the Development Server

```bash
uvicorn main:app --reload
```

Setelah server berjalan, buka dokumentasi API melalui:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Dokumentasi interaktif ini dapat digunakan untuk melihat endpoint yang terdaftar, memeriksa schema request dan response, serta mencoba API yang tersedia.

## 🌐 API Overview

API dikelompokkan berdasarkan entitas yang dikelola.

| Module | Description |
|---|---|
| Category | Pengelolaan kategori |
| Unit | Pengelolaan satuan |
| Product | Pengelolaan produk |
| Supplier | Pengelolaan pemasok |
| Product Supplier | Relasi produk dan pemasok |
| Transaction | Pengelolaan transaksi |
| Transaction Item | Detail item transaksi |
| Transaction Type | Pengelolaan tipe transaksi |

Daftar path endpoint, HTTP method, parameter, dan format respons dapat dilihat pada dokumentasi Swagger setelah aplikasi dijalankan.

## 🧪 Testing

Repository menyediakan file pengujian untuk beberapa bagian aplikasi, termasuk konfigurasi, koneksi database, model, dan session.

Untuk menjalankan pengujian menggunakan pytest, jika sudah dikonfigurasi sebagai test suite:

```bash
pytest
```

Pastikan dependency testing dan konfigurasi database yang diperlukan sudah tersedia.

## 🔗 Project Links

- **GitHub Repository:** https://github.com/Fariz1703/SukaKasir_backend
- **Deployment:** https://suka-kasir-backend.vercel.app

URL deployment dicantumkan sebagai referensi proyek. Ketersediaan endpoint dan status deployment dapat berubah.

## 📌 Project Scope

Repository ini berfokus pada pengembangan backend API dan integrasi database untuk aplikasi SukaKasir.

README ini mendokumentasikan modul yang terlihat pada struktur repository. Fitur tambahan seperti autentikasi, otorisasi berbasis role, pelaporan, atau mekanisme pengurangan stok otomatis tidak dianggap tersedia kecuali telah diimplementasikan dan dapat diverifikasi pada kode sumber.

---

*Built with Python and FastAPI to support the data management needs of the SukaKasir application.*
