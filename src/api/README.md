# GBCMS API Layer

## Overview
The GBCMS API Layer is built using FastAPI and provides RESTful endpoints and WebSocket support for managing projects and authentication. It serves as the backend interface for the GBCMS application, handling all API-related operations.

## Features
- **Authentication**: JWT-based authentication for secure access.
- **Project Management**: Create, retrieve, update, and delete projects.
- **WebSockets**: Real-time communication support.
- **API Gateway**: Middleware for logging and authentication.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-repo/gbcms.git
    ```

2. **Navigate to the API Directory**
    ```bash
    cd gbcms/src/api
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**
    Create a `.env` file in the root directory with the following:
    ```
    JWT_SECRET=your_secret_key
    ```

## Usage

1. **Run the API Server**
    ```bash
    uvicorn main:app --reload
    ```

2. **Access API Documentation**
    Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

## Endpoints

### Authentication
- **POST** `/api/auth/login`: Authenticate a user and receive a JWT.

### Projects
- **POST** `/api/projects/`: Create a new project.
- **GET** `/api/projects/{project_id}`: Retrieve a project by ID.
- **PUT** `/api/projects/{project_id}`: Update a project.
- **DELETE** `/api/projects/{project_id}`: Delete a project.

## WebSockets
- **WebSocket Endpoint**: `/ws`
    - Handles real-time communication for the application.

## Middleware
- **API Gateway Middleware**: Handles logging and authentication for incoming requests.

## Error Handling
The API uses standardized HTTP status codes to indicate success or failure of requests, with detailed error messages for troubleshooting.

## Testing
To run tests, navigate to the API directory and execute:
