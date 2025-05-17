# Smart Irrigation System - Deployment Checklist

Use this checklist to ensure all deployment steps are completed successfully.

## Pre-Deployment Preparation

### Backend
- [ ] Update `requirements.txt` with all necessary dependencies (gunicorn, whitenoise, etc.)
- [ ] Configure `settings.py` for production (DEBUG=False, proper ALLOWED_HOSTS)
- [ ] Set up CORS settings to allow your frontend domain
- [ ] Create a Procfile for Render
- [ ] Test MongoDB connection with production settings
- [ ] Collect static files (`python manage.py collectstatic`)

### Frontend
- [ ] Create environment files (.env.production)
- [ ] Update API endpoint configuration to use environment variables
- [ ] Create Vercel configuration file (vercel.json)
- [ ] Test build process locally (`npm run build`)
- [ ] Verify API connections work with the production backend URL

## Deployment Process

### Backend (Render)
- [ ] Create MongoDB Atlas database
- [ ] Set up MongoDB user and get connection string
- [ ] Create new Web Service on Render
- [ ] Configure build and start commands
- [ ] Set all required environment variables:
  - [ ] SECRET_KEY
  - [ ] DEBUG=False
  - [ ] MONGODB_URI
  - [ ] OPENWEATHERMAP_API_KEY
  - [ ] ALLOWED_HOSTS
- [ ] Deploy and verify the application is running
- [ ] Test API endpoints using a tool like Postman

### Frontend (Vercel)
- [ ] Create new project on Vercel
- [ ] Configure build settings
- [ ] Set VITE_API_BASE_URL environment variable
- [ ] Deploy and verify the application is running
- [ ] Test connection to backend APIs

## Post-Deployment Verification

- [ ] Verify all frontend features work with the deployed backend
- [ ] Check for any CORS errors in the browser console
- [ ] Ensure MongoDB connection is working properly
- [ ] Verify authentication flows work correctly
- [ ] Test all major features of the application
- [ ] Check mobile responsiveness

## Common Issues and Solutions

### CORS Issues
- Solution: Verify CORS settings in backend settings.py

### MongoDB Connection Issues
- Solution: Check MongoDB Atlas network access settings

### Static Files Not Loading
- Solution: Verify whitenoise configuration and run collectstatic

### API Endpoint Issues
- Solution: Check environment variables and API URL configuration
