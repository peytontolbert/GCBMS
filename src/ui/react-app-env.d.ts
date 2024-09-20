/// <reference types="react-scripts" />

// Declare global environment variables
declare namespace NodeJS {
  interface ProcessEnv {
    REACT_APP_API_BASE_URL: string; // Base URL for API requests
    REACT_APP_WEBSOCKET_URL: string; // WebSocket URL for real-time communication
  }
}

// Declare module for any non-TypeScript modules you're using
declare module 'react-cytoscapejs'; // Cytoscape.js integration

// Add any other custom type declarations here
interface Project {
  id: string; // Unique identifier for the project
  name: string; // Name of the project
  files: File[]; // Array of files associated with the project
}

interface File {
  id: string; // Unique identifier for the file
  path: string; // Path of the file in the project
  content: string; // Content of the file
  project_id: string; // ID of the project the file belongs to
}

interface ChatMessage {
  id: string; // Unique identifier for the chat message
  content: string; // Content of the message
  sender: 'user' | 'agent'; // Sender of the message
  timestamp: string; // Timestamp of when the message was sent
}

// Add more interfaces or type declarations as needed
