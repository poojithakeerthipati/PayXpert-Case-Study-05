import unittest
from DAO import EmployeeService
from Entity import Employee


class TestEmployeeServiceModule(unittest.TestCase):
    def setUp(self):
        self.employee_service = EmployeeService()
        self.test_employee = (
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
        self.test_employee_id = self.employee_service.add_employee(self.test_employee)

    def test_display_employees(self):
        employees = self.employee_service.get_all_employees()
        self.assertGreater(len(employees), 0)

    def test_update_employee(self):
        updated_employee = (
            "Mikel",
            "Adams",
            "1989-01-25",
            "M",
            "mickel@example.com",
            "9564764561",
            "mumbai",
            "Senior Manager",
            "2018-10-01",
            "2024-09-17",
        )
        self.employee_service.update_employee(updated_employee, self.test_employee_id)
        updated_employee = self.employee_service.cursor.execute(
            "SELECT * FROM Employee WHERE EmployeeID = ?", (self.test_employee_id,)
        ).fetchone()

        self.assertEqual(updated_employee[1], "Mikel")
        self.assertEqual(updated_employee[2], "Adams")
        self.assertEqual(updated_employee[4], "M")

    def test_remove_employee(self):
        self.employee_service.remove_employee(self.test_employee_id)

        removed_employee = self.employee_service.cursor.execute(
            "SELECT * FROM Employee WHERE EmployeeID = ?", (self.test_employee_id,)
        ).fetchone()

        self.assertIsNone(removed_employee)


if __name__ == "__main__":
    unittest.main()
