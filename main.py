#import required modules
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import mysql.connector
import os
from fastapi.security.api_key import APIKeyHeader
from fastapi.openapi.models import APIKey
from fastapi.openapi.utils import get_openapi
from dotenv import load_dotenv
from db import db, cursor

# Loading environment variables 
load_dotenv()

# Create the FastAPI 
app = FastAPI()
api_key_header = APIKeyHeader(name="api_key", auto_error=False)

# Define the Task model
class Task(BaseModel):
    task: str
    completed: bool

# API key checker
async def authenticate(api_key: str):
    cursor.execute("SELECT api_key FROM api_keys WHERE api_key = %s", (api_key,))
    if not cursor.fetchone():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
    
@app.get("/")
async def welcome(api_key: str):
    await authenticate(api_key)
    return {"message": "Welcome to the To-Do List API"}

# Get all tasks
@app.get("/tasks")
async def read_tasks(api_key: str):
    await authenticate(api_key)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return tasks

# Add a new task
@app.post("/tasks")
async def create_task(tasks: Task, api_key: str):
    await authenticate(api_key)
    cursor.execute("INSERT INTO tasks (task, completed) VALUES (%s, %s)", (tasks.task, tasks.completed))
    db.commit()
    return {"message": "Task created", "task": tasks.task}

# Update a task
@app.put("/tasks/{id}")
async def update_task(id: int, tasks: Task, api_key: str):
    await authenticate(api_key)
    cursor.execute("UPDATE tasks SET task = %s, completed = %s WHERE id = %s", (tasks.task, tasks.completed, id))
    db.commit()
    return {"message": "Task updated", "id": id}

# Delete a task
@app.delete("/tasks/{id}")
async def delete_task(id: int, api_key: str):
    await authenticate(api_key)
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    db.commit()
    return {"message": "Task deleted", "id": id}

