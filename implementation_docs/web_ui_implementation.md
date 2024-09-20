# Web User Interface (UI) Module Implementation

## Overview

This document provides a detailed implementation guide for the Web User Interface (UI) Module of the Graph-Based Codebase Management System (GBCMS). The goal is to ensure that an automated agent can generate the module in its entirety based on this documentation. The UI is built using React.js with TypeScript, interfacing with a Flask backend via RESTful APIs and WebSockets.

## Technology Stack

- **Frontend:**
  - **React.js** with **TypeScript** (`.tsx` files)
  - **Redux Toolkit** for state management
  - **Cytoscape.js** for graph rendering
  - **Monaco Editor** for code editing
  - **Axios** for HTTP requests
  - **WebSockets** for real-time communication

- **Backend:**
  - **Flask** as the web server
  - **Flask-CORS** for handling Cross-Origin Resource Sharing
  - **Flask-SocketIO** for WebSocket support

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
├── services/
│ ├── apiService.ts
│ └── socketService.ts
├── utils/
│ └── helpers.ts
├── styles.css
├── App.tsx
├── index.tsx
└── react-app-env.d.ts
```

## Components Implementation

### 1. Header.tsx

Handles the navigation bar and branding.
```
typescript:src/components/Header.tsx
import React from 'react';
import { Link } from 'react-router-dom';
const Header: React.FC = () => (
<header className="header">
<h1>GBCMS</h1>
<nav>
<Link to="/">Dashboard</Link>
<Link to="/projects">Projects</Link>
<Link to="/settings">Settings</Link>
</nav>
</header>
);
export default Header;
```

### 2. Dashboard.tsx

Displays an overview of projects and recent activities.
typescript:src/components/Dashboard.tsx
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchProjects } from '../store/slices/projectSlice';
import { RootState } from '../store/store';
const Dashboard: React.FC = () => {
const dispatch = useDispatch();
const projects = useSelector((state: RootState) => state.project.projects);
useEffect(() => {
dispatch(fetchProjects());
}, [dispatch]);
return (
<div className="dashboard">
<h2>Projects Overview</h2>
<ul>
{projects.map(project => (
<li key={project.id}>{project.name}</li>
))}
</ul>
</div>
);
};
export default Dashboard;


### 3. GraphViewer.tsx

Renders the interactive codebase graph.
```
typescript:src/components/GraphViewer.tsx
import React, { useEffect } from 'react';
import CytoscapeComponent from 'react-cytoscapejs';
import { useSelector, useDispatch } from 'react-redux';
import { RootState } from '../store/store';
import { selectNode } from '../store/slices/graphSlice';
const GraphViewer: React.FC = () => {
const dispatch = useDispatch();
const graphData = useSelector((state: RootState) => state.graph.data);
const handleClick = (event: any) => {
const nodeId = event.target.id();
dispatch(selectNode(nodeId));
};
return (
<div className="graph-viewer">
<CytoscapeComponent
elements={graphData.elements}
style={{ width: '600px', height: '600px' }}
layout={{ name: 'cose' }}
stylesheet={graphData.styles}
cy={(cy) => {
cy.on('tap', 'node', handleClick);
}}
/>
</div>
);
};
export default GraphViewer;
```

### 4. CodeEditor.tsx

Integrates the Monaco Editor for code viewing and editing.
```
typescript:src/components/CodeEditor.tsx
import React from 'react';
import MonacoEditor from '@monaco-editor/react';
import { useSelector, useDispatch } from 'react-redux';
import { RootState } from '../store/store';
import { updateCodeContent } from '../store/slices/projectSlice';
import axios from 'axios';
const CodeEditor: React.FC = () => {
const dispatch = useDispatch();
const selectedFile = useSelector((state: RootState) => state.project.selectedFile);
const codeContent = selectedFile.content;
const handleEditorChange = (value: string | undefined) => {
if (value !== undefined) {
dispatch(updateCodeContent(value));
}
};
const handleSave = async () => {
try {
const response = await axios.post(/api/projects/${selectedFile.project_id}/files/${selectedFile.id}/save, {
content: codeContent,
});
console.log(response.data.message);
} catch (error) {
console.error('Error saving file:', error);
}
};
return (
<div className="code-editor">
<MonacoEditor
height="500px"
language="python"
value={codeContent}
onChange={handleEditorChange}
theme="vs-dark"
/>
<button onClick={handleSave}>Save</button>
</div>
);
};
export default CodeEditor;
```

### 5. ChatInterface.tsx

Enables real-time communication with the LLM Agent via WebSocket.
```
typescript:src/components/ChatInterface.tsx
import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store/store';
import { sendMessage, receiveMessage } from '../store/slices/chatSlice';
import socketService from '../services/socketService';
const ChatInterface: React.FC = () => {
const dispatch = useDispatch();
const messages = useSelector((state: RootState) => state.chat.messages);
const [input, setInput] = useState('');
useEffect(() => {
socketService.onMessage((msg: string) => {
dispatch(receiveMessage(msg));
});
}, [dispatch]);
const handleSend = () => {
if (input.trim() !== '') {
dispatch(sendMessage(input));
socketService.sendMessage(input);
setInput('');
}
};
return (
<div className="chat-interface">
<div className="messages">
{messages.map((msg, idx) => (
<div key={idx} className={message ${msg.sender}}>
<span>{msg.content}</span>
</div>
))}
</div>
<input
type="text"
value={input}
onChange={(e) => setInput(e.target.value)}
placeholder="Type your message..."
/>
<button onClick={handleSend}>Send</button>
</div>
);
};
export default ChatInterface;
```

### 6. ProjectManager.tsx

Facilitates project creation, import, and management.
```
typescript:src/components/ProjectManager.tsx
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { createProject, importProject } from '../store/slices/projectSlice';
import axios from 'axios';
const ProjectManager: React.FC = () => {
const dispatch = useDispatch();
const [projectName, setProjectName] = useState('');
const [importFile, setImportFile] = useState<File | null>(null);
const handleCreate = () => {
if (projectName.trim() !== '') {
dispatch(createProject({ name: projectName }));
setProjectName('');
}
};
const handleImport = async () => {
if (importFile) {
const formData = new FormData();
formData.append('file', importFile);
try {
const response = await axios.post('/api/projects/import', formData);
dispatch(importProject(response.data.project));
setImportFile(null);
} catch (error) {
console.error('Error importing project:', error);
}
}
};
return (
<div className="project-manager">
<h3>Create New Project</h3>
<input
type="text"
value={projectName}
onChange={(e) => setProjectName(e.target.value)}
placeholder="Project Name"
/>
<button onClick={handleCreate}>Create</button>
<h3>Import Existing Project</h3>
<input
type="file"
onChange={(e) => setImportFile(e.target.files ? e.target.files[0] : null)}
/>
<button onClick={handleImport}>Import</button>
</div>
);
};
export default ProjectManager;
```

## Redux Slices

### 1. projectSlice.ts

Manages project-related state and actions.
```
typescript:src/store/slices/projectSlice.ts
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';
interface File {
id: string;
path: string;
content: string;
project_id: string;
}
interface Project {
id: string;
name: string;
files: File[];
}
interface ProjectState {
projects: Project[];
selectedProject: Project | null;
selectedFile: File | null;
}
const initialState: ProjectState = {
projects: [],
selectedProject: null,
selectedFile: null,
};
export const fetchProjects = createAsyncThunk('project/fetchProjects', async () => {
const response = await axios.get('/api/projects');
return response.data.projects;
});
export const createProject = createAsyncThunk('project/createProject', async (projectData: { name: string }) => {
const response = await axios.post('/api/projects', projectData);
return response.data.project;
});
export const importProject = createAsyncThunk('project/importProject', async (project: Project) => {
return project;
});
const projectSlice = createSlice({
name: 'project',
initialState,
reducers: {
selectFile(state, action) {
const fileId = action.payload;
const file = state.selectedProject?.files.find(f => f.id === fileId) || null;
state.selectedFile = file;
},
updateCodeContent(state, action) {
if (state.selectedFile) {
state.selectedFile.content = action.payload;
}
},
},
extraReducers: (builder) => {
builder
.addCase(fetchProjects.fulfilled, (state, action) => {
state.projects = action.payload;
})
.addCase(createProject.fulfilled, (state, action) => {
state.projects.push(action.payload);
})
.addCase(importProject.fulfilled, (state, action) => {
state.projects.push(action.payload);
});
},
});
export const { selectFile, updateCodeContent } = projectSlice.actions;
export default projectSlice.reducer;
```

## Services

### 1. apiService.ts

Handles HTTP requests to the backend APIs.
```
typescript:src/services/apiService.ts
import axios from 'axios';
const apiService = axios.create({
baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api',
headers: {
'Content-Type': 'application/json',
},
});
export default apiService;
```

### 2. socketService.ts

Manages WebSocket connections for real-time features.
```
typescript:src/services/socketService.ts
import io from 'socket.io-client';
const socket = io(process.env.REACT_APP_WEBSOCKET_URL || 'http://localhost:5000');
const socketService = {
sendMessage: (msg: string) => {
socket.emit('message', msg);
},
onMessage: (callback: (msg: string) => void) => {
socket.on('message', callback);
},
};
export default socketService;
```

## Utilities

### helpers.ts

Contains helper functions used across the UI.
```
typescript:src/utils/helpers.ts
export const formatDate = (dateString: string): string => {
const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'short', day: 'numeric' };
return new Date(dateString).toLocaleDateString(undefined, options);
};
```

## State Management

Utilizes **Redux Toolkit** for managing the application state. The store is configured in `store/store.ts` and combines various slices.
```
typescript:src/store/store.ts
import { configureStore } from '@reduxjs/toolkit';
import projectReducer from './slices/projectSlice';
import chatReducer from './slices/chatSlice';
import graphReducer from './slices/graphSlice';
import logsReducer from './slices/logsSlice';
import userReducer from './slices/userSlice';
const store = configureStore({
reducer: {
project: projectReducer,
chat: chatReducer,
graph: graphReducer,
logs: logsReducer,
user: userReducer,
},
});
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export default store;
```

## Backend Integration

The Flask backend serves as the API provider and handles WebSocket connections.

### Flask Setup
```
python:main.py
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
app = Flask(name)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="")
@socketio.on('message')
def handle_message(msg):
# Process the message and generate a response
response = generate_response(msg)
socketio.emit('message', response)
def generate_response(message):
# Integrate with LLM Agent to generate a response
return "Response from LLM Agent"
if name == 'main':
socketio.run(app, host='0.0.0.0', port=5000)
```

## Deployment Considerations

- **Frontend:** Deploy the React application separately using platforms like Netlify or Vercel.
- **Backend:** Host the Flask server on platforms like Heroku, AWS, or DigitalOcean.
- **Environment Variables:** Ensure that the frontend knows the correct API and WebSocket URLs based on the deployment environment.

## Conclusion

This implementation guide provides a comprehensive overview of the Web UI Module for GBCMS. By following this documentation, an automated agent can generate the necessary components, services, and state management configurations to build a fully functional frontend interfacing seamlessly with the Flask backend.