import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store';
import { fetchProjects, createProject, importProject } from '../store/slices/projectsSlice';
import { useHistory } from 'react-router-dom';

const ProjectManager: React.FC = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const projects = useSelector((state: RootState) => state.projects.list);
  const projectStatus = useSelector((state: RootState) => state.projects.status);
  const projectError = useSelector((state: RootState) => state.projects.error);
  const [newProjectName, setNewProjectName] = useState<string>('');

  useEffect(() => {
    if (projectStatus === 'idle') {
      dispatch(fetchProjects());
    }
  }, [dispatch, projectStatus]);

  const handleCreate = () => {
    if (newProjectName.trim() !== '') {
      dispatch(createProject({ name: newProjectName }));
      setNewProjectName('');
    }
  };

  const handleImport = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      dispatch(importProject(file));
    }
  };

  if (projectStatus === 'loading') {
    return <div>Loading projects...</div>;
  }

  if (projectStatus === 'failed') {
    return <div>Error: {projectError}</div>;
  }

  return (
    <div className="project-manager">
      <h2>Project Manager</h2>
      <div className="create-project">
        <input
          type="text"
          placeholder="New Project Name"
          value={newProjectName}
          onChange={e => setNewProjectName(e.target.value)}
        />
        <button onClick={handleCreate} className="btn">Create Project</button>
      </div>
      <div className="import-project">
        <input type="file" accept=".zip,.tar.gz" onChange={handleImport} />
        <button className="btn">Import Existing Project</button>
      </div>
      <h3>Existing Projects</h3>
      <ul>
        {projects.map(project => (
          <li key={project.id}>
            <strong>{project.name}</strong> - {project.description}
            <button onClick={() => history.push(`/projects/${project.id}`)} className="btn view-btn">View</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectManager;