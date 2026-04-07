# FastAPI - Modern Python Web Framework

A comprehensive guide to understanding APIs and building them with FastAPI.

---

## Part 0: Understanding APIs (Fundamentals)

### What is an API?

**API** stands for **Application Programming Interface**. It's a set of rules and protocols that allows different software applications to communicate with each other.

**Simple Analogy:** Think of a restaurant:
- You (the customer) = Client/Frontend
- The menu = API documentation
- The waiter = API
- The kitchen = Server/Backend

You don't go into the kitchen yourself. You tell the waiter what you want, and the waiter brings back your food. Similarly, an API takes your request, communicates with the server, and returns the response.

---

### Why Do We Need APIs?

| Reason | Explanation |
|--------|-------------|
| **Separation of Concerns** | Frontend and backend can be developed independently |
| **Reusability** | Same API can serve web, mobile, and desktop apps |
| **Security** | Users don't interact directly with the database |
| **Scalability** | Different parts of the system can scale independently |
| **Integration** | Different services can communicate (e.g., payment gateways, maps) |

---

### Types of APIs

| Type | Description | Example |
|------|-------------|---------|
| **Web APIs** | Accessed over HTTP/HTTPS | REST API, GraphQL |
| **Library APIs** | Functions provided by a library | Python's `os` module |
| **Operating System APIs** | Interface to OS features | Windows API |
| **Database APIs** | Interface to databases | JDBC, ODBC |

**This document focuses on Web APIs (specifically REST APIs).**

---

### What is REST?

**REST** stands for **Representational State Transfer**. It's an architectural style for designing web APIs.

**REST Principles:**

| Principle | Description |
|-----------|-------------|
| **Stateless** | Each request contains all information needed; server doesn't store client state |
| **Client-Server** | Client and server are separate; they communicate via requests/responses |
| **Uniform Interface** | Consistent way to interact with resources (URLs + HTTP methods) |
| **Resource-Based** | Everything is a resource identified by a URL |

---

### How Web APIs Work

```
┌─────────────┐         HTTP Request          ┌─────────────┐
│             │  ─────────────────────────>   │             │
│   CLIENT    │   GET /api/users/123          │   SERVER    │
│  (Browser,  │                               │  (FastAPI,  │
│   Mobile)   │  <─────────────────────────   │   Django)   │
│             │         HTTP Response         │             │
└─────────────┘   {"name": "John", "age": 25} └─────────────┘
```

**The Request-Response Cycle:**

1. **Client sends a request** - Includes URL, HTTP method, headers, and optionally a body
2. **Server processes the request** - Validates, performs operations, queries database
3. **Server sends a response** - Includes status code, headers, and response body (usually JSON)

---

### HTTP Methods (Verbs)

HTTP methods define what action to perform on a resource:

| Method | Purpose | Example | Has Body |
|--------|---------|---------|----------|
| **GET** | Retrieve data | Get user profile | No |
| **POST** | Create new data | Create new user | Yes |
| **PUT** | Update entire resource | Update all user fields | Yes |
| **PATCH** | Partial update | Update only email | Yes |
| **DELETE** | Remove data | Delete a user | No |

**Example URLs:**
```
GET    /api/users          → Get all users
GET    /api/users/123      → Get user with ID 123
POST   /api/users          → Create a new user
PUT    /api/users/123      → Update user 123 (replace all fields)
PATCH  /api/users/123      → Update user 123 (partial update)
DELETE /api/users/123      → Delete user 123
```

---

### HTTP Status Codes

Status codes tell the client what happened with their request:

| Code Range | Category | Common Codes |
|------------|----------|--------------|
| **1xx** | Informational | 100 Continue |
| **2xx** | Success | 200 OK, 201 Created, 204 No Content |
| **3xx** | Redirection | 301 Moved Permanently, 304 Not Modified |
| **4xx** | Client Error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| **5xx** | Server Error | 500 Internal Server Error, 503 Service Unavailable |

**Common Status Codes Explained:**

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST (resource created) |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Authenticated but not allowed |
| 404 | Not Found | Resource doesn't exist |
| 422 | Unprocessable Entity | Validation error |
| 500 | Internal Server Error | Server crashed |

---

### What is JSON?

**JSON** (JavaScript Object Notation) is the most common data format for APIs.

```json
{
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "is_active": true,
    "roles": ["admin", "user"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}
```

**JSON Data Types:**
- **String**: `"hello"`
- **Number**: `42`, `3.14`
- **Boolean**: `true`, `false`
- **Null**: `null`
- **Array**: `[1, 2, 3]`
- **Object**: `{"key": "value"}`

---

### Request and Response Structure

**HTTP Request:**
```
POST /api/users HTTP/1.1              ← Request line (method, URL, version)
Host: api.example.com                 ← Headers
Content-Type: application/json
Authorization: Bearer token123

{                                     ← Body (for POST/PUT/PATCH)
    "name": "John",
    "email": "john@example.com"
}
```

**HTTP Response:**
```
HTTP/1.1 201 Created                  ← Status line
Content-Type: application/json
Date: Mon, 15 Jan 2024 10:30:00 GMT

{                                     ← Response body
    "id": 1,
    "name": "John",
    "email": "john@example.com",
    "created_at": "2024-01-15T10:30:00Z"
}
```

---

### Common API Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Content-Type` | Format of request body | `application/json` |
| `Accept` | Expected response format | `application/json` |
| `Authorization` | Authentication token | `Bearer eyJhbGc...` |
| `User-Agent` | Client information | `Mozilla/5.0...` |
| `Cache-Control` | Caching behavior | `no-cache` |

---

### API Authentication Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| **API Key** | Simple key in header/query | Public APIs |
| **Basic Auth** | Username:password encoded in Base64 | Simple internal APIs |
| **Bearer Token** | Token in Authorization header | Modern apps |
| **JWT** | JSON Web Token with encoded data | Stateless authentication |
| **OAuth 2.0** | Third-party authorization | "Login with Google" |

**Example - Bearer Token:**
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

### Testing APIs

You can test APIs using various tools:

| Tool | Type | Use Case |
|------|------|----------|
| **Postman** | GUI Application | Comprehensive API testing |
| **cURL** | Command Line | Quick terminal testing |
| **HTTPie** | Command Line | User-friendly terminal testing |
| **Browser** | GUI | Simple GET requests |
| **Python requests** | Code | Automated testing |

**Example - Using cURL:**
```bash
# GET request
curl https://api.example.com/users

# POST request with JSON body
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}'
```

**Example - Using Python requests:**
```python
import requests

# GET request
response = requests.get("https://api.example.com/users")
print(response.json())

# POST request
data = {"name": "John", "email": "john@example.com"}
response = requests.post("https://api.example.com/users", json=data)
print(response.status_code)  # 201
print(response.json())       # {"id": 1, "name": "John", ...}
```

---

### API Design Best Practices

| Practice | Good | Bad |
|----------|------|-----|
| Use nouns for resources | `/users`, `/products` | `/getUsers`, `/createProduct` |
| Use plural names | `/users/123` | `/user/123` |
| Use HTTP methods correctly | `DELETE /users/123` | `POST /deleteUser` |
| Version your API | `/api/v1/users` | `/api/users` |
| Use proper status codes | `404` for not found | `200` for everything |
| Handle errors gracefully | `{"error": "User not found"}` | `500 Internal Error` |

---

### Real-World API Example

Let's trace a real scenario: **User logs in and views their profile**

```
Step 1: Login
─────────────────────────────────────────────────────────
POST /api/auth/login
Body: {"email": "john@example.com", "password": "secret123"}

Response (200 OK):
{"access_token": "eyJhbGc...", "token_type": "bearer"}

Step 2: Get Profile (using the token)
─────────────────────────────────────────────────────────
GET /api/users/me
Headers: Authorization: Bearer eyJhbGc...

Response (200 OK):
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2024-01-01T00:00:00Z"
}
```

