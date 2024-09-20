import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Dashboard from './components/Dashboard';
import GraphViewer from './components/GraphViewer';
import CodeEditor from './components/CodeEditor';
import ChatInterface from './components/ChatInterface';
import LogViewer from './components/LogViewer';
import ProjectManager from './components/ProjectManager';
import UserSettings from './components/UserSettings';

const App: React.FC = () => {
  return (
    <Router>
      <div className="app-container">
        <Header />
        <main>
          <Switch>
            <Route exact path="/" component={Dashboard} />
            <Route path="/graph" component={GraphViewer} />
            <Route path="/editor" component={CodeEditor} />
            <Route path="/chat" component={ChatInterface} />
            <Route path="/logs" component={LogViewer} />
            <Route path="/projects" component={ProjectManager} />
            <Route path="/settings" component={UserSettings} />
          </Switch>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;