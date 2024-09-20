
# Execution Engine Module Documentation

## Table of Contents
- [Overview](#overview)
- [Module Structure](#module-structure)
- [Components](#components)
  - [Execution Manager](#execution-manager)
  - [Environment Provisioner](#environment-provisioner)
  - [Security Sandbox](#security-sandbox)
- [Data Model](#data-model)
  - [Entities](#entities)
  - [Attributes](#attributes)
  - [Relationships](#relationships)
- [API Specifications](#api-specifications)
  - [Endpoints](#endpoints)
    - [Start Execution](#start-execution)
    - [Monitor Execution](#monitor-execution)
    - [Terminate Execution](#terminate-execution)
- [Implementation Details](#implementation-details)
  - [Interaction Flow](#interaction-flow)
  - [Error Handling](#error-handling)
  - [Logging](#logging)
- [Security Considerations](#security-considerations)
- [Performance & Scalability](#performance--scalability)
- [Extensibility](#extensibility)
- [Example Use Cases](#example-use-cases)
- [Glossary](#glossary)
- [Visual Aids](#visual-aids)
- [Testing Strategies](#testing-strategies)
- [Deployment Instructions](#deployment-instructions)
- [Version Control and Update Logs](#version-control-and-update-logs)
- [Feedback Mechanism](#feedback-mechanism)
- [Licensing Information](#licensing-information)

## Overview
The Execution Engine Module is responsible for running projects within the Graph-Based Codebase Management System (GBCMS). It manages the execution environments, handles resource allocation, monitors ongoing executions, and ensures that executions are performed securely and efficiently. This module is critical for testing, deploying, and validating projects, providing real-time feedback and results to users.

### Key Responsibilities:
- **Project Execution**: Allow for running projects that are uploaded to the database.
- **Environment Management**: Manage execution environments (e.g., virtual environments, containers).
- **Resource Allocation**: Handle resource management for running projects.
- **Monitoring and Logging**: Track execution status, resource usage, and capture outputs.
- **Security**: Ensure executed code runs in secure and isolated environments.

## Module Structure
The Execution Engine Module is organized into the following key components:
1. **Execution Manager**
2. **Environment Provisioner**
3. **Security Sandbox**

## Components

### Execution Manager
**Description:**

Orchestrates the execution of projects, managing the lifecycle of each execution task from initiation to completion or termination.

**Classes and Methods:**
- `ExecutionManager`
  - `start_execution(project_id)`: Initiates the execution of a project.
  - `monitor_execution(execution_id)`: Monitors the status and progress of a running execution.
  - `terminate_execution(execution_id)`: Stops a running execution.
  - `get_execution_logs(execution_id)`: Retrieves logs generated during execution.

**Technologies Used:**
- **Celery**: For managing asynchronous execution tasks.
- **RabbitMQ/Redis**: As message brokers for task queues.
- **Prometheus**: For monitoring execution metrics.

### Environment Provisioner
**Description:**

Sets up and manages the necessary environments for project execution, including deploying containers or virtual machines based on project requirements.

**Classes and Methods:**
- `EnvironmentProvisioner`
  - `create_environment(project_config)`: Sets up an execution environment based on project specifications.
  - `destroy_environment(environment_id)`: Tears down the specified environment after execution.

**Technologies Used:**
- **Docker**: For containerization of execution environments.
- **Kubernetes**: For orchestrating containers at scale.
- **Terraform**: For managing infrastructure as code, if needed.

### Security Sandbox
**Description:**

Ensures that all executed code runs in a secure and isolated environment to prevent malicious activities and protect the host system.

**Classes and Methods:**
- `SecuritySandbox`
  - `initialize_sandbox(environment_id)`: Sets up security constraints and isolation for the execution environment.
  - `enforce_security_policies(execution_id)`: Applies security policies during execution.

**Technologies Used:**
- **AppArmor/SELinux**: For enforcing security policies on containers.
- **Sandboxing Tools**: Such as Firejail or gVisor for additional isolation.

## Data Model

### Entities
- **Execution**
- **Environment**
- **Project**
- **User**

### Attributes

#### Execution
- `id`: Unique identifier.
- `project_id`: Reference to the project being executed.
- `status`: Current status (e.g., Running, Completed, Failed).
- `started_at`: Timestamp when execution started.
- `ended_at`: Timestamp when execution ended.
- `logs`: Reference to execution logs.

#### Environment
- `id`: Unique identifier.
- `project_id`: Reference to the associated project.
- `environment_type`: Type of environment (e.g., Docker container, VM).
- `created_at`: Timestamp of environment creation.
- `destroyed_at`: Timestamp when environment was destroyed.

#### Project
- `id`: Unique identifier.
- `name`: Name of the project.
- `description`: Brief description.
- `created_at`: Timestamp of creation.
- `updated_at`: Timestamp of last update.
- `owner_id`: Reference to the owning user.

#### User
- `id`: Unique identifier.
- `username`: User's display name.
- `email`: User's email address.
- `role`: User's role (e.g., Admin, Developer).

### Relationships
- **Project** can have multiple **Executions**.
- **Project** is linked to one **Environment** per execution.
- **User** owns multiple **Projects**.

## API Specifications

### Endpoints

#### Start Execution
- **Endpoint**: `POST /api/executions`
- **Description**: Initiates the execution of a project.
- **Request Body**:
  ```json
  {
    "project_id": "project123"
  }
  ```
- **Response**:
  ```json
  {
    "id": "execution789",
    "project_id": "project123",
    "status": "Running",
    "started_at": "2024-04-27T12:00:00Z"
  }
  ```

#### Monitor Execution
- **Endpoint**: `GET /api/executions/{execution_id}`
- **Description**: Retrieves the current status and details of an ongoing or completed execution.
- **Response**:
  ```json
  {
    "id": "execution789",
    "project_id": "project123",
    "status": "Running",
    "started_at": "2024-04-27T12:00:00Z",
    "ended_at": null,
    "logs": "path/to/execution789.log"
  }
  ```

#### Terminate Execution
- **Endpoint**: `POST /api/executions/{execution_id}/terminate`
- **Description**: Terminates a running execution.
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Execution terminated successfully.",
    "execution_id": "execution789",
    "terminated_at": "2024-04-27T12:30:00Z"
  }
  ```

## Implementation Details

### Interaction Flow
1. **Initiating Execution**:
   - User initiates a project execution via the UI.
   - Frontend sends a `POST /api/executions` request with `project_id`.
   - Backend creates an `Execution` record and starts the Execution Manager.
2. **Environment Setup**:
   - Execution Manager invokes the Environment Provisioner to create an execution environment.
   - Environment is set up using Docker/Kubernetes based on project configuration.
3. **Code Execution**:
   - Execution Manager runs the project's code within the provisioned environment.
   - Logs are captured and stored for monitoring.
4. **Monitoring**:
   - Frontend periodically polls the `GET /api/executions/{execution_id}` endpoint or uses WebSockets for real-time updates.
5. **Completion or Termination**:
   - Upon completion, Execution Manager updates the `Execution` status.
   - If terminated, Execution Manager stops the execution and cleans up the environment.

### Error Handling
- **Environment Setup Failures**: Returns 500 Internal Server Error with details.
- **Execution Failures**: Marks execution as Failed, logs errors, and notifies the user.
- **Termination Issues**: Ensures that resources are cleaned up even if termination requests fail.

### Logging
- **Execution Logs**: Captures stdout/stderr from executed code.
- **System Logs**: Records actions like execution start, completion, failures, and terminations.
- **Access Logs**: Tracks API usage and access patterns for auditing purposes.

## Security Considerations
- **Isolation**: Executed code runs in isolated environments to prevent host system compromise.
- **Resource Limits**: Enforces CPU, memory, and disk usage limits to prevent resource exhaustion.
- **Network Restrictions**: Restricts network access for execution environments as necessary.
- **Input Validation**: Validates all inputs to API endpoints to prevent injection and other attacks.
- **Access Control**: Ensures only authorized users can initiate or manage executions.

## Performance & Scalability
- **Autoscaling**: Utilizes Kubernetes to scale execution environments based on demand.
- **Load Balancing**: Distributes execution tasks across multiple instances to balance load.
- **Optimized Resource Allocation**: Efficiently manages resources to maximize throughput and minimize latency.
- **Caching**: Caches frequently accessed data to reduce response times.

## Extensibility
- **Plugin Support**: Allows adding support for new execution environments or languages.
- **Modular Components**: Execution Manager, Environment Provisioner, and Security Sandbox can be extended or replaced independently.
- **API Extensions**: Provides hooks for integrating with additional services or tools.

## Example Use Cases

### 1. Running a Test Suite
**Scenario:**
A user wants to execute the project's test suite to verify recent changes.

**Steps:**
1. User selects the project and chooses "Run Tests" in the UI.
2. Frontend sends a `POST /api/executions` request with the `project_id`.
3. Execution Manager sets up the environment and runs the test suite.
4. Execution status is updated in real-time.
5. Upon completion, test results and logs are displayed to the user.

### 2. Executing Deployment Scripts
**Scenario:**
A user needs to deploy the project to a staging environment.

**Steps:**
1. User initiates deployment through the UI.
2. Frontend sends a `POST /api/executions` request with the `project_id`.
3. Execution Manager runs deployment scripts in a secure environment.
4. Deployment progress and status are monitored and displayed.
5. Success or failure notifications are provided upon completion.

### 3. Terminating a Long-Running Process
**Scenario:**
A user realizes that a project’s execution is stuck and needs to terminate it.

**Steps:**
1. User views the running executions in the UI.
2. Clicks "Terminate" on the stuck execution.
3. Frontend sends a `POST /api/executions/{execution_id}/terminate` request.
4. Execution Manager stops the execution and cleans up the environment.
5. User receives confirmation that the execution has been terminated.

## Glossary
- **GBCMS (Graph-Based Codebase Management System)**: A system for managing codebases using graph-based representations.
- **JWT (JSON Web Token)**: A compact URL-safe means of representing claims to be transferred between two parties.
- **API (Application Programming Interface)**: A set of rules that allow different software entities to communicate with each other.
- **CI/CD (Continuous Integration/Continuous Deployment)**: Practices that enable automated building, testing, and deployment of code.
- **Docker**: A platform for developing, shipping, and running applications inside containers.
- **Kubernetes**: An open-source system for automating deployment, scaling, and management of containerized applications.
- **Celery**: An asynchronous task queue/job queue based on distributed message passing.
- **AppArmor/SELinux**: Security modules in the Linux kernel for enforcing security policies.

## Visual Aids
![Execution Engine Module Architecture](path/to/execution_engine_module_architecture_diagram.png)
![Execution Workflow](path/to/execution_workflow_diagram.png)

## Testing Strategies
- **Unit Tests**:
  - Test individual methods in `ExecutionManager`, `EnvironmentProvisioner`, and `SecuritySandbox`.
  - *Example*: Verify that `start_execution` correctly initiates an execution and creates necessary records.
- **Integration Tests**:
  - Ensure that components like `ExecutionManager` and `Environment Provisioner` work together seamlessly.
  - *Example*: Test the full flow of starting an execution, setting up the environment, and execution monitoring.
- **End-to-End (E2E) Tests**:
  - Simulate user interactions to validate the entire execution workflow.
  - *Example*: Automate the process of starting a project execution, monitoring it, and terminating it.
- **Performance Testing**:
  - Assess the module's responsiveness and resource usage under high load.
  - *Example*: Load test the execution initiation endpoint with multiple simultaneous requests.

## Deployment Instructions
- **Environment Setup**:
  1. **Dependencies**: Install necessary packages using `pip install -r requirements.txt`.
  2. **Configuration**: Set environment variables in `.env` files, including database URLs, JWT secrets, and message broker settings.
- **Build and Deploy**:
  1. **Containerization**: Use Docker to containerize the Execution Engine Module.
     ```bash
     docker build -t gbcms-execution-engine .
     ```
  2. **Deployment**: Deploy the container using Kubernetes or Docker Compose.
     ```bash
     docker-compose up -d
     ```
- **Rollback Procedures**:
  1. **Maintain Previous Images**: Keep older Docker images tagged appropriately.
  2. **Use CI/CD Tools**: Utilize CI/CD pipelines to manage and execute rollback procedures if deployment fails.

## Version Control and Update Logs
- **Version**: 1.0.0
- **Changelog**:
  - *2024-09-19*: Initial documentation creation.

## Feedback Mechanism
- **Submit Feedback**:
  - Users can submit feedback through the "Feedback" section in the UI or by contacting support at [support@example.com](mailto:support@example.com).
- **Suggestions**:
  - Suggestions for improvements or new features can be made via the project's GitHub repository issues page.

## Licensing Information
- **License**: MIT License
- **Terms**:
  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software...
