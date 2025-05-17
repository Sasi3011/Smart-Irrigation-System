// API configuration utility
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

// Log the API base URL for debugging
console.log('API Base URL configured as:', API_BASE_URL);

// Export the base URL for use in components
export const getApiBaseUrl = () => {
  console.log('getApiBaseUrl called, returning:', API_BASE_URL);
  return API_BASE_URL;
};

// Helper function to construct API endpoints
export const getApiUrl = (endpoint) => {
  // Remove leading slash if present
  const cleanEndpoint = endpoint.startsWith('/') ? endpoint.substring(1) : endpoint;
  const fullUrl = `${API_BASE_URL}/${cleanEndpoint}`;
  console.log(`API URL constructed: ${fullUrl} (from endpoint: ${endpoint})`);
  return fullUrl;
};

// Example usage of API functions
export const API = {
  // Authentication endpoints
  login: () => getApiUrl('api/auth/login/'),
  logout: () => getApiUrl('api/auth/logout/'),
  
  // Data endpoints
  fields: () => getApiUrl('api/fields/'),
  field: (id) => getApiUrl(`api/fields/${id}/`),
  sensorData: (fieldId) => getApiUrl(`api/fields/${fieldId}/sensor-data/`),
  weather: (location) => getApiUrl(`api/weather/?location=${encodeURIComponent(location)}`),
  irrigationSchedule: (fieldId) => getApiUrl(`api/fields/${fieldId}/irrigation-schedule/`),
  cropSoilData: () => getApiUrl('api/crop-soil-data/'),
};

export default API;
