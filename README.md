# DPDzero_Backend_Assignment
### Backend System
## Introduction
This is the API documentation for the Backend System project. This project is built using Flask, a lightweight Python web framework, and it interacts with a MySQL database.

## Framework
The API is built using Flask, a lightweight Python web framework.

## Database Schema
The application uses a MySQL database named `Users` with two tables:
### Users Table
The `users` table is used to store user information.
### Key-Value Data Table
The `key_value_data` table is used to store key-value pairs.
## Getting Started

### Prerequisites
1. Python (version 3.7 or higher) installed on your system.
2. MySQL database server.
3. Required Python packages (Flask, SQLAlchemy, mysql-connector-python) installed.

### Installation
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/backend-system.git

2. Navigate to the project directory:
 ```bash
    cd backend-system
3. Install Python packages:\*pip install -r requirements.txt*\
### Configuration
Configure the application as follows:
Create a MySQL database named Users.
Update the SQLALCHEMY_DATABASE_URI in app.py with your MySQL server configuration, including username, password, host, port, and the database name.
### Running the Application
 ```bash
python app.py

The app will be accessible at  
 ```bash 
http://localhost:5000.

### Testing
The test_scripts.py file contains test cases for the API. To execute the tests, 
run the following command:
 \*python test_scripts.py*\


