import unittest
from datetime import datetime
from Entity import Employee
from DAO import EmployeeService, PayrollService, TaxService
from MyExceptions import EmployeeNotFoundException


class TestPayrollSystem(unittest.TestCase):
    def setUp(self):
        self.employee_service = EmployeeService()
        self.payroll_service = PayrollService()
        self.tax_service = TaxService()

    def tearDown(self):
        pass

    def test_calculate_gross_salary_for_employee(self):
        test_employee = Employee(
            "Mike",
            "Russel",
            "1980-01-01",
            "M",
            "mikes@example.com",
            "1234567890",
            "chennai",
            "Manager",
            "2022-01-01",
            None,
        )
        employee_id = 6
        self.employee_service.add_employee(test_employee)
        self.payroll_service.generate_payroll(employee_id, "2024-05-01", "2024-05-31")
        payroll = self.payroll_service.get_pay_rolls_for_period(
            "2024-05-01", "2024-05-15"
        )
        self.assertIsNotNone(payroll)

    def test_calculate_net_salary_after_deductions(self):
        employee_id = 7
        test_employee = Employee(
            "Jane",
            "Smith",
            "1995-02-15",
            "F",
            "jane@example.com",
            "9876543210",
            "456 Street",
            "Developer",
            "2022-02-01",
            None,
        )

        self.employee_service.add_employee(test_employee)

        self.payroll_service.generate_payroll(employee_id, "2024-05-01", "2024-05-31")

        payroll = self.payroll_service.get_pay_rolls_for_period(
            "2024-05-01", "2024-05-31"
        )

        self.assertIsNotNone(payroll)

    def test_verify_tax_calculation_for_high_income_employee(self):
        employee_id = 7
        test_employee = Employee(
            "James",
            "Johnson",
            "1985-08-10",
            "M",
            "james@example.com",
            "5678901234",
            "789 Street",
            "CEO",
            "2022-03-01",
            None,
        )

        self.employee_service.add_employee(test_employee)
        self.payroll_service.generate_payroll(employee_id, "2024-05-01", "2024-05-31")

        payroll = self.payroll_service.get_pay_rolls_for_period(
            "2024-05-01", "2024-05-31"
        )

        self.assertIsNotNone(payroll)

    def test_process_payroll_for_multiple_employees(self):
        test_employees = [
            Employee(
                "Alice",
                "Anderson",
                "1992-04-20",
                "F",
                "alice@example.com",
                "1112223334",
                "101 Park Ave",
                "Manager",
                "2022-04-01",
                None,
            ),
            Employee(
                "Bob",
                "Brown",
                "1990-07-15",
                "M",
                "bob@example.com",
                "2223334445",
                "202 Main St",
                "Developer",
                "2022-05-01",
                None,
            ),
            Employee(
                "Eve",
                "Evans",
                "1995-10-30",
                "F",
                "eve@example.com",
                "3334445556",
                "303 Elm St",
                "Analyst",
                "2022-06-01",
                None,
            ),
        ]

        for employee in test_employees:
            self.employee_service.add_employee(employee)

        employee_id = 9

        for employee in test_employees:
            self.payroll_service.generate_payroll(
                employee_id, "2024-05-01", "2024-05-31"
            )
            employee_id += 1

        for employee in test_employees:
            payroll = self.payroll_service.get_pay_rolls_for_period(
                "2024-05-01", "2024-05-31"
            )

            self.assertIsNotNone(payroll)


if __name__ == "__main__":
    unittest.main()
