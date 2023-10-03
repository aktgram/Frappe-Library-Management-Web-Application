# Frappe-Library-Management-Web-Application

### Problem statement [link](https://frappe.io/dev-hiring-test)

## Demo
- [Import Books, Update Book Stock](https://drive.google.com/file/d/1rJ_PQPSNiqn2awgdrPoMUq1lCQzb0DgI/view?usp=drive_link)
- [Search Books with Debouncing Instant search](https://drive.google.com/file/d/1Va9UcHdcHfkA7yQaFgu0QAqFfI_OIpGk/view?usp=drive_link)
- [Return Book](https://drive.google.com/file/d/1KDdcnCfVAyCQvoRiVLpLb8ylBJktd0j3/view?usp=drive_link)
- [₹500 debt exceed alert, Transaction details, Issue Book](https://drive.google.com/file/d/1iHlh1ELe4dMRu_it9GqnIayyof1d144a/view?usp=drive_link)
- [Members CRUD](https://drive.google.com/file/d/1vSJ39V_SO_Njomr2wELoyEBGKnRxdyV5/view?usp=drive_link)

## Data Design:
![DataDesign](./design/data_design_frappe_library.png)

## Running locally:
**Run in order:**

### Database
```
cd database
```
```
docker-compose up --build
```

### Backend (Render)
- URL https://frappe-library-backend.onrender.com
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
