# GBCMS Web User Interface (UI) Module

## Overview

The Web User Interface (UI) Module is a crucial component of the Graph-Based Codebase Management System (GBCMS). It provides users with an interactive and user-friendly interface to visualize the codebase, edit code, manage projects, communicate with the LLM Agent, and access system logs. Built with React.js and TypeScript, the module emphasizes scalability, responsiveness, and extensibility.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Available Scripts](#available-scripts)
- [Project Structure](#project-structure)
- [State Management](#state-management)
- [Components Overview](#components-overview)
- [API Integration](#api-integration)
- [Styling](#styling)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/gbcms-ui.git
   cd gbcms-ui
   ```

2. **Install Dependencies:**

   Using npm:
   ```bash
   npm install
   ```

   Or using yarn:
   ```bash
   yarn install
   ```

## Configuration

1. **Environment Variables:**

   Create a `.env` file in the `src/ui/` directory and define the necessary environment variables:

   ```env
   REACT_APP_API_BASE_URL=https://api.yourdomain.com
   REACT_APP_WEBSOCKET_URL=wss://ws.yourdomain.com/chat
   ```

2. **API Endpoints:**

   Ensure that the backend APIs are running and the endpoints match those defined in the documentation.

## Available Scripts

In the project directory, you can run:

- **Start the Development Server:**
  
  ```bash
  npm start
  ```
  
  or
  
  ```bash
  yarn start
  ```

- **Build for Production:**
  
  ```bash
  npm run build
  ```
  
  or
  
  ```bash
  yarn build
  ```

- **Run Tests:**
  
  ```bash
  npm test
  ```
  
  or
  
  ```bash
  yarn test
  ```

## Project Structure
```
src/
├── components/
│ ├── ChatInterface.tsx
│ ├── CodeEditor.tsx
│ ├── Dashboard.tsx
│ ├── Footer.tsx
│ ├── GraphViewer.tsx
│ ├── Header.tsx
│ ├── LogViewer.tsx
│ ├── ProjectManager.tsx
│ └── UserSettings.tsx
├── store/
│ ├── slices/
│ │ ├── chatSlice.ts
│ │ ├── graphSlice.ts
│ │ ├── logsSlice.ts
│ │ ├── projectSlice.ts
│ │ └── userSlice.ts
│ └── store.ts
├── styles.css
├── App.tsx
└── index.tsx
```


## State Management

The application utilizes **Redux Toolkit** for state management, ensuring a predictable and scalable state container. The `store` is configured in `store/store.ts` and integrates various slices responsible for different parts of the state.

### Available Slices:

- **chatSlice:** Manages chat messages and WebSocket connections.
- **projectSlice:** Handles project data and related actions.
- **graphSlice:** Manages graph visualization data.
- **logsSlice:** Oversees system and agent logs.
- **userSlice:** Handles user information and settings.

## Components Overview

### 1. **Header**

- **Path:** `src/ui/components/Header.tsx`
- **Description:** Contains the navigation links and branding for the application.

### 2. **Footer**

- **Path:** `src/ui/components/Footer.tsx`
- **Description:** Displays footer information such as copyright.

### 3. **Dashboard**

- **Path:** `src/ui/components/Dashboard.tsx`
- **Description:** Provides an overview of projects, recent activities, and quick actions.

### 4. **GraphViewer**

- **Path:** `src/ui/components/GraphViewer.tsx`
- **Description:** Renders the interactive codebase graph using Cytoscape.js.

### 5. **CodeEditor**

- **Path:** `src/ui/components/CodeEditor.tsx`
- **Description:** Integrates the Monaco Editor for code viewing and editing.

### 6. **ChatInterface**

- **Path:** `src/ui/components/ChatInterface.tsx`
- **Description:** Enables real-time communication with the LLM Agent via WebSocket.

### 7. **LogViewer**

- **Path:** `src/ui/components/LogViewer.tsx`
- **Description:** Displays system and agent logs in a tabular format.

### 8. **ProjectManager**

- **Path:** `src/ui/components/ProjectManager.tsx`
- **Description:** Facilitates project creation, import, and management.

### 9. **UserSettings**

- **Path:** `src/ui/components/UserSettings.tsx`
- **Description:** Allows users to customize preferences such as theme, username, and email.

## API Integration

The UI communicates with the backend APIs to perform CRUD operations, fetch data, and handle real-time interactions. **Axios** is used for HTTP requests, and **WebSockets** manage real-time chat communications.

### Key Endpoints:

- **Fetch Projects:** `GET /api/projects`
- **Create Project:** `POST /api/projects`
- **Import Project:** `POST /api/projects/import`
- **Fetch Logs:** `GET /api/logs`
- **Fetch User:** `GET /api/user`
- **Update User Settings:** `PUT /api/user`
- **Chat WebSocket:** `wss://ws.yourdomain.com/chat`

## Styling

Basic styling is handled via `styles.css` in the `src/ui/` directory. The styles ensure a consistent look and feel across all components, emphasizing responsiveness and user experience.

## Testing

Testing strategies include:

- **Unit Tests:** For individual components and Redux slices.
- **Integration Tests:** To verify interactions between components and the store.
- **End-to-End (E2E) Tests:** Simulating user workflows using tools like Cypress.

Run tests using:

bash
```
npm test
```

or

bash
```
yarn test
```

## Deployment

1. **Build the Application:**

   ```bash
   npm run build
   ```

   or

   ```bash
   yarn build
   ```

2. **Deploy to a Static Hosting Service:**

   Deploy the `build` directory to services like **Netlify**, **Vercel**, or **GitHub Pages**.

3. **Containerization (Optional):**

   Use Docker to containerize the frontend for consistent deployments.

   ```dockerfile
   # Dockerfile
   FROM node:14-alpine
   WORKDIR /app
   COPY package.json yarn.lock ./
   RUN yarn install --frozen-lockfile
   COPY . .
   RUN yarn build
   CMD ["yarn", "start"]
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -m "Add YourFeature"
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

---