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
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Unix or MacOS
source venv/bin/activate
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

## Contact 📌

If you have any questions or suggestions, feel free to open an issue or contact me at [felixdavidsuarezbonilla@gmail.com].
