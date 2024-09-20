import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store';
import { sendMessage, receiveMessage, connectWebSocket } from '../store/slices/chatSlice';

const ChatInterface: React.FC = () => {
  const dispatch = useDispatch();
  const messages = useSelector((state: RootState) => state.chat.messages);
  const socketStatus = useSelector((state: RootState) => state.chat.status);
  const [input, setInput] = useState<string>('');

  useEffect(() => {
    dispatch(connectWebSocket());
  }, [dispatch]);

  const handleSend = () => {
    if (input.trim() !== '') {
      dispatch(sendMessage(input));
      setInput('');
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div className="chat-interface">
      <h2>Chat with LLM Agent</h2>
      <div className="chat-messages">
        {messages.map(msg => (
          <div key={msg.id} className={`message ${msg.sender}`}>
            <span>{msg.content}</span>
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          type="text"
          placeholder="Type your message..."
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <button onClick={handleSend} className="btn send-btn">Send</button>
      </div>
      <div className="socket-status">
        Status: {socketStatus}
      </div>
    </div>
  );
};

export default ChatInterface;