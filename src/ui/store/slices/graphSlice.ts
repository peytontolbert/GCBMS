import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface GraphState {
  data: any; // Replace `any` with appropriate type
}

const initialState: GraphState = {
  data: {},
};

const graphSlice = createSlice({
  name: 'graph',
  initialState,
  reducers: {
    setGraphData(state, action: PayloadAction<any>) { // Replace `any` with appropriate type
      state.data = action.payload;
    },
    // ... other graph-related reducers
  },
});

export const { setGraphData } = graphSlice.actions;
export default graphSlice.reducer;