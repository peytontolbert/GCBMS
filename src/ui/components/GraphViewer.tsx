import React, { useEffect } from 'react';
import CytoscapeComponent from 'react-cytoscapejs';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store/store';
// ... import necessary actions

const GraphViewer: React.FC = () => {
  const dispatch = useDispatch();
  const graphData = useSelector((state: RootState) => state.graph.data);

  useEffect(() => {
    // Fetch graph data from API
    // dispatch(fetchGraphData());
  }, [dispatch]);

  return (
    <div className="graph-viewer">
      <CytoscapeComponent elements={graphData.elements} style={{ width: '800px', height: '600px' }} />
    </div>
  );
};

export default GraphViewer;