# todo-list-api
This is a simple and secure **To-Do List API** built with **FastAPI** and **MySQL**, featuring **CRUD functionalities** and **API key authentication**.

# Features
- Create, read, update, and delete tasks
- API Key Authentication
- MySQL as backend database

# Endpoints
- `GET /` Returns a welcome message for authorized users.
- `GET /tasks` Retrieve all tasks stored in the database.
- `POST /tasks` Add a new task to the database.
- `PUT /task/{task_id}` Update an existing task in the database.
- `DELETE /task/{task_id}` Update an existing task in the database.

# Requirements
- Python 
- Fast-API
- mysql-connector-python
- dotenv
- pydantic
- uvicorn

# Usage

Before running the API, ensure:
- You have a MySQL database running with the correct tables.
- Your `.env` file contains valid database credentials.
- Required dependencies are installed using `pip install -r requirements.txt`.

# Running the API Locally
1. **Activate your virtual environment**.
2. **Start the FastAPI server** by running the following command in your project directory:
    uvicorn main:app --reload

