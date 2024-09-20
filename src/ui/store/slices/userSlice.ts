import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface UserState {
  id: string;
  username: string;
  email: string;
  role: string;
  theme: string;
  // ... other user attributes
}

const initialState: UserState = {
  id: '',
  username: '',
  email: '',
  role: 'Viewer',
  theme: 'light',
  // ... initialize other attributes
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setUser(state, action: PayloadAction<UserState>) {
      return action.payload;
    },
    updateTheme(state, action: PayloadAction<string>) {
      state.theme = action.payload;
    },
    // ... other user-related reducers
  },
});

export const { setUser, updateTheme } = userSlice.actions;
export default userSlice.reducer;