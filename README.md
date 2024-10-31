# Health Care Backend API

A robust REST API built with Python/FastAPI and MySQL for the Health Care project, designed to handle patient records and authentication.

## 📑 Table of Contents
1. [Features](#features-)
2. [Requirements](#requirements-)
3. [Installation](#installation-)
4. [Project Structure](#project-structure-)
5. [Configuration](#configuration-)
6. [API Documentation](#api-documentation-)
7. [Development](#development-)
8. [Contact](#contact-)

   

## Features ✨

- Patient record management: create, update, delete, and retrieve records
- File processing: securely process and validate healthcare data from Excel files
- Authentication: secure JWT-based user authentication and role-based access control
- Database operations: efficient handling of MySQL operations
- Data security: secure handling of personal health information

## Requirements 🛠

### Core Dependencies
- Python 3.10+
- MySQL Server
- pip package manager

### Python Packages
```
python-multipart==0.0.6
fastapi[standard]==0.100.0
uvicorn==0.23.0
pydantic==2.0
python-dotenv==1.0.0
requests==2.31.0
pandas==2.0.3
openpyxl==3.1.2
mysql-connector-python==8.1.0
```

##  Installation 🚀

1. Clone the repository
```bash
git clone <repository-url>
cd healthcare-backend
```

2. Create and activate virtual environment

```bash
#Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Unix or MacOS
source venv/bin/activate
# or
source venv/Scripts/Activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure 📦

```
healthcare-backend/
├── database/               # Database related files
│   ├── MySQLConnection.py    # Database connection handler
│   ├── PatientService.py     # Patient data services
│   ├── script_sql.sql        # Database schema
│   └── temp/                 # Temporary files
├── models/                 # Data models
│   ├── ErrorMsg.py          # Error message definitions
│   ├── Patient.py           # Patient model
│   ├── ResultResponse.py    # API response models
│   └── Token.py             # Authentication token model
├── Dockerfile              # Container configuration
├── healthcare.py           # Main application file
└── requirements.txt        # Project dependencies
```

## Configuration ⚙

### Database Setup

1. Create a MySQL database named `db_healthcare`
2. Configure your database connection:
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "2802",
    "database": "db_healthcare"
}
```

### Environment Variables
Create a `.env` file in the root directory:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=2802
DB_NAME=db_healthcare
JWT_SECRET=your_jwt_secret
```

## API Documentation 🔌

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | User authentication |
| POST | `/logout` | User logout |
| POST | `/validate_token` | Validate authentication token |

### Patient Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/patient-record` | Retrieve patient records |
| POST | `/process-file` | Process patient data file |

### Sample Request
```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "pass"}'
```

## Development 💻

### Running the Application
```bash
# Development mode
uvicorn healthcare:app --reload

# Production mode
uvicorn healthcare:app --host 0.0.0.0 --port 8000
```

### Using Docker
```bash
# Build image
docker build -t healthcare-backend .

# Run container
docker run -p 8000:8000 healthcare-backend
```
# Health Care Front-End API

This project is the front-end of a healthcare web application. It includes a page to upload an Excel file with patient information to the database and has another page to register users. The application consists of two pages, each designed for a specific function within the user's workflow.

## Index

1. 🛠️ [Prerequisites](#-prerequisites)
2. 🚀 [Setup and Development](#-setup-and-development)
3. 💻 [Functionalities](#-functionalities)
4. 📌[Contact](#contact-)

## 🛠️ Prerequisites

- Visual Studio Code
- node_modules == 22.11.0
- vite
- Git
- SSH key (for repository cloning)
- Live Server extension for VS Code
- Web browser



## 🚀 Setup and Development

1. Clone the repository
```bash
git clone <repository-url>
cd healthcare_frontend
```

2. **Open the project in Visual Studio Code:**
   ```
   code .
   ```

3. **Install the Live Server extension:**
   - Open the Extensions view in VS Code (Ctrl+Shift+X)
   - Search for "Live Server"
   - Click "Install" on the extension by Ritwick Dey

4. **Install dependencies:**

   ```
   npm install 
   npm install vite --save-dev
   ```

5. **Run the project:**
   ```
   npm run dev
   ```
   - The application will open in your default web browser using a local server (usually ` http://localhost:5173/` or similar)

6. **Development:**
   - Make changes to your HTML, CSS, or JavaScript files
   - Save the files
   - The browser will automatically refresh to show your changes
   

# 📋 FUNCTIONALITIES OF EACH TAB

## 🏠 Home (Home.jsx)

The Landing Page section provides users with an interface where they can upload xlsx files to save the information they contain in the database.

##  ✏️ Patient Records (PatientRecords.jsx)


The Landing Page section provides users with an interface where they can search for specific patient information in the database.


## Contact 📌

If you have any questions or suggestions, feel free to open an issue or contact me at [felixdavidsuarezbonilla@gmail.com].
