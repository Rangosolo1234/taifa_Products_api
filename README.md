# 📦 Vue + Django Product Listing Web App

## 📌 Overview
This project is a **Product Listing Web Application** built using **Vue.js (frontend)** and **Django REST Framework (backend)**. The application fetches products from a Django API and displays them in a beautifully designed interface, showcasing images, names, descriptions, and prices.

## 🚀 Technologies Used

### Frontend:
- **Vue 3** (Composition API)
- **Tailwind CSS** (for styling)
- **Fetch API** (to call Django REST API)

### Backend:
- **Django** (as the backend framework)
- **Django REST Framework (DRF)** (for building APIs)
- **SQLite** (default database for development)
- **CORS Headers** (for frontend-backend communication)

---

## 🛠️ Installation & Setup

### 1️⃣ Backend Setup (Django)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/vue-django-product-app.git
   cd vue-django-product-app
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate  # For Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (optional, for Django admin):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Start the server:**
   ```bash
   python manage.py runserver
   ```

---

### 2️⃣ Frontend Setup (Vue.js)

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Run the development server:**
   ```bash
   npm run dev
   ```

---

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/products/` | Fetch all products |
| POST | `/api/products/` | Add a new product |
| GET | `/api/products/{id}/` | Fetch a single product |
| PUT | `/api/products/{id}/` | Update a product |
| DELETE | `/api/products/{id}/` | Delete a product |

---

## 🎨 UI Design & Features

### 🏆 **Home Page (Product List)**
✅ Displays products in a responsive grid layout  
✅ Shows product **name, description, price, and image**  
✅ Uses Tailwind CSS for modern styling  

![Product List Screenshot](screenshots/product-list.png)

### 🔎 **Fetching API Data**
The application uses Vue's `fetch` API to retrieve product data from the backend dynamically.

---

## 🛠️ Troubleshooting

### ❓ Product Images Not Showing
- Ensure **`settings.py`** has:
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
- Ensure **`urls.py`** includes:
  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```
- Modify Vue image binding:
  ```vue
  <img :src="getImageUrl(item.image)" class="w-full h-40 object-cover rounded-md">
  ```

### ❓ CORS Issues
- Install Django CORS headers:
  ```bash
  pip install django-cors-headers
  ```
- Add to **settings.py**:
  ```python
  INSTALLED_APPS += ['corsheaders']
  MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware']
  CORS_ALLOW_ALL_ORIGINS = True
  ```

---

## 👏 Contributions
Pull requests are welcome! Please create an issue before submitting major changes.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

🚀 **Enjoy Coding!** 🎉

