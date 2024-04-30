import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/api', // Update with your Flask backend URL
});

export const login = async (username, password) => {
  const response = await api.post('/auth/login', { username, password });
  localStorage.setItem('token', response.data.access_token);
  return response.data;
};

export const register = async (username, email, password) => {
  const response = await api.post('/auth/register', {
    username,
    email,
    password,
  });
  return response.data;
};

export const logout = () => {
  localStorage.removeItem('token');
};