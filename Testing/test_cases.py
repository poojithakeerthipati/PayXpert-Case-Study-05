import unittest
from DAO import EmployeeService, PayrollService, TaxService, FinancialService
from MyExceptions import InvalidInputException


class TestPayXpert(unittest.TestCase):
    def setUp(self):
        self.employee_service = EmployeeService()

    def test_calculate_gross_salary_for_employee(self):
        employee_id = 1
        basic_salary = 500000
        overtime_pay = 20000
        deductions = 30000
        expected_gross_salary = 490000
        employee_service = EmployeeService()
        actual_gross_salary = employee_service.calculate_gross_salary(
            employee_id, basic_salary, overtime_pay
        )
        self.assertTrue(actual_gross_salary, expected_gross_salary)

    def test_calculate_net_salary_after_deductions(self):
        gross_salary = 6500
        deductions = 1000
        expected_net_salary = 5500
        payroll_service = PayrollService()
        actual_net_salary = payroll_service.calculate_net_salary(
            gross_salary, deductions
        )
        self.assertTrue(actual_net_salary, expected_net_salary)

    def test_verify_tax_calculation_for_high_income_employee(self):
        employee_id = 1
        high_income = 10000
        expected_tax_amount = 2000
        tax_service = TaxService()
        actual_tax_amount = tax_service.calculate_tax(employee_id, high_income)
        self.assertEqual(actual_tax_amount, expected_tax_amount)

    def test_process_payroll_for_multiple_employees(self):
        employee_ids = [123, 124, 125]
        pay_period_start_date = "2024-05-01"
        pay_period_end_date = "2024-05-15"
        payroll_service = PayrollService()
        payroll_details = payroll_service.process_payroll_for_multiple_employees(
            employee_ids, pay_period_start_date, pay_period_end_date
        )

        self.assertIsNotNone(payroll_details)

    def test_verify_error_handling_for_invalid_employee_data(self):
        invalid_employee_id = 999
        incorrect_salary_info = (-1000, 500, 0)
        employee_service = EmployeeService()
        with self.assertRaises(InvalidInputException):
            employee_service.calculate_gross_salary(*incorrect_salary_info)


if __name__ == "__main__":
    unittest.main()
