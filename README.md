# 🧩 Django CRM – Beginner Project

This is a beginner-friendly **Customer Relationship Management (CRM)** system built with [Django](https://www.djangoproject.com/) and [MySQL](https://www.mysql.com/). It includes basic **CRUD functionality** and **user authentication** features such as login, registration, and logout.

---

## ✨ Features

- 🔐 User registration, login & logout  
- ➕ Add new customer records  
- 📝 Update existing records  
- ❌ Delete records  
- 🔍 View detailed customer info  
- 🧭 Clean, simple UI using Django templates  

This project is ideal for learning how to:  
- Use Django models, views, and templates  
- Handle forms and user input  
- Implement authentication  
- Connect Django to a MySQL database  

---

## 💻 Technologies Used

- **Backend:** Python & Django  
- **Database:** MySQL  
- **Frontend:** HTML/CSS (via Django templates)  
- **Styling:** Bootstrap (optional)  

---

## ⚙️ Installation Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database

Make sure MySQL server is installed and running.

Create a new MySQL database and user:
```sql
CREATE DATABASE crm_db CHARACTER SET UTF8;
CREATE USER 'crm_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON crm_db.* TO 'crm_user'@'localhost';
FLUSH PRIVILEGES;
```

Update your Django project's `settings.py` with your database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm_db',
        'USER': 'crm_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/` to see the project in action.

---

## 📦 Requirements

Create a `requirements.txt` file with the following dependencies:
```
Django>=4.2,<5.0
mysqlclient>=2.1.0
python-decouple>=3.6
```
---

## 🛠️ Usage

1. **Register a new account** or **login** with existing credentials
2. **Add customers** using the "Add Customer" form
3. **View all customers** in the main dashboard
4. **Edit or delete** customer records as needed
5. **Access admin panel** at `/admin/` using superuser credentials

---

## 📋 Additional Notes

- Ensure you have MySQL development headers installed (e.g., `libmysqlclient-dev` on Ubuntu) to install the `mysqlclient` Python package
- Use environment variables or a `.env` file to keep sensitive data (like DB passwords) secure in production
- For styling, Bootstrap is optionally included but not required
- This setup is intended for local development. For production deployment, consider:
  - Configuring proper static files handling
  - Security settings (DEBUG=False, ALLOWED_HOSTS, etc.)
  - Database backups and optimization
  - Using a production WSGI server like Gunicorn

---

## 🚀 Future Enhancements

- [ ] Search and filter functionality
- [ ] Export customer data to CSV/Excel
- [ ] Email integration for customer communication
- [ ] Dashboard with analytics and charts
- [ ] REST API endpoints
- [ ] Role-based permissions

---

## 🙋‍♂️ Contributing

Feel free to fork this repo, submit issues, or open pull requests. This project is open for learning and improvement!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub or contact mc_chaker@esi.dz

