import unittest
from datetime import datetime
from Entity import Employee, Payroll, Tax, FinancialRecord
from DAO import EmployeeService, FinancialService, TaxService, PayrollService
from MyExceptions.employee_exception import EmployeeNotFoundException


class TestPayrollSystem(unittest.TestCase):
    def setUp(self):
        self.employee_service = EmployeeService()
        self.financial_service = FinancialService()
        self.tax_service = TaxService()
        self.payroll_service = PayrollService()

    def test_calculate_gross_salary_for_employee(self):
        # Create a test employee
        test_employee = Employee(
            "John",
            "Doe",
            "1990-01-01",
            "Male",
            "john@example.com",
            "1234567890",
            "123 Street",
            "Manager",
            "2022-01-01",
            None,
        )
        self.employee_service.add_employee(test_employee)
        self.payroll_service.generate_payroll(
            test_employee.employee_id, "2024-05-01", "2024-05-31"
        )
        payroll = self.payroll_service.get_pay_rolls_for_period(
            "2024-05-01", "2024-05-31"
        )
        self.assertIsNotNone(payroll)
        self.assertIsNotNone(payroll.gross_salary)
        self.employee_service.remove_employee(test_employee.employee_id)

    def test_calculate_net_salary_after_deductions(self):

        test_employee = Employee(
            "Jane",
            "Smith",
            "1995-02-15",
            "Female",
            "jane@example.com",
            "9876543210",
            "456 Street",
            "Developer",
            "2022-02-01",
            None,
        )

        self.employee_service.add_employee(test_employee)

        self.payroll_service.generate_payroll(
            test_employee.employee_id, "2024-05-01", "2024-05-31"
        )

        payroll = self.payroll_service.get_pay_rolls_for_period(
            "2024-05-01", "2024-05-31"
        )

        self.assertIsNotNone(payroll)

        self.assertIsNotNone(payroll.net_salary)

        self.employee_service.remove_employee(test_employee.employee_id)

    def test_verify_tax_calculation_for_high_income_employee(self):
        test_employee = Employee(
            "James",
            "Johnson",
            "1985-08-10",
            "Male",
            "james@example.com",
            "5678901234",
            "789 Street",
            "CEO",
            "2022-03-01",
            None,
        )

        self.employee_service.add_employee(test_employee)
        self.payroll_service.generate_payroll(
            test_employee.employee_id, "2024-05-01", "2024-05-31"
        )

        payroll = self.payroll_service.get_pay_rolls_for_period(
            "2024-05-01", "2024-05-31"
        )

        self.assertIsNotNone(payroll)

        tax_amount = self.tax_service.calculate_tax(test_employee.employee_id, "2024")

        self.assertIsNotNone(tax_amount)

        self.employee_service.remove_employee(test_employee.employee_id)

    def test_process_payroll_for_multiple_employees(self):
        test_employees = [
            Employee(
                "Alice",
                "Anderson",
                "1992-04-20",
                "Female",
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
                "Male",
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
                "Female",
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

        for employee in test_employees:
            self.payroll_service.generate_payroll(
                employee.employee_id, "2024-05-01", "2024-05-31"
            )

        for employee in test_employees:
            payroll = self.payroll_service.get_pay_rolls_for_period(
                "2024-05-01", "2024-05-31"
            )

            self.assertIsNotNone(payroll)

        for employee in test_employees:
            self.employee_service.remove_employee(employee.employee_id)

    def test_verify_error_handling_for_invalid_employee_data(self):
        invalid_employee_id = -1
        with self.assertRaises(EmployeeNotFoundException):
            self.employee_service.get_employee_by_id(invalid_employee_id)
        invalid_employee_id = -1
        with self.assertRaises(EmployeeNotFoundException):
            self.employee_service.remove_employee(invalid_employee_id)


if __name__ == "__main__":
    unittest.main()
