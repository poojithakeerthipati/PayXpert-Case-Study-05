from tabulate import tabulate
from Util.DBConn import DBConnection
from abc import ABC, abstractmethod
from MyExceptions import EmployeeNotFoundException


class IEmployeeService(ABC):
    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def add_employee(self, Employee):
        pass

    @abstractmethod
    def update_employee(self, Employee, employee_id):
        pass

    @abstractmethod
    def remove_employee(self, employee_id):
        pass


class EmployeeService(DBConnection, IEmployeeService):
    def get_employee_by_id(self, employee_id):
        try:
            self.cursor.execute(
                "SELECT * FROM Employee WHERE EmployeeID=?", (employee_id)
            )
            employee_data = [list(row) for row in self.cursor.fetchall()]
            if employee_data:
                headers = [
                    "EmployeeID",
                    "FirstName",
                    "LastName",
                    "DateOfBirth",
                    "Gender",
                    "Email",
                    "PhoneNumber",
                    "Address",
                    "Position",
                    "JoiningDate",
                    "TerminationDate",
                ]
                print(tabulate(employee_data, headers, tablefmt="grid"))
            else:
                raise EmployeeNotFoundException(employee_id)
        except Exception as e:
            print("OOPS Error Happened")

    def get_all_employees(self):
        try:
            self.cursor.execute("SELECT * FROM Employee ")
            employee_data = [list(row) for row in self.cursor.fetchall()]
            if employee_data:
                headers = [
                    "EmployeeID",
                    "FirstName",
                    "LastName",
                    "DateOfBirth",
                    "Gender",
                    "Email",
                    "PhoneNumber",
                    "Address",
                    "Position",
                    "JoiningDate",
                    "TerminationDate",
                ]
                print(tabulate(employee_data, headers, tablefmt="grid"))
            else:
                raise EmployeeNotFoundException(employee_data[0])
        except Exception as e:
            print("Error Happened")

    def add_employee(self, Employee):
        try:
            self.cursor.execute(
                """INSERT INTO Employee(FirstName, LastName, DateOfBirth, Gender, Email,
                PhoneNumber, Address, Position, JoiningDate, TerminationDate) 
                VALUES(?,?,?,?,?,?,?,?,?,?)""",
                (
                    Employee.first_name,
                    Employee.last_name,
                    Employee.date_of_birth,
                    Employee.gender,
                    Employee.email,
                    Employee.phone_number,
                    Employee.address,
                    Employee.position,
                    Employee.joined_date,
                    Employee.termination_date,
                ),
            )
            self.conn.commit()
        except Exception as e:
            print("Error adding employee:", e)

    def update_employee(self, Employee, employee_id):
        try:
            self.cursor.execute(
                """UPDATE Employee set FirstName=?, LastName=?, DateOfBirth=?, Gender=?, Email=?,
                PhoneNumber=?, Address=?, Position=?, JoiningDate=?, TerminationDate=? WHERE EmployeeID=?""",
                (
                    Employee.first_name,
                    Employee.last_name,
                    Employee.date_of_birth,
                    Employee.gender,
                    Employee.email,
                    Employee.phone_number,
                    Employee.address,
                    Employee.position,
                    Employee.joined_date,
                    Employee.termination_date,
                    employee_id,
                ),
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def remove_employee(self, employee_id):
        try:
            self.cursor.execute(
                "DELETE FROM Employee WHERE EmployeeID=?", (employee_id)
            )
            self.conn.commit()
        except Exception as e:
            raise EmployeeNotFoundException(employee_id)
