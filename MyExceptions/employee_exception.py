class EmployeeNotFoundException(Exception):
    def __init__(self, employee_id):
        super().__init__(f"Employee with {employee_id} was not found")
