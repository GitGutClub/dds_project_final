# Frontend (React)

## Docker (production build served by nginx)
From repo root:
  docker-compose up --build
Frontend will be available at http://localhost:3000 (nginx maps to port 3000).

## Local development
1. cd frontend
2. npm install
3. npm start
The dev server runs on port 3000 and proxies /api requests to backend at http://localhost:8000/api (CORS must be configured).
