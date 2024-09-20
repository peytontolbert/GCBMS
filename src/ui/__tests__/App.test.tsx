import React from 'react';
import { render, screen } from '@testing-library/react';
import { Provider } from 'react-redux';
import store from '../store/store';
import App from '../App';

test('renders app with header and footer', () => {
  render(
    <Provider store={store}>
      <App />
    </Provider>
  );
  
  const headerElement = screen.getByText(/GBCMS Web UI/i);
  expect(headerElement).toBeInTheDocument();
  
  const footerElement = screen.getByText(/© 2024 GBCMS/i);
  expect(footerElement).toBeInTheDocument();
});