# SukaKasir Backend

REST API backend untuk **SukaKasir**, aplikasi kasir yang menyediakan pengelolaan data produk dan pencatatan transaksi. Repository ini berfokus pada penyediaan API serta integrasi database agar aplikasi client dapat berkomunikasi dengan data secara terstruktur.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
</p>

## Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Fitur Utama](#fitur-utama)
- [Teknologi](#teknologi)
- [Arsitektur](#arsitektur)
- [Menjalankan Proyek Secara Lokal](#menjalankan-proyek-secara-lokal)
- [Dokumentasi dan Endpoint](#dokumentasi-dan-endpoint)
- [Repository Terkait](#repository-terkait)

## Tentang Proyek

SukaKasir Backend merupakan layanan backend untuk mendukung kebutuhan pengelolaan data pada aplikasi kasir. Backend menyediakan endpoint untuk entitas seperti kategori, satuan, produk, pemasok, serta transaksi dan detail transaksi.

Proyek ini dibuat sebagai bagian dari pengembangan aplikasi SukaKasir sekaligus portofolio pengembangan backend. Fokus implementasinya meliputi perancangan REST API, pemisahan tanggung jawab antarbagian aplikasi, integrasi database relasional, validasi data, serta pengelolaan perubahan skema database.

## Fitur Utama

| Modul | Deskripsi |
|---|---|
| **Category Management** | Mengelola kategori untuk pengelompokan produk. |
| **Unit Management** | Mengelola satuan yang digunakan oleh produk. |
| **Product Management** | Menyediakan API untuk pengelolaan data produk. |
| **Supplier Management** | Mengelola data pemasok. |
| **Product–Supplier** | Mengelola relasi antara produk dan pemasok. |
| **Transaction Management** | Mengelola data transaksi. |
| **Transaction Items** | Menyimpan dan mengelola detail item yang terkait dengan transaksi. |
| **Transaction Types** | Mengelola tipe transaksi. |

## Teknologi

| Teknologi | Peran |
|---|---|
| [Python](https://www.python.org/) | Bahasa pemrograman backend. |
| [FastAPI](https://fastapi.tiangolo.com/) | Framework untuk membangun REST API. |
| [Pydantic](https://docs.pydantic.dev/) | Validasi dan struktur data request/response. |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM untuk berinteraksi dengan database. |
| [PostgreSQL](https://www.postgresql.org/) | Database relasional. |
| [Alembic](https://alembic.sqlalchemy.org/) | Migrasi skema database. |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server untuk menjalankan aplikasi FastAPI. |
| [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) | SDK Python yang tersedia untuk integrasi layanan penyimpanan berbasis S3. |

## Arsitektur

Secara umum, request dari frontend atau API client diteruskan ke router FastAPI, diproses menggunakan schema dan logika aplikasi, lalu berinteraksi dengan database melalui SQLAlchemy.

```text
Frontend / API Client
        |
        | HTTP Request
        v
   FastAPI Router
        |
        v
      Schema
        |
        v
     Service
        |
        v
     Repository
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

### Struktur Repository

```text
SukaKasir_backend/
├── alembic/          # Riwayat dan konfigurasi migrasi database
├── api/              # Router dan endpoint API
├── core/             # Konfigurasi serta komponen inti aplikasi
├── database/         # Koneksi database dan session
├── helper/           # Fungsi bantu yang digunakan aplikasi
├── models/           # Model/entitas database
├── repository/       # Lapisan akses data
├── schemas/          # Schema request dan response
├── service/          # Logika layanan aplikasi
├── .env.example      # Contoh variabel lingkungan
├── alembic.ini       # Konfigurasi Alembic
├── main.py           # Entry point aplikasi FastAPI
└── requirements.txt  # Daftar dependency Python
```

## Menjalankan Proyek Secara Lokal

### Prasyarat

Pastikan perangkat sudah memiliki:

- Python dan `pip`.
- PostgreSQL.
- Git.

### 1. Clone repository

```bash
git clone https://github.com/Fariz1703/SukaKasir_backend.git
cd SukaKasir_backend
```

### 2. Buat dan aktifkan virtual environment

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install dependency

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Siapkan database dan environment variables

Buat database PostgreSQL, misalnya:

```sql
CREATE DATABASE sukakasir;
```

Salin file contoh environment:

```bash
cp .env.example .env
```

Di Windows Command Prompt, gunakan `copy .env.example .env`. Selanjutnya, periksa dan sesuaikan isi `.env` dengan konfigurasi lokal. Contoh format variabel:

```env
DATABASE_URL=postgresql+psycopg://postgres:password_anda@localhost:5432/sukakasir
FILEBASE_ACCESS_KEY=access_key_anda
FILEBASE_SECRET_KEY=secret_key_anda
FILEBASE_BUCKET=gambar-produk
```

Sesuaikan username, password, host, port, nama database, serta kredensial penyimpanan dengan lingkungan Anda. Jangan commit file `.env` atau kredensial asli ke repository publik.

### 5. Jalankan migrasi database

```bash
alembic upgrade head
```

Perintah ini menerapkan migrasi Alembic yang tersedia ke database yang sudah dikonfigurasi.

### 6. Jalankan server development

```bash
uvicorn main:app --reload
```

Secara default, aplikasi dapat diakses di `http://127.0.0.1:8000`.

## Dokumentasi dan Endpoint

FastAPI menyediakan dokumentasi interaktif untuk melihat endpoint, schema, parameter, serta mencoba request dan response.

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Base URL deployment:** [https://suka-kasir-backend.vercel.app](https://suka-kasir-backend.vercel.app)

Beberapa endpoint pemeriksaan yang didefinisikan langsung pada aplikasi:

| Method | Path | Kegunaan |
|---|---|---|
| `GET` | `/` | Memeriksa apakah API berjalan. |
| `GET` | `/test-db` | Memeriksa koneksi database dengan query sederhana. |

Endpoint untuk modul kategori, satuan, produk, pemasok, dan transaksi dapat ditinjau melalui Swagger UI setelah server dijalankan. Path serta format payload spesifik tidak dicantumkan di sini agar tetap mengikuti implementasi aktual.

## Repository Terkait

- **Backend:** [Fariz1703/SukaKasir_backend](https://github.com/Fariz1703/SukaKasir_backend)
- **Aplikasi Android:** [LackFos/suka-kasir-mobile](https://github.com/LackFos/suka-kasir-mobile)
- **Deployment backend:** [suka-kasir-backend.vercel.app](https://suka-kasir-backend.vercel.app)


Dikembangkan sebagai backend untuk aplikasi SukaKasir dengan Python, FastAPI, dan PostgreSQL.
