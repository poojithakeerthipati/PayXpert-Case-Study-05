# PayXpertDB Management System
## Description
- PayXpertDB Management System is a Python project designed to manage employee records, payroll information, taxes, and financial records within a database.

## Installation
1. Clone the repository to your local machine:
```bash
git clone https://github.com/poojithakeerthipati/PayXpert-Case-Study-05.git
```
## Install the required dependencies:
```bash
pip install tabulate
pip install pyodbc
```
## Usage
1. Running the Application
To run the PayXpertDB Management System, execute the following command:

```bash
python main.py
```
2. Functionality
### The system provides the following functionalities:

- View employee records: Retrieve information about employees stored in the database.
- Add new employees: Insert new employee records into the database.
- Update employee information: Modify existing employee details such as name, position, etc.
- Remove employees: Delete employee records from the database.
- Manage payroll: Handle payroll information including basic salary, overtime pay, deductions, and net salary.
- Handle taxes: Manage tax records for employees including taxable income and tax amounts.
- Maintain financial records: Record financial transactions related to employees.
## Configuration
- No additional configuration is required for the PayXpertDB Management System. However, ensure that your database connection details are correctly configured in the DBConn.py file.

## Contributing
- Contributions to the PayXpertDB Management System are welcome! To contribute, follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature/new-feature).
- Make your changes.
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature/new-feature).
- Create a new Pull Request.
## License
- This project is licensed under the MIT License - see the LICENSE file for details.

## Credits
- Tabulate: Used for formatting data in tabular form.
- Pyodbc: Python ODBC library used for connecting to SQL Server database.