# Django REST Framework Project Setup

This guide provides step-by-step instructions to set up and run the Django REST Framework (DRF) project locally.

## Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- pip
- virtualenv (optional but recommended)
- MySQL 

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/marketbytes-official/alsi_cms_backend.git
cd alsi_cms_backend
```

### 2. Create and Activate Virtual Environment
#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```


![Screenshot 2025-02-11 141312](https://github.com/user-attachments/assets/c8b20756-dbab-43b8-8b3a-ad963a33a811)


### 3. Install Dependencies
```bash
pip install -r requirements.txt
```


![Screenshot 2025-02-11 141357](https://github.com/user-attachments/assets/b01ddb5c-6a29-4005-9a6c-ac78c1df9b2d)


### 4. Set Up Environment Variables
Create a `.env` file in the project root and add the required configurations:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=mysql://username:password@localhost/dbname
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```


![Screenshot 2025-02-11 142256](https://github.com/user-attachments/assets/e591f0d0-e8eb-4bed-b1c2-1fdefffc09cd)



### 7. Access the API
Open your browser and go to:
```
http://127.0.0.1:8000/api/
```

## Importing and Exporting Data (If Required)
To export data:
```bash
python manage.py dumpdata app_name > data.json
```
To import data:
```bash
python manage.py loaddata data.json
```

## Additional Notes
- Ensure `.env` is listed in `.gitignore` to prevent exposing sensitive data.
- If using a different database, update the `DATABASE_URL` accordingly.

## License
This project is licensed under the MIT License.

---
Feel free to customize this README based on your project's specific requirements!

