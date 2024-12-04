# Employee Management System

A Python and JavaScript-based application designed for managing employee data efficiently. This system incorporates modern development practices to ensure scalability, security, and usability.

---

## Features
- **Employee Records Management:** Add, update, delete, and view employee data.
- **Role-Based Access Control (RBAC):** Secure access based on user roles.
- **API Integration:** Exposes RESTful API endpoints for seamless integration.
- **Data Security:** Implements measures to ensure data integrity and privacy.

---

## Implementation Details
This project is built using:
- **Backend:** Python
- **Frontend:** JavaScript
- **Database:** (MariaDB)

**Development Considerations:**
- Prioritized modular code for scalability.
- Used environment variables for sensitive configurations.

---

## Setup and Run Instructions

### Prerequisites
- Python 3.x installed
- Node.js installed
- Database setup (if applicable)

### Installation Steps
1. Clone the repository:  
   ```bash
   git clone https://github.com/OmarMagdy2k/employee_management_system.git
2. Navigate to the project directory:
   ```bash
   cd employee_management_system
3. Install dependencies:
   ```bash
   sudo apt install -y nodejs
   sudo pip3 install frappe-bench
   bench init frappe-bench --version 14
4. Configure environment variables in a .env file.

## Task Completion Checklist
- [x] Models.
- [x] Validations & Business Logic.
- [x] Workflow.
- [x] APIs.
- [ ] Testing.
- [ ] Logging.


# API Documentation

This API allows interaction with the Employee Management System to manage companies, departments, employees, and projects. All endpoints use the `frappe` framework.

## 1. **Get All Companies**
### Endpoint:  
`GET /api/method/get_all_companies`

### Parameters:  
- None

### Expected Response:  
	```json
	    [
	      {
	        "company_name": "TechCorp",
	        "number_of_departments": 5,
	        "number_of_employees": 120,
	        "number_of_projects": 10
	      },
	      {
	        "company_name": "InnovateX",
	        "number_of_departments": 3,
	        "number_of_employees": 50,
	        "number_of_projects": 7
	      }
	    ]
		 
## 2. **Get a Specific Company**
### Endpoint:  
`GET /api/method/get_company`

### Parameters:  
- `company_name` (string): Name of the company.

### Example Request:  
`GET /api/method/get_company?company_name=TechCorp`

### Expected Response:  
	```json
	{
	  "company_name": "TechCorp",
	  "number_of_departments": 5,
	  "number_of_employees": 120,
	  "number_of_projects": 10
	}
 
## 3. **Get All Departments**
### Endpoint:  
`GET /api/method/get_all_departments`

### Parameters:  
- None

### Expected Response:  
	```json
	[
		{
			"department_name": "Engineering",
			"company": "TechCorp",
			"number_of_employees": 50,
			"number_of_projects": 5
		},
		{
			"department_name": "Marketing",
			"company": "InnovateX",
			"number_of_employees": 15,
			"number_of_projects": 3
		}
	]
 
## 4. **Get a Specific Department**
### Endpoint:  
`GET /api/method/get_department`

### Parameters:  
- `department_name` (string): Name of the department to retrieve.

### Example Request:  
`GET /api/method/get_department?department_name=Engineering`

### Expected Response:  
	```json
	{
	  "department_name": "Engineering",
	  "company": "TechCorp",
	  "number_of_employees": 50,
	  "number_of_projects": 5
	}

## 5. **Create Employee**
### Endpoint:  
`POST /api/method/create_employee`

### Parameters:  
- `data` (JSON): JSON object containing employee data.

#### Example Request Body:
	```json
	{
	  "employee_name": "Omar Magdy",
	  "email_address": "omarmagdy2k@gmail.com",
	  "mobile_number": "1094979164",
	  "address": "123 Tech Street",
	  "company": "TechCorp",
	  "department": "Engineering",
	  "designation": "Software Engineer",
	  "employee_status": "Active",
	  "hired_on": "2024-01-01",
	  "days_employed": 30,
	  "number_of_assigned_projects": 3
	}
 