---

### Summary: Key Takeaways

1. **API** = A contract between client and server for communication
2. **REST** = An architectural style using HTTP methods and URLs
3. **JSON** = The standard data format for modern APIs
4. **HTTP Methods** = GET (read), POST (create), PUT/PATCH (update), DELETE (remove)
5. **Status Codes** = 2xx (success), 4xx (client error), 5xx (server error)
6. **Authentication** = API keys, tokens, JWT, OAuth

Now that you understand APIs, let's learn how to build them with FastAPI!

---
---

## What is FastAPI?

FastAPI is a modern, high-performance Python web framework for building APIs. It's built on top of Starlette (for web handling) and Pydantic (for data validation).

### Key Features

| Feature | Description |
|---------|-------------|
| **High Performance** | One of the fastest Python frameworks, comparable to Node.js and Go |
| **Type Hints** | Uses Python type hints for automatic validation and documentation |
| **Auto Documentation** | Generates interactive Swagger UI and ReDoc documentation |
| **Async Support** | Native support for `async`/`await` |
| **Data Validation** | Automatic request/response validation using Pydantic |
| **Easy to Learn** | Intuitive API with minimal boilerplate |

---

## Setting Up a Virtual Environment

Before installing FastAPI (or any Python packages), it's best practice to create a **virtual environment**. This keeps your project dependencies isolated from other projects and your system Python.

### Why Use a Virtual Environment?

| Benefit | Explanation |
|---------|-------------|
| **Isolation** | Each project has its own dependencies, avoiding conflicts |
| **Clean System** | Keeps your global Python installation clean |
| **Reproducibility** | Easy to share exact dependencies via `requirements.txt` |
| **Version Control** | Different projects can use different versions of the same package |

**Problem without virtual environment:**
```
Project A needs: requests==2.25.0
Project B needs: requests==2.31.0
Without venv → One project breaks!
With venv → Both work perfectly in isolation.
```

---

### Creating a Virtual Environment

**Using `venv` (built-in, recommended):**

```bash
# Navigate to your project folder
cd my_fastapi_project

# Create a virtual environment named 'venv'
python -m venv venv
```

This creates a `venv/` folder containing:
- A copy of the Python interpreter
- The `pip` package manager
- A place for installed packages

---

### Activating the Virtual Environment

You must **activate** the environment before installing packages:

| Operating System | Command |
|------------------|---------|
| **Windows (CMD)** | `venv\Scripts\activate` |
| **Windows (PowerShell)** | `venv\Scripts\Activate.ps1` |
| **macOS / Linux** | `source venv/bin/activate` |

**After activation, your terminal shows:**
```bash
(venv) $ _
```

The `(venv)` prefix indicates you're inside the virtual environment.

---

### Deactivating the Virtual Environment

When you're done working:

```bash
deactivate
```

The `(venv)` prefix disappears, and you're back to your system Python.

---

### Installing Packages in Virtual Environment

**Always activate first, then install:**

```bash
# Activate (macOS/Linux)
source venv/bin/activate

# Now install packages - they go into venv/, not system Python
pip install fastapi uvicorn

# Verify installation
pip list
```

---

### Creating requirements.txt

Save your project's dependencies to a file:

```bash
# Generate requirements.txt from installed packages
pip freeze > requirements.txt
```

**Example `requirements.txt`:**
```
annotated-types==0.6.0
anyio==4.2.0
fastapi==0.109.0
pydantic==2.5.3
starlette==0.35.1
uvicorn==0.27.0
```

---

### Installing from requirements.txt

