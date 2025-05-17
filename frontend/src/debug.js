// Debug utility to help troubleshoot deployment issues
const DEBUG = {
  enabled: true,
  
  // Log API base URL and environment variables
  logConfig: () => {
    if (!DEBUG.enabled) return;
    
    console.log('=== DEBUG INFO ===');
    console.log('API Base URL:', import.meta.env.VITE_API_BASE_URL || 'Not set');
    console.log('Environment:', import.meta.env.MODE);
    console.log('All env vars:', import.meta.env);
    console.log('=================');
  },
  
  // Log API requests
  logApiRequest: (method, url, data) => {
    if (!DEBUG.enabled) return;
    
    console.log(`API ${method}:`, url);
    if (data) console.log('Request data:', data);
  },
  
  // Log API responses
  logApiResponse: (url, response, error) => {
    if (!DEBUG.enabled) return;
    
    if (error) {
      console.error(`API Error (${url}):`, error);
    } else {
      console.log(`API Response (${url}):`, response);
    }
  }
};

export default DEBUG;
