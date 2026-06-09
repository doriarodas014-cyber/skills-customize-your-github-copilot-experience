from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI()

# Data model for Task
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

# In-memory storage for tasks
tasks_db = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build a REST API", "completed": False},
    {"id": 3, "title": "Deploy to production", "completed": False},
]

# Task 1: Create basic API endpoints


@app.get("/tasks")
def get_all_tasks():
    # Return all tasks
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # Create a new task and add it to the list
    pass


# Task 2: Implement task details and update endpoints


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Return a specific task by ID
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    # Update an existing task
    pass


# Task 3: Add task deletion and status management


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # Delete a task by ID
    pass


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    # Mark a task as completed
    pass


# Helper function to find a task by ID
def find_task(task_id: int):
    # Find and return a task by its ID
    pass


# Helper function to generate next task ID
def get_next_task_id():
    # Return the next available task ID
    pass


# Run the server with: uvicorn starter_code:app --reload
