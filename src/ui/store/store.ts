import { configureStore } from '@reduxjs/toolkit';
import chatReducer from './slices/chatSlice';
import projectReducer from './slices/projectSlice';
import graphReducer from './slices/graphSlice';
import logsReducer from './slices/logsSlice';
import userReducer from './slices/userSlice';
// ... import other reducers

const store = configureStore({
  reducer: {
    chat: chatReducer,
    project: projectReducer,
    graph: graphReducer,
    logs: logsReducer,
    user: userReducer,
    // ... add other reducers here
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;