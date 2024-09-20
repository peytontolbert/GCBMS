import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="header">
      <h1>GBCMS Web UI</h1>
      <nav>
        <ul>
          <li><Link to="/">Dashboard</Link></li>
          <li><Link to="/graph">Graph Viewer</Link></li>
          <li><Link to="/projects">Project Manager</Link></li>
          <li><Link to="/chat">Chat Interface</Link></li>
          <li><Link to="/logs">Log Viewer</Link></li>
          <li><Link to="/settings">User Settings</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;