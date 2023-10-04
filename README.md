# Frappe-Library-Management-Web-Application

### Problem statement [link](https://frappe.io/dev-hiring-test)

## Main Ideas
- Page navigation kept minimal, for quick single page application like usage.
+ Instant search as you type allows fast lookup of books, Debouncing implemented to reduce api calls.
- Keep main functionality at easy reach, issuing and returning book, in the home screen using Side Drawers.
+ Avoid unnecessary prompts for editing small fields, such as Book Stock, has been done with simple edit button within Book details UI.
- Integration to Frappe API done via backend, which scans through several pages of the api as required for larger no of books.
+ CRUD operations implemented through Forms within Modals.

## Demo
- [Import Books, Update Book Stock](https://drive.google.com/file/d/1rJ_PQPSNiqn2awgdrPoMUq1lCQzb0DgI/view?usp=drive_link)
- [Search Books with Debouncing Instant search](https://drive.google.com/file/d/1Va9UcHdcHfkA7yQaFgu0QAqFfI_OIpGk/view?usp=drive_link)
- [Return Book](https://drive.google.com/file/d/1KDdcnCfVAyCQvoRiVLpLb8ylBJktd0j3/view?usp=drive_link)
- [₹500 debt exceed alert, Transaction details, Issue Book](https://drive.google.com/file/d/1iHlh1ELe4dMRu_it9GqnIayyof1d144a/view?usp=drive_link)
- [Members CRUD](https://drive.google.com/file/d/1vSJ39V_SO_Njomr2wELoyEBGKnRxdyV5/view?usp=drive_link)

## Data Design:
![DataDesign](./design/data_design_frappe_library.png)

## Libraries used:
**Frontend**
- Svelte and Sveltkit
- Tailwind CSS
- Skeleton UI Toolkit for Svelte

**Backend**
- Flask
- Flask Migrate and Alembic
- SQLAlchemy

**Database**
- Postgresql

## Running locally:
**Run in order:**

### Database (AWS RDS)
```
cd database
```
```
docker-compose up --build
```

### Backend (AWS EC2)
- URL https://16.16.156.1
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
