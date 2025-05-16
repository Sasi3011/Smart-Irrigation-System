# Smart Irrigation System

A web-based application for managing and automating irrigation systems based on environmental data.

## Project Structure

The project is organized into two main components:

- **Backend**: Django-based API server
- **Frontend**: React-based web application

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create and activate a virtual environment (optional if already done):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.template` to `.env`
   - Update the values in `.env` as needed

5. Run the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```

## Usage

Access the web application at http://localhost:5173 when both backend and frontend servers are running.
