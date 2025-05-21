### Hexlet tests and linter status:
[![Actions Status](https://github.com/Mirroel-Alvares/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Mirroel-Alvares/python-project-52/actions)


[![test-check](https://github.com/Mirroel-Alvares/python-project-52/actions/workflows/test-check.yml/badge.svg)](https://github.com/Mirroel-Alvares/python-project-52/actions/workflows/test-check.yml)

Maintainability and Test Coverage status:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Mirroel-Alvares_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Mirroel-Alvares_python-project-52)


### Access to the deployed application
[You can see the web-service in action at Render] (https://python-project-52-svod.onrender.com)

---

# Task Manager

**Task Manager**  is a simple web application that helps users manage their tasks.

---

###  Local Run
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Mirroel-Alvares/python-project-52.git
   cd python-project-52
   ```
2. **Install dependencies**:
   ```sh
   make install
   ```
3. **Set up environment variables (`.env`)**:
   ```sh
   DATABASE_URL=postgresql://user:password@localhost:5432/database
   SECRET_KEY=your_secret_key
   ```
4. **Create database tables**:
   ```sh
   make build
   ```
5. **Run the application**:
   - In **development**:  
     ```sh
     make dev
     ```
   - In **production**:  
     ```sh
     make start
     ```

6. **Open in browser**:
   - **Locally**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - **Deployed application**: [https://python-project-52-svod.onrender.com](https://python-project-52-svod.onrender.com)

---

## Requirements
- Python 3.11+
- PostgreSQL
- Django, Rollbar
- UV (dependency management)

---

## License
This project is available under the MIT license.
