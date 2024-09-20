import { createSlice, PayloadAction, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

interface Project {
  id: string;
  name: string;
  description: string;
  created_at: string;
  updated_at: string;
  // ... other project attributes
}

interface ProjectState {
  projects: Project[];
  currentFile: {
    id: string;
    content: string;
    // ... other file attributes
  } | null;
  // ... other project-related state
}

const initialState: ProjectState = {
  projects: [],
  currentFile: null,
};

export const fetchProjects = createAsyncThunk(
  'project/fetchProjects',
  async (_, { rejectWithValue }) => {
    try {
      const response = await axios.get('/api/projects');
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

const projectSlice = createSlice({
  name: 'project',
  initialState,
  reducers: {
    addProject(state, action: PayloadAction<Project>) {
      state.projects.push(action.payload);
    },
    setCurrentFile(state, action: PayloadAction<{ id: string; content: string }>) {
      state.currentFile = action.payload;
    },
    // ... other project-related reducers
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchProjects.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchProjects.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.projects = action.payload;
      })
      .addCase(fetchProjects.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.payload;
      });
  },
});

export const { addProject, setCurrentFile } = projectSlice.actions;
export default projectSlice.reducer;