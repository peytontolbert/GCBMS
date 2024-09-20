import { addMessage } from '../store/slices/chatSlice';
import store from '../store/store';

const WEBSOCKET_URL = process.env.REACT_APP_WEBSOCKET_URL || 'ws://localhost:3000/ws';

class WebSocketService {
  private socket: WebSocket | null = null;

  connect() {
    this.socket = new WebSocket(WEBSOCKET_URL);

    this.socket.onopen = () => {
      console.log('WebSocket connected');
    };

    this.socket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      store.dispatch(addMessage(message));
    };

    this.socket.onclose = () => {
      console.log('WebSocket disconnected');
      // Implement reconnection logic here
    };
  }

  sendMessage(message: string) {
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify({ message }));
    } else {
      console.error('WebSocket is not connected');
    }
  }

  disconnect() {
    if (this.socket) {
      this.socket.close();
    }
  }
}

export default new WebSocketService();