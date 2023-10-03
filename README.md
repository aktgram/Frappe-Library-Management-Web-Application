# Frappe-Library-Management-Web-Application

**Run in order:**

## Database (AWS)
URL: http://16.16.156.1:5050 (no https)
```
cd database
```
```
docker-compose up --build
```

## Backend (AWS)
URL https://16.16.156.1
```
cd backend
```
```
pip install -r requirements.txt
```
```
flask db upgrade
```
```
flask run
```
## Frontend (Netlify)
URL https://frappe-library.netlify.app
```
npm install
```
```
npm run dev
```
