# Frappe-Library-Management-Web-Application

### Problem statement [link](https://frappe.io/dev-hiring-test)

## Data Design:
![DataDesign](./design/data_design_frappe_library.png)

## Running locally:
**Run in order:**

### Database (AWS)
- URL: http://16.16.156.1:5050 (no https) (pgadmin)
- Username: ``` admin@example.com ```
- Password: ``` admin ```
```
cd database
```
```
docker-compose up --build
```

### Backend (AWS)
- URL https://16.16.156.1 (with https)
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
### Frontend (Netlify)
- URL https://frappe-library.netlify.app
- Add ```PUBLIC_API_URL``` env variable for backend url
```
npm install
```
```
npm run dev
```