When someone clones your project (or you set it up on a new machine):

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install all dependencies
pip install -r requirements.txt
```

---

### Virtual Environment Best Practices

| Practice | Description |
|----------|-------------|
| **Never commit `venv/`** | Add `venv/` to `.gitignore` |
| **Always use `requirements.txt`** | Commit this file to version control |
| **One venv per project** | Don't share virtual environments between projects |
| **Name it `venv` or `.venv`** | Standard naming conventions |
| **Activate before installing** | Ensure packages go to the right place |

**Add to `.gitignore`:**
```
venv/
.venv/
__pycache__/
*.pyc
```

---

### Complete Project Setup Workflow

```bash
# 1. Create project folder
mkdir my_fastapi_app
cd my_fastapi_app

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# 4. Install packages
pip install fastapi uvicorn

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Create .gitignore
echo "venv/" >> .gitignore

# 7. Start coding!
```

---

### Alternative: Using `conda`

If you prefer Anaconda/Miniconda (popular for data science):

```bash
# Create environment
conda create -n fastapi-env python=3.11

# Activate
conda activate fastapi-env

# Install packages
pip install fastapi uvicorn

# Deactivate
conda deactivate
```

---

Now that your environment is set up, let's install FastAPI!

---

## Installation

**Make sure your virtual environment is activated first!**

```bash
# Install FastAPI
pip install fastapi

# Install ASGI server (Uvicorn recommended)
pip install uvicorn

# Or install both together
pip install fastapi[all]

# Save to requirements.txt
pip freeze > requirements.txt
```

---

## Part 1: Basic Concepts

### 1.1 Hello World

```python
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

**Run the server:**
```bash
uvicorn main:app --reload
```

- `main` - the file name (main.py)
- `app` - the FastAPI instance
- `--reload` - auto-reload on code changes (development only)

---

### 1.2 Path Parameters

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Multiple path parameters
@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}
```

**Type conversion is automatic:**
- `/items/42` returns `{"item_id": 42}` (as integer)
- `/items/foo` returns 422 Validation Error

---

### 1.3 Query Parameters

```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# URL: /items/?skip=5&limit=20
```

**Optional parameters:**
```python
from typing import Optional

@app.get("/search/")
def search(q: Optional[str] = None):
    if q:
        return {"query": q}
    return {"query": "No search term provided"}
```

---

### 1.4 Request Body with Pydantic

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define data model
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    is_available: bool = True

# Use model in endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

**Request body (JSON):**
```json
{
    "name": "Laptop",
    "price": 999.99,
    "description": "A powerful laptop"
}
```

---

## Part 2: HTTP Methods

### 2.1 CRUD Operations

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

# In-memory database
items_db = {}

# CREATE
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item_id] = item
    return {"message": "Item created", "item": item}

# READ
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return {"message": "Item updated", "item": item}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted"}
```

---

### 2.2 HTTP Methods Summary

| Method | Decorator | Use Case |
|--------|-----------|----------|
| GET | `@app.get()` | Retrieve data |
| POST | `@app.post()` | Create new resource |
| PUT | `@app.put()` | Update entire resource |
| PATCH | `@app.patch()` | Partial update |
| DELETE | `@app.delete()` | Delete resource |

---

## Part 3: Response Handling

### 3.1 Response Model

```python
from pydantic import BaseModel

class ItemIn(BaseModel):
    name: str
    price: float
    password: str  # Sensitive data

class ItemOut(BaseModel):
    name: str
    price: float
    # password excluded from response

@app.post("/items/", response_model=ItemOut)
def create_item(item: ItemIn):
    return item  # password automatically filtered out
```

---

### 3.2 Status Codes

```python
from fastapi import FastAPI, status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None
```

**Common status codes:**

| Code | Constant | Meaning |
|------|----------|---------|
| 200 | `HTTP_200_OK` | Success |
| 201 | `HTTP_201_CREATED` | Resource created |
| 204 | `HTTP_204_NO_CONTENT` | Success, no content |
| 400 | `HTTP_400_BAD_REQUEST` | Bad request |
| 404 | `HTTP_404_NOT_FOUND` | Not found |
| 422 | `HTTP_422_UNPROCESSABLE_ENTITY` | Validation error |

---

## Part 4: Async/Await

### 4.1 Async Endpoints

