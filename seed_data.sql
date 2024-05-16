

Use PayXpertDB;

INSERT INTO Employee
    ( FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
VALUES
    ('Ram', 'Pothineni', '1988-05-15', 'M', 'ram@example.com', '181-53686774', '451 Church Street', 'Developer', '2020-01-01', NULL),
    ('Peter', 'Parker', '1991-08-10', 'M', 'peter123@example.com', '91-9847543210', 'Forest Hills', 'Manager', '2018-06-05', NULL),
    ('Scarlett', 'Johansson', '1982-03-10', 'F', 'scarlett@example.com', '47568368743', 'Manhattan', 'Sales Associate', '2021-02-20', NULL),
    ('Emily', 'Brown', '1995-11-20', 'F', 'emily@example.com', '4625786754', 'Los Angeles', 'HR Coordinator', '2018-09-10', NULL),
    ('David', 'Warner', '1988-07-03', 'M', 'david@example.com', '7436784579', 'New York City', 'Accountant', '2022-04-05', NULL);


INSERT INTO Payroll
    (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
VALUES
    (1, '2024-05-01', '2024-05-15', 500000, 20000, 30000, 490000),
    (2, '2024-05-01', '2024-05-15', 650000, 30000, 40000, 640000),
    (3, '2024-05-01', '2024-05-15', 551000, 25000, 35000, 541000),
    (4, '2024-05-01', '2024-05-15', 520000, 22000, 32000, 510000),
    (5, '2024-05-01', '2024-05-15', 605800, 28000, 38000, 595800);


INSERT INTO Tax
    (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
VALUES
    (1, 2024, 500000, 20000),
    (2, 2024, 650000, 30000),
    (3, 2024, 551000, 25000),
    (4, 2024, 520000, 22000),
    (5, 2024, 605800, 28000);



INSERT INTO FinancialRecord
    (EmployeeID, RecordDate, Description, Amount, RecordType)
VALUES
    (1, '2024-05-01', 'Bonus', 1000.00, 'Income'),
    (2, '2024-05-01', 'Travel Expenses', 500.00, 'Expense'),
    (3, '2024-05-01', 'Commission', 700.00, 'Income'),
    (4, '2024-05-01', 'Training Course Fee', 300.00, 'Expense'),
    (5, '2024-05-01', 'Salary', 5800.00, 'Income');

SELECT *
FROM Employee;
SELECT *
FROM FinancialRecord;
SELECT *
FROM Payroll;
SELECT *
FROM Tax;