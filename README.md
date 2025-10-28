# 🗂️ Welcome to TaskHub! 🚀🧠💻

**Demo:** [https://abdumalikxs.pythonanywhere.com/](https://abdumalikxs.pythonanywhere.com/)

---

## 💡 Inspiration

TaskHub was born from the need for a **simple yet powerful task management platform** that teams and individuals could use to organize projects efficiently.  
While many to-do apps exist, most fail to combine **collaboration**, and a **clean, responsive UI** — all within a lightweight Django framework.  
TaskHub bridges that gap by offering an intuitive dashboard that’s as functional as it is beautiful.

---
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 23 33 01" src="https://github.com/user-attachments/assets/8c7c23e3-c214-424f-91ec-823590421c71" />
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 23 34 15" src="https://github.com/user-attachments/assets/dbabb9a9-d43b-404a-ba03-3070e6656c09" />
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 23 34 37" src="https://github.com/user-attachments/assets/90481e45-176e-43e2-8acd-091790c7c93e" />
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 23 35 18" src="https://github.com/user-attachments/assets/41893987-3e4e-4c00-af8a-952bf8753363" />
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 23 39 08" src="https://github.com/user-attachments/assets/eb6d27d1-1397-4571-9599-73144f640adb" />


## ⚙️ What It Does

TaskHub is a **collaborative task manager** built with Django’s MTV architecture.  
It efficiently lets users create, edit, complete, and delete tasks while providing

### ✨ Core Functions

✅ **Full CRUD** for tasks and projects  
🔐 **User authentication system** — secure **login**, **logout**, and **session management**
🎨 **Tailwind CSS UI** for modern, responsive design  
📊 **Progress tracking** for better visualization of completed tasks  
💾 **SQLite backend** (easily switchable to PostgreSQL)  
🌐 **Deployed on PythonAnywhere** for real-time access anywhere

---

## 🏗️ How I Built It

TaskHub’s backend is powered by **Django** and follows the **MTV (Model–Template–View)** pattern.  
The frontend is built using Django’s template inheritance system with HTML, CSS, JavaScript, and Tailwind CSS for a clean, responsive interface, while routing and view logic are implemented through Django’s built-in URL dispatcher (urlpatterns) for smooth server-side rendering and navigation.

### 🧩 Stack Overview

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript, Tailwind CSS
- **Database:** SQLite3
- **Environment & Package Management:** Pipenv
- **Deployment:** PythonAnywhere

---

## 🚧 Challenges I Faced

🔧 Designing clean, reusable models and templates while maintaining readability.  
🗃️ Structuring URL routes and view logic to keep the project modular, maintainable, and ready for future API expansion.
🎨 Keeping the UI both responsive and minimal across devices.

---

## 🏆 Accomplishments I'm Proud Of

✨ Built a **fully functional task management system** from scratch using Django  
🔐 Implemented a **user login/logout system** using Django’s built-in authentication framework  
⚡ Optimized the UI with Tailwind CSS for a lightweight, modern experience  
☁️ Successfully **deployed** on PythonAnywhere for live demonstration

---

## 🔮 What’s Next for TaskHub

🔹 Expand AI assistance for automated task prioritization  
🔹 Integrate calendar and reminders  
🔹 Switch to PostgreSQL and Dockerize the deployment  
🔹 Release an open REST API for third-party integration

---

## 💻 Development Setup

### 🧰 Prerequisites

You’ll need:

- Python **3.12+**
- **Pipenv** (for managing virtual environments and dependencies)
- **Git** (to clone the project)
- **Tailwind CSS** _(optional — for UI customization)_

### ▶️ Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/abdumaliksx/taskhub.git
   cd taskhub
   ```

2. **Install dependencies using Pipenv**

   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**

   ```bash
   pipenv shell
   ```

4. **Run initial migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the local development server**

   ```bash
   python manage.py runserver
   ```

6. **Open the app in your browser**
   ```
   http://127.0.0.1:8000/
   ```

---

✅ **Notes**

- Make sure you have **Python 3.12+** and **Pipenv** installed before starting.
- To exit the Pipenv shell later, type:
  ```bash
  exit
  ```
- On Windows, use **PowerShell** or **Command Prompt** to run the same commands.
