import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/api', // Update with your Flask backend URL
});

// Add authentication token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const getProfile = async () => {
  const response = await api.get('/user/profile');
  return response.data;
};

export const updateProfile = async (username, email) => {
  const response = await api.put('/user/profile', { username, email });
  return response.data;
};

export const connectDEXAccount = async (exchangeName, apiKey, apiSecret) => {
  const response = await api.post('/dex/connect', {
    exchange_name: exchangeName,
    api_key: apiKey,
    api_secret: apiSecret,
  });
  return response.data;
};

export const getDEXAccounts = async () => {
  const response = await api.get('/dex/accounts');
  return response.data;
};

export const getDEXBalances = async () => {
  const response = await api.get('/dex/balances');
  return response.data;
};

export const getArbitrageOpportunities = async () => {
  const response = await api.get('/arbitrage/opportunities');
  return response.data;
};
