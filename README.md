# 📝 Flask Task Manager

<div align="center">

![Flask](https://img.shields.io/badge/Flask-3.0.0-blue?style=for-the-badge&logo=flask)
![Python](https://img.shields.io/badge/Python-3.12+-green?style=for-the-badge&logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1.1-red?style=for-the-badge)
![TailwindCSS](https://img.shields.io/badge/Tailwind-3.0-38B2AC?style=for-the-badge&logo=tailwind-css)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A beautiful and functional task management application built with Flask, SQLAlchemy, and Tailwind CSS.

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [Project Structure](#-project-structure)

</div>

---

## ✨ Features

- ➕ **Add Tasks** - Quickly create new tasks with a simple input field
- ✅ **Toggle Complete** - Mark tasks as done with a single click
- ✏️ **Edit Tasks** - Inline editing without page refresh
- 🗑️ **Delete Tasks** - Remove tasks with confirmation dialog
- 📊 **Statistics Dashboard** - View total, completed, and pending tasks at a glance
- 🎨 **Beautiful UI** - Modern gradient design with smooth animations
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- 💾 **Persistent Storage** - All data saved in SQLite database
- 🕒 **Timestamps** - Track when each task was created

---

## 🎬 Demo

### Main Interface
- Clean, intuitive design with gradient background
- Real-time task statistics
- Smooth hover effects and transitions

### Key Actions
- **Add:** Type your task and click the "Add" button
- **Complete:** Click the circle icon (turns green when done)
- **Edit:** Click the pencil icon, modify, and save
- **Delete:** Click the trash icon with confirmation

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ayushh9999/Flask-Task-Manager.git
cd Flask-Task-Manager
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open in Browser
Navigate to: **http://127.0.0.1:5000**

🎉 **That's it!** Your task manager is now running locally!

---

## 💻 Usage

### Adding a Task
1. Type your task in the input field
2. Click the **"Add"** button or press Enter
3. Your task appears in the list below

### Managing Tasks
| Action | How To |
|--------|--------|
| **Mark Complete** | Click the circle icon next to the task |
| **Edit Task** | Click the blue pencil icon, modify text, and save |
| **Delete Task** | Click the red trash icon and confirm |

### Understanding Statistics
- **Total Tasks:** All tasks in your list
- **Completed:** Tasks marked as done (green checkmark)
- **Pending:** Tasks still in progress

---

## 🛠️ Tech Stack

### Backend
- **[Flask](https://flask.palletsprojects.com/)** - Lightweight Python web framework
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)** - SQL toolkit and ORM
- **[SQLite](https://www.sqlite.org/)** - Embedded database

### Frontend
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[Font Awesome](https://fontawesome.com/)** - Icon library
- **[Jinja2](https://jinja.palletsprojects.com/)** - Templating engine

### Features
- ✅ RESTful routing
- ✅ ORM database operations
- ✅ Responsive design
- ✅ Form validation
- ✅ CRUD operations

---

## 📁 Project Structure

```
Flask-Task-Manager/
│
├── 📄 app.py                  # Main Flask application with routes
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md              # Project documentation (you're here!)
├── 📄 .gitignore             # Git ignore file
│
├── 📁 templates/
│   └── 📄 index.html         # Main HTML template with Tailwind CSS
│
├── 📁 instance/
│   └── 📄 todo.db            # SQLite database (auto-generated)
│
└── 📁 .venv/                 # Virtual environment (not in repo)
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Flask application, routes, and database models |
| `index.html` | Frontend UI with Tailwind CSS styling |
| `requirements.txt` | List of Python packages needed |
| `todo.db` | SQLite database storing all tasks |

---

## 🎯 API Routes

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Display all todos |
| `POST` | `/add` | Create a new todo |
| `GET` | `/toggle/<id>` | Toggle todo completion status |
| `GET` | `/delete/<id>` | Delete a todo |
| `POST` | `/edit/<id>` | Update todo title |

---

## 🗄️ Database Schema

### Todo Model
```python
class Todo(db.Model):
    id          # Integer, Primary Key
    title       # String(200), Required
    completed   # Boolean, Default: False
    created_at  # DateTime, Auto-set
```

---

## 🎨 Customization

### Change Colors
Edit `index.html` and modify Tailwind classes:
```html
<!-- Primary color (blue/indigo) -->
<button class="bg-indigo-600 hover:bg-indigo-700">

<!-- Change to purple -->
<button class="bg-purple-600 hover:bg-purple-700">
```

### Modify Database
Edit the `Todo` model in `app.py`:
```python
class Todo(db.Model):
    # Add new fields here
    priority = db.Column(db.String(20), default='medium')
    due_date = db.Column(db.DateTime)
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use different port
```

### Database Issues
```bash
# Delete and recreate database
rm instance/todo.db
python app.py  # Database will be auto-created
```

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

---

## 📝 License

This project is licensed under the MIT License - feel free to use it for your own projects!

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/ayushh9999/Flask-Task-Manager/issues).

### How to Contribute
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Ayush Mondal**

- GitHub: [@ayushh9999](https://github.com/ayushh9999)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/ayush-mondal)

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

## 📸 Screenshots

### Main Interface
> Add your screenshot here

### Mobile View
> Add your mobile screenshot here

---

<div align="center">

**Made with ❤️ and Python**

**[⬆ Back to Top](#-flask-task-manager)**

</div>
