# API Concepts - Interview Prep

## 1. What is an API?

API (Application Programming Interface) is a contract that allows two applications to communicate with each other. It defines what requests can be made, how to make them, and what responses to expect.

**Example:** A frontend app calls `GET /users/1` to fetch user data from a backend server. The backend processes the request and returns a JSON response.

---

## 2. GET vs POST

| | GET | POST |
|---|---|---|
| Purpose | Fetch/read data | Send/create data |
| Data sent via | URL query parameters | Request body |
| Idempotent | Yes (same request = same result) | No (can create duplicates) |
| Cacheable | Yes | No |
| Bookmarkable | Yes | No |
| Example | `GET /logs?type=error` | `POST /logs` with body `{"level": "error", "message": "disk full"}` |

**Key line for interviews:** GET is for reading, POST is for writing. GET sends data in the URL, POST sends it in the body.

---

## 3. What are Status Codes?

Standard 3-digit codes returned by the server to indicate the result of a request.

| Range | Meaning | Common Examples |
|---|---|---|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirection | 301 Moved Permanently, 304 Not Modified |
| 4xx | Client Error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 422 Unprocessable Entity |
| 5xx | Server Error | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

**Key line for interviews:** 2xx means the request succeeded, 4xx means the client made a mistake, 5xx means the server failed.

---

## 4. What is a REST API?

REST (Representational State Transfer) is an architectural style for building APIs. A REST API follows these principles:

- **Standard HTTP methods** - uses GET, POST, PUT, PATCH, DELETE for CRUD operations
- **Stateless** - every request is independent; the server stores no client session
- **Resource-based URLs** - endpoints represent resources (`/users`, `/logs/1`), not actions
- **JSON responses** - data is typically exchanged in JSON format

| HTTP Method | CRUD Operation | Example |
|---|---|---|
| GET | Read | `GET /logs` |
| POST | Create | `POST /logs` |
| PUT | Full Update | `PUT /logs/1` |
| PATCH | Partial Update | `PATCH /logs/1` |
| DELETE | Delete | `DELETE /logs/1` |

**Key line for interviews:** REST is a set of rules for designing APIs around resources, using standard HTTP methods, where each request is stateless and self-contained.
