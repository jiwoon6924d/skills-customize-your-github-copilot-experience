# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API in Python using FastAPI to create, read, update, and delete data through HTTP endpoints. This assignment will help you practice API design, JSON responses, request validation, and route handling.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a FastAPI application and create a basic endpoint that returns a welcome message when the API is accessed.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define a root route that returns a JSON message
- Run the app locally with Uvicorn or a similar ASGI server
- Example response:
  ```json
  {"message": "Welcome to the FastAPI task API!"}
  ```

### 🛠️ Build a Resource Endpoint

#### Description
Create a resource for storing and retrieving items such as tasks, products, or notes through API endpoints.

#### Requirements
Completed program should:

- Store data in an in-memory list or dictionary
- Create a `GET /items` endpoint that returns all items
- Create a `GET /items/{item_id}` endpoint that returns one item by ID
- Return JSON data in a clear, consistent structure
- Example response:
  ```json
  [{"id": 1, "name": "Write code", "done": false}]
  ```

### 🛠️ Add CRUD Functionality

#### Description
Finish the API by allowing users to create, update, and delete items through HTTP requests.

#### Requirements
Completed program should:

- Add a `POST /items` endpoint to create a new item
- Add a `PUT /items/{item_id}` endpoint to update an existing item
- Add a `DELETE /items/{item_id}` endpoint to remove an item
- Validate request data using a Pydantic model
- Return useful status codes such as `200 OK`, `201 Created`, and `404 Not Found`
- Example request body:
  ```json
  {
    "name": "Study for quiz",
    "done": false
  }
  ```
