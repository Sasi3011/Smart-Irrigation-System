@echo off
echo Starting Smart Irrigation System...

echo Starting Backend Server...
start cmd /k "cd backend && python manage.py runserver"

echo Starting Frontend Server...
start cmd /k "cd frontend && npm run dev"

echo Smart Irrigation System is now running!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
