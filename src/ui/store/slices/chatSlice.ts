import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface ChatState {
  messages: { user: string; text: string }[];
}

const initialState: ChatState = {
  messages: [],
};

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    addMessage(state, action: PayloadAction<{ user: string; text: string }>) {
      state.messages.push(action.payload);
    },
    clearChat(state) {
      state.messages = [];
    },
  },
});

export const { addMessage, clearChat } = chatSlice.actions;
export default chatSlice.reducer;