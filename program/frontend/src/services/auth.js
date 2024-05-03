import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/api', // Update with your Flask backend URL
});

export const login = async (username, password) => {
  try {
    const { data } = await api.post('/auth/login', { username, password });
    localStorage.setItem('token', data.access_token);
    return data;
  } catch (error) {
    console.error('Error during login:', error);
    throw error; // Rethrow the error for further handling
  }
};

export const register = async (username, email, password) => {
  try {
    const { data } = await api.post('/auth/register', { username, email, password });
    return data;
  } catch (error) {
    console.error('Error during registration:', error);
    throw error; // Rethrow the error for further handling
  }
};

export const logout = () => {
  localStorage.removeItem('token');
};