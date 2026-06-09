# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a modern REST API using the FastAPI framework by implementing endpoints for a simple task management system. You'll practice creating routes, handling HTTP methods, and working with request/response data structures.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application with basic GET and POST endpoints to manage a list of tasks. Students should implement endpoints to retrieve all tasks and create new tasks.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define a GET endpoint at `/tasks` that returns a list of all tasks as JSON
- Define a POST endpoint at `/tasks` that accepts a new task and adds it to the list
- Return appropriate HTTP status codes (200 for GET, 201 for successful POST)
- Example response for GET `/tasks`:
  ```json
  [
    {"id": 1, "title": "Learn FastAPI", "completed": false},
    {"id": 2, "title": "Build an API", "completed": false}
  ]
  ```

### 🛠️ Implement Task Details and Update Endpoints

#### Description
Add endpoints to retrieve a specific task by ID and update an existing task's information.

#### Requirements
Completed program should:

- Define a GET endpoint at `/tasks/{task_id}` that returns a single task by its ID
- Define a PUT endpoint at `/tasks/{task_id}` that updates a task's title and completion status
- Return a 404 status code if the task ID does not exist
- Return the updated task as JSON when successfully updated
- Example request body for PUT `/tasks/1`:
  ```json
  {"title": "Updated Task Title", "completed": true}
  ```

### 🛠️ Add Task Deletion and Status Management

#### Description
Implement an endpoint to delete tasks and a helper function to manage task completion status.

#### Requirements
Completed program should:

- Define a DELETE endpoint at `/tasks/{task_id}` that removes a task from the list
- Return a 204 status code on successful deletion
- Implement a PATCH endpoint at `/tasks/{task_id}/complete` to mark a task as completed
- Return appropriate error responses when attempting to delete or modify non-existent tasks
- Maintain task data in memory throughout the API session
