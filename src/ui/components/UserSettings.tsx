import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store';
import { fetchUser, updateUserSettings } from '../store/slices/userSlice';

const UserSettings: React.FC = () => {
  const dispatch = useDispatch();
  const user = useSelector((state: RootState) => state.user);
  const [theme, setTheme] = useState<string>(user.settings.theme);
  const [email, setEmail] = useState<string>(user.email);
  const [username, setUsername] = useState<string>(user.username);

  useEffect(() => {
    if (user.status === 'idle') {
      dispatch(fetchUser());
    }
  }, [dispatch, user.status]);

  const handleThemeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setTheme(e.target.value);
    dispatch(updateUserSettings({ theme: e.target.value }));
  };

  const handleEmailChange = () => {
    dispatch(updateUserSettings({ email }));
  };

  const handleUsernameChange = () => {
    dispatch(updateUserSettings({ username }));
  };

  if (user.status === 'loading') {
    return <div>Loading user settings...</div>;
  }

  if (user.status === 'failed') {
    return <div>Error: {user.error}</div>;
  }

  return (
    <div className="user-settings">
      <h2>User Settings</h2>
      <div className="setting-item">
        <label htmlFor="theme-select">Theme:</label>
        <select id="theme-select" value={theme} onChange={handleThemeChange}>
          <option value="light">Light</option>
          <option value="vs-dark">Dark</option>
        </select>
      </div>
      <div className="setting-item">
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
        <button onClick={handleUsernameChange} className="btn">Update Username</button>
      </div>
      <div className="setting-item">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
        <button onClick={handleEmailChange} className="btn">Update Email</button>
      </div>
      {/* Add more settings as needed */}
    </div>
  );
};

export default UserSettings;