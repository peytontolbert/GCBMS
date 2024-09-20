import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store';
import { fetchLogs } from '../store/slices/logsSlice';

const LogViewer: React.FC = () => {
  const dispatch = useDispatch();
  const logs = useSelector((state: RootState) => state.logs.entries);
  const logStatus = useSelector((state: RootState) => state.logs.status);
  const logError = useSelector((state: RootState) => state.logs.error);

  useEffect(() => {
    if (logStatus === 'idle') {
      dispatch(fetchLogs());
    }
  }, [dispatch, logStatus]);

  if (logStatus === 'loading') {
    return <div>Loading logs...</div>;
  }

  if (logStatus === 'failed') {
    return <div>Error: {logError}</div>;
  }

  return (
    <div className="log-viewer">
      <h2>Log Viewer</h2>
      <table className="log-table">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>User</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {logs.map(log => (
            <tr key={log.id}>
              <td>{new Date(log.timestamp).toLocaleString()}</td>
              <td>{log.user}</td>
              <td>{log.action}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LogViewer;