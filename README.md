# RBAC Authentication and Authorization System

## Overview

This project implements a secure backend system featuring **Authentication**, **Authorization**, and **Role-Based Access Control (RBAC)**. Users can register, log in, and access protected resources based on their assigned roles and permissions. The system adheres to best practices for security, scalability, and maintainability.

---

## Features

### **Authentication**
- User registration with secure password hashing (`bcrypt`).
- User login with JWT token generation for session management.
- Token-based authentication for stateless API requests.

### **Authorization**
- Dynamic role and permission management via `/role/add_role` API.
- Restricted access to protected routes based on user roles and permissions.

### **Role-Based Access Control (RBAC)**
- Roles and permissions stored in a relational database.
- Flexible access control based on user roles and associated permissions.

---

## Endpoints

### **Authentication**
- `POST /auth/register`: Register a new user with a username, password, and role.
- `POST /auth/login`: Log in a user and receive a JWT token.
- `POST /auth/logout` (optional): Log out a user and invalidate their session.

### **Role Management**
- `POST /role/add_role`: Create a new role with specified permissions.

### **Protected Routes**
- `GET /api/protected`: Example of a secured route accessible only to users with specific roles.

---

## Installation

1. Clone the repository:
   git clone <repository_url>
   cd <repository_folder>
2. Install dependencies:
   pip install -r requirements.txt
3. Apply migrations:
   flask db upgrade
4. Start the server:
   python app.py

## Usage
### Register a User:

POST /auth/register
{
  "username": "testuser",
  "password": "password123",
  "role": "admin"
}

### Log In:

POST /auth/login
{
  "username": "testuser",
  "password": "password123"
}

#### Response:

{
  "token": "<JWT_TOKEN>"
}

### Add a Role:

POST /role/add_role
{
  "name": "admin",
  "permissions": ["view_protected", "edit_data"]
}

### Access a Protected Route:

GET /api/protected
Headers: {
  "Authorization": "Bearer <JWT_TOKEN>"
}

## Testing
Use Postman or cURL to test the endpoints.
Ensure roles are created using /role/add_role before assigning them to users during registration.

## Technologies Used
Flask: Backend framework.\
JWT: For token-based authentication.\
SQLAlchemy: ORM for database operations.\
bcrypt: For secure password hashing.

