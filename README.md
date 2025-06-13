# Flask-React Full Stack Application

Aplikasi Full Stack yang dibangun menggunakan Flask (Backend) dan React (Frontend) untuk manajemen kontak.

## Pengembang
**Nama:** Alvin Dio Prakosa  
**Role:** Full Stack Developer

## Teknologi yang Digunakan
- **Backend:**
  - Flask
  - SQLAlchemy
  - Flask-CORS
  - Python 3.x

- **Frontend:**
  - React
  - Vite
  - Modern JavaScript (ES6+)

## Fitur
- Manajemen Kontak (CRUD)
- RESTful API
- Responsive Design
- Modern UI/UX

## Cara Menjalankan Aplikasi

### Backend
1. Masuk ke direktori backend:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan server:
   ```bash
   python main.py
   ```

### Frontend
1. Masuk ke direktori frontend:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Jalankan development server:
   ```bash
   npm run dev
   ```

## API Endpoints
- GET /contacts - Mendapatkan semua kontak
- POST /create_contact - Membuat kontak baru
- PATCH /update_contact/<id> - Memperbarui kontak
- DELETE /delete_contact/<id> - Menghapus kontak

## Lisensi
MIT License
 
