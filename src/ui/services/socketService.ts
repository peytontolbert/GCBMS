import io from 'socket.io-client';
import { receiveMessage } from '../store/slices/chatSlice';
import store from '../store/store';

const socket = io(process.env.REACT_APP_WEBSOCKET_URL || 'http://localhost:5000');

const socketService = {
  sendMessage: (msg: string) => {
    socket.emit('message', msg);
  },

  onMessage: (callback: (msg: string) => void) => {
    socket.on('message', (msg) => {
      callback(msg);
      store.dispatch(receiveMessage(msg));
    });
  },

  connect: () => {
    socket.connect();
  },

  disconnect: () => {
    socket.disconnect();
  }
};

export default socketService;