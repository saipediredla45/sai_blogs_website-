# 📝 Blogs Website (Django + MySQL)

A full-stack **Blogs Website** built using **Django**, **HTML**, **CSS**, and **JavaScript**, with **MySQL** as the database.  
This project demonstrates backend–frontend integration and database-driven dynamic content rendering.

---

## 🚀 Features

- Blog post creation and management
- Admin panel for content control
- Dynamic content from MySQL database
- Django template-based frontend
- Responsive UI using HTML & CSS
- Image upload support
- Clean and maintainable project structure

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript (DOM concepts)

### Backend
- Python
- Django Framework

### Database
- **MySQL**

### Tools
- Git & GitHub
- VS Code

---
blogs-website/
│
├── blog/ # Blog application
├── templates/ # HTML templates
├── static/ # CSS, JS, images
├── media/ # Uploaded blog images
├── manage.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure MySQL Database

Install MySQL and create a database:

CREATE DATABASE blog_db;


Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


Install MySQL client:

pip install mysqlclient

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create Superuser
python manage.py createsuperuser

7️⃣ Run Development Server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

🔐 Admin Panel

Access the admin panel:

http://127.0.0.1:8000/admin/


Use superuser credentials to manage blogs.

🌱 Future Enhancements

User authentication (login/signup)

Comment and like system

Category & tag filters

REST API with Django REST Framework

Deployment on cloud platforms

👤 Author

Sai Pediredla
Aspiring Python Full Stack Developer

Skills:
Python | Django | MySQL | HTML | CSS | JavaScript

📧 Email: saipediredla85@gmail.com

🌐 GitHub: https://github.com/your-username

📄 License

This project is developed for learning and educational purposes.


---

### ✅ Next Steps (Optional)
I can also help you:
- Add **screenshots section**
- Add **Live Demo link**
- Create **requirements.txt**
- Prepare **deployment README** (Railway / Render / PythonAnywhere)

Just tell me 👍

## 📂 Project Structure

