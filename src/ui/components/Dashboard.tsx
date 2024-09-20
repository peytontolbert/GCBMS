import React from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../store/store';

const Dashboard: React.FC = () => {
  const projects = useSelector((state: RootState) => state.project.projects);
  
  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      {/* Display projects, recent activities, and quick actions */}
      {/* ... */}
    </div>
  );
};

export default Dashboard;