### Expected Response:  
	```json
 	{
	  "employee_name": "Omar Magdy",
	  "email_address": "omarmagdy2k@gmail.com",
	  "mobile_number": "1094979164",
	  "address": "123 Tech Street",
	  "company": "TechCorp",
	  "department": "Engineering",
	  "designation": "Software Engineer",
	  "employee_status": "Active",
	  "hired_on": "2024-01-01",
	  "days_employed": 30,
	  "number_of_assigned_projects": 3
	}
 
## 6. **Get All Employees**
### Endpoint:  
`GET /api/method/get_employees`

### Parameters:  
- None

### Expected Response:  
	```json
	[
	  {
	    "employee_name": "Omar Magdy",
	    "email_address": "omarmagdy2k@gmail.com",
	    "mobile_number": "1094979164",
	    "address": "123 Tech Street",
	    "company": "TechCorp",
	    "department": "Engineering",
	    "designation": "Software Engineer",
	    "employee_status": "Active",
	    "hired_on": "2024-01-01",
	    "days_employed": 30,
	    "number_of_assigned_projects": 3
	  }
	]
 
## 7. **Get a Specific Employee**
### Endpoint:  
`GET /api/method/get_employee`

### Parameters:  
- `employee_name` (string): Name of the employee.

### Example Request:  
`GET /api/method/get_employee?employee_name=Omar Magdy`

### Expected Response:  
	```json
	{
	  "employee_name": "Omar Magdy",
	  "email_address": "omarmagdy2k@gmail.com",
	  "mobile_number": "1094979164",
	  "address": "123 Tech Street",
	  "company": "TechCorp",
	  "department": "Engineering",
	  "designation": "Software Engineer",
	  "employee_status": "Active",
	  "hired_on": "2024-01-01",
	  "days_employed": 30,
	  "number_of_assigned_projects": 3
	}
 
## 8. **Update Employee**
### Endpoint:  
`POST /api/method/update_employee`

### Parameters:  
- `employee_name` (string): Name of the employee to update.
- `data` (JSON): JSON object containing the fields to update.

#### Example Request Body:
	```json
	{
	  "employee_name": "Omar Magdy",
	  "data": {
	    "employee_status": "Inactive"
	  }
	}
### Expected Response:  
	```json
 	{
	  "employee_name": "Omar Magdy",
	  "email_address": "omarmagdy2k@gmail.com",
	  "mobile_number": "1094979164",
	  "address": "123 Tech Street",
	  "company": "TechCorp",
	  "department": "Engineering",
	  "designation": "Software Engineer",
	  "employee_status": "Inactive",
	  "hired_on": "2024-01-01",
	  "days_employed": 30,
	  "number_of_assigned_projects": 3
	}
 
## 9. **Delete Employee**
### Endpoint:  
`POST /api/method/delete_employee`

### Parameters:  
- `employee_name` (string): Name of the employee to delete.

### Example Request:  
`POST /api/method/delete_employee?employee_name=Omar Magdy`

### Expected Response:  
	```json
	{
	  "message": "Employee Omar Magdy deleted successfully"
	}
 
## 10. **Create Project**
### Endpoint:  
`POST /api/method/create_project`

### Parameters:  
- `data` (JSON): JSON object containing project details.

#### Example Request Body:
	```json
	{
	  "project_name": "Project Alpha",
	  "description": "A cutting-edge software project",
	  "company": "TechCorp",
	  "department": "Engineering",
	  "start_date": "2024-02-01",
	  "end_date": "2024-12-31"
	}
### Expected Response:  
	```json
 	{
	  "project_name": "Project Alpha",
	  "description": "A cutting-edge software project",
	  "company": "TechCorp",
	  "department": "Engineering",
	  "start_date": "2024-02-01",
	  "end_date": "2024-12-31"
	}
 
## 11. **Get All Projects**
### Endpoint:  
`GET /api/method/get_projects`

### Parameters:  
- None

### Expected Response:  
	```json
	[
	  {
	    "project_name": "Project Alpha",
	    "description": "A cutting-edge software project",
	    "company": "TechCorp",
	    "department": "Engineering",
	    "start_date": "2024-02-01",
	    "end_date": "2024-12-31"
	  }
	]

## 12. **Get a Specific Project**
### Endpoint:  
`GET /api/method/get_project`

### Parameters:  
- `project_name` (string): Name of the project.

### Example Request:  
`GET /api/method/get_project?project_name=Project Alpha`

### Expected Response:  
	```json
	{
	  "project_name": "Project Alpha",
	  "description": "A cutting-edge software project",
	  "company": "TechCorp",
	  "department": "Engineering",
	  "start_date": "2024-02-01",
	  "end_date": "2024-12-31"
	}

Feel free to fork, explore, and contribute to this repository! 🎉
