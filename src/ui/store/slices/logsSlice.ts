import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface LogEntry {
  id: string;
  user_id: string;
  action: string;
  timestamp: string;
}

interface LogsState {
  entries: LogEntry[];
}

const initialState: LogsState = {
  entries: [],
};

const logsSlice = createSlice({
  name: 'logs',
  initialState,
  reducers: {
    addLogEntry(state, action: PayloadAction<LogEntry>) {
      state.entries.push(action.payload);
    },
    clearLogs(state) {
      state.entries = [];
    },
    // ... other log-related reducers
  },
});

export const { addLogEntry, clearLogs } = logsSlice.actions;
export default logsSlice.reducer;