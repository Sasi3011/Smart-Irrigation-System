# Smart Irrigation System - Deployment Guide

This guide provides step-by-step instructions for deploying the Smart Irrigation System, with the backend on Render and the frontend on Vercel.

## Backend Deployment (Render)

1. **Create a Render Account**
   - Sign up at [render.com](https://render.com)

2. **Create a MongoDB Atlas Database**
   - Sign up at [mongodb.com/cloud/atlas](https://mongodb.com/cloud/atlas)
   - Create a new cluster (free tier is sufficient for starting)
   - Set up a database user with password
   - Get your connection string (will look like: `mongodb+srv://username:password@cluster.mongodb.net/irrigation_system`)

3. **Deploy to Render**
   - Go to your Render dashboard
   - Click "New" and select "Web Service"
   - Connect your GitHub/GitLab repository or use the manual deploy option
   - Configure the service:
     - Name: `smart-irrigation-backend` (or your preferred name)
     - Runtime: Python
     - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
     - Start Command: `gunicorn sis.wsgi:application`
   - Add the following environment variables:
     - `SECRET_KEY`: Generate a secure random string
     - `DEBUG`: Set to `False`
     - `MONGODB_URI`: Your MongoDB Atlas connection string
     - `OPENWEATHERMAP_API_KEY`: Your OpenWeatherMap API key
     - `ALLOWED_HOSTS`: Your Render domain (e.g., `smart-irrigation-backend.onrender.com`)

4. **Verify Deployment**
   - Once deployed, visit your backend URL (e.g., `https://smart-irrigation-backend.onrender.com`)
   - You should see a Django page or your API endpoints working

## Frontend Deployment (Vercel)

1. **Create a Vercel Account**
   - Sign up at [vercel.com](https://vercel.com)

2. **Deploy to Vercel**
   - Go to your Vercel dashboard
   - Click "New Project" and import your repository
   - Configure the project:
     - Framework Preset: Vite
     - Build Command: `npm run build`
     - Output Directory: `dist`
   - Add the following environment variable:
     - `VITE_API_BASE_URL`: Your Render backend URL (e.g., `https://smart-irrigation-backend.onrender.com`)
   - Click "Deploy"

3. **Verify Deployment**
   - Once deployed, visit your frontend URL (e.g., `https://smart-irrigation-system.vercel.app`)
   - Your application should be running and connecting to your backend

## Troubleshooting

### CORS Issues
If you encounter CORS issues, make sure your backend's `CORS_ALLOWED_ORIGINS` setting includes your Vercel frontend URL.

### MongoDB Connection Issues
- Verify your MongoDB Atlas connection string is correct
- Ensure your MongoDB Atlas IP access list allows connections from Render (you may need to allow all IPs: `0.0.0.0/0`)

### Static Files Issues
If static files aren't loading correctly, run `python manage.py collectstatic` locally and check that the files are being collected properly.

### API Connection Issues
- Check the browser console for any API errors
- Verify that the `VITE_API_BASE_URL` environment variable is set correctly in Vercel
- Make sure your API endpoints are working by testing them directly

## Updating Your Deployment

### Backend (Render)
- Push changes to your repository
- Render will automatically redeploy your application

### Frontend (Vercel)
- Push changes to your repository
- Vercel will automatically redeploy your application
