--Creating a DATABASE Named PayXpertDB to create our tables
CREATE DATABASE PayXpertDB;

-- Using the DATABASE created
Use PayXpertDB;


-- Creating Employee Table
CREATE TABLE Employee
(
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(200),
    LastName NVARCHAR(200),
    DateOfBirth DATE,
    Gender CHAR(1),
    Email NVARCHAR(200),
    PhoneNumber NVARCHAR(20),
    Address NVARCHAR(200),
    Position NVARCHAR(200),
    JoiningDate DATE,
    TerminationDate DATE
);

-- Creating Payroll Table 
CREATE TABLE Payroll
(
    PayrollID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    PayPeriodStartDate DATE,
    PayPeriodEndDate DATE,
    BasicSalary DECIMAL(10, 2),
    OvertimePay DECIMAL(10, 2),
    Deductions DECIMAL(10, 2),
    NetSalary DECIMAL(10, 2),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Creating Tax Table
CREATE TABLE Tax
(
    TaxID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    TaxYear INT,
    TaxableIncome DECIMAL(10, 2),
    TaxAmount DECIMAL(10, 2),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Creating FinancialRecord Table
CREATE TABLE FinancialRecord
(
    RecordID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    RecordDate DATE,
    Description VARCHAR(300),
    Amount DECIMAL(10, 2),
    RecordType NVARCHAR(200),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);