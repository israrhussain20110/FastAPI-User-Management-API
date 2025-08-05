# FastAPI User Management API

## Description

This project is a robust and secure User Management API built with FastAPI and MongoDB. It provides essential functionalities for user registration, authentication (JWT-based), and CRUD operations for user data. The API is designed with best practices for schema validation, password hashing, and proper resource management.

## Features

- User Registration
- JWT-based Authentication (Login)
- User Data Management (CRUD operations)
- Password Hashing with `bcrypt`
- Pydantic for Data Validation and Serialization
- MongoDB Integration with `motor` (async driver)
- Pagination for User Listing
- Swagger UI for API Documentation and Testing

## Setup and Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd FastAPI-User-Management-API
```

### 2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv .venv
```

**On Windows:**

```bash
.venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

*(Note: You might need to create a `requirements.txt` file if it doesn't exist by running `pip freeze > requirements.txt`)*

### 4. MongoDB Setup

Ensure you have a MongoDB instance running. The application connects to `mongodb://localhost:27017` by default. You can change this in `database.py`.

### 5. Run the Application

```bash
uvicorn main:app --reload
```

## API Documentation (Swagger UI)

Once the application is running, you can access the interactive API documentation (Swagger UI) at:

`http://localhost:8000/docs`

Here you can test all the endpoints, including user registration, login, and authenticated routes.

## Authentication

This API uses JWT (JSON Web Tokens) for authentication. To access protected routes:

1. **Register a User:** Use the `POST /users/` endpoint.
2. **Login:** Use the `POST /token` endpoint with your `username` and `password` (form-data) to get an `access_token`.
3. **Authorize in Swagger UI:** Click the "Authorize" button in Swagger UI, select "BearerAuth", and enter your token in the format `Bearer YOUR_ACCESS_TOKEN`.
4. **Access Protected Routes:** You can now make requests to protected endpoints like `GET /users/`