```python
import asyncio

@app.get("/async-example")
async def async_endpoint():
    await asyncio.sleep(1)  # Non-blocking sleep
    return {"message": "This was async!"}
```

### 4.2 When to Use Async

| Scenario | Use |
|----------|-----|
| I/O bound operations (API calls, DB queries) | `async def` |
| CPU bound operations | `def` (regular function) |
| Third-party sync libraries | `def` (regular function) |

```python
# Async database query example
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await database.fetch_one(query, values={"id": user_id})
    return user
```

---

## Part 5: Dependency Injection

### 5.1 Basic Dependencies

```python
from fastapi import Depends

def get_db():
    db = DatabaseSession()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```

### 5.2 Authentication Dependency

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != "valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    return token

@app.get("/protected")
def protected_route(token: str = Depends(verify_token)):
    return {"message": "You have access!", "token": token}
```

---

## Part 6: Middleware and CORS

### 6.1 Custom Middleware

```python
import time
from fastapi import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### 6.2 CORS (Cross-Origin Resource Sharing)

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Part 7: File Uploads

```python
from fastapi import File, UploadFile

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }

# Multiple files
@app.post("/upload-multiple/")
async def upload_files(files: list[UploadFile] = File(...)):
    return {"filenames": [f.filename for f in files]}
```

---

## Part 8: API Router (Organizing Large Apps)

### 8.1 Creating Routers

**routers/users.py:**
```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def get_users():
    return [{"name": "John"}, {"name": "Jane"}]

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### 8.2 Including Routers

**main.py:**
```python
from fastapi import FastAPI
from routers import users, items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
```

---

## Part 9: Auto Documentation

FastAPI automatically generates interactive API documentation:

| URL | Documentation Type |
|-----|-------------------|
| `/docs` | Swagger UI (interactive) |
| `/redoc` | ReDoc (clean, readable) |
| `/openapi.json` | OpenAPI schema (JSON) |

### Customizing Documentation

```python
app = FastAPI(
    title="My API",
    description="A sample API built with FastAPI",
    version="1.0.0",
    docs_url="/documentation",  # Custom Swagger URL
    redoc_url="/redoc"
)
```

---

## Part 10: Complete Example

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

app = FastAPI(title="Todo API", version="1.0.0")

# Models
class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoCreate):
    id: int
    created_at: datetime

# In-memory storage
todos_db: dict[int, Todo] = {}
counter = 0

# Dependency
def get_todo_or_404(todo_id: int) -> Todo:
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos_db[todo_id]

# Endpoints
@app.get("/todos", response_model=list[Todo])
def list_todos(completed: Optional[bool] = None):
    todos = list(todos_db.values())
    if completed is not None:
        todos = [t for t in todos if t.completed == completed]
    return todos

@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    global counter
    counter += 1
    new_todo = Todo(
        id=counter,
        created_at=datetime.now(),
        **todo.model_dump()
    )
    todos_db[counter] = new_todo
    return new_todo

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo: Todo = Depends(get_todo_or_404)):
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoCreate, existing: Todo = Depends(get_todo_or_404)):
    updated = Todo(
        id=existing.id,
        created_at=existing.created_at,
        **todo_update.model_dump()
    )
    todos_db[todo_id] = updated
    return updated

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, _: Todo = Depends(get_todo_or_404)):
    del todos_db[todo_id]

# Run: uvicorn main:app --reload
```

---

## Quick Reference

### Project Structure (Recommended)

```
my_api/
├── main.py              # FastAPI app instance
├── routers/
│   ├── __init__.py
│   ├── users.py
│   └── items.py
├── models/
│   ├── __init__.py
│   └── schemas.py       # Pydantic models
├── dependencies/
│   └── auth.py
├── database/
│   └── connection.py
└── requirements.txt
```

### Essential Commands

```bash
# Development server
uvicorn main:app --reload

# Production server
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# With Gunicorn (production)
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

---

## Resources

- [Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI GitHub](https://github.com/tiangolo/fastapi)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Starlette Documentation](https://www.starlette.io/)
