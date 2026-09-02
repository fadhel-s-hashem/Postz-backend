# Postz - Back-End API

This is the Django REST Framework API for **Postz**, a social post-sharing and category management application[cite: 2]. It handles JWT user authentication, post creation across categories, interactive commenting, and user dashboard filtering backed by a relational database[cite: 2].

## Front-End Repository

For full project documentation, UI screenshots, complete setup instructions, and feature details, please visit the primary repository:
[Postz Front-End](https://github.com/fadhel-s-hashem/Postz_frontend)

---

## Tech Stack

* **Language & Framework:** Python, Django, Django REST Framework (DRF)[cite: 2]
* **Authentication:** JSON Web Tokens (JWT) via SimpleJWT[cite: 2]
* **Database:** SQLite / PostgreSQL[cite: 2]

---

## Prerequisites

Before running this project locally, ensure you have the following installed:
* Python (v3.10 or higher
* `pip` and `virtualenv`

---

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/fadhel-s-hashem/Postz-backend
cd Postz-backend
```

### 2. Create and activate a virtual environment
**macOS:**
```bash
python3 -m venv .venv 
source .venv/bin/activate 
```

**Windows (Git Bash):**
```bash
python -m venv .venv 
source .venv/Scripts/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database migrations & Start server
```bash
python manage.py migrate
python manage.py runserver
```

---

For complete setup instructions, frontend integration, and full application details, please refer to the [Postz Front-End Repository](https://github.com/fadhel-s-hashem/Postz_frontend)
