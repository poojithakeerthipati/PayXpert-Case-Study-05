from Util.DBConn import DBConnection
from abc import ABC, abstractmethod
from tabulate import tabulate
from MyExceptions import PayrollGenerationException


class IPayrollService(ABC):
    @abstractmethod
    def generate_payroll(self, Payroll):
        pass

    @abstractmethod
    def get_pay_roll_by_id(self, payroll_id):
        pass

    @abstractmethod
    def get_pay_rolls_for_employee(self, Payroll):
        pass

    @abstractmethod
    def get_pay_rolls_for_period(self, Payroll):
        pass


class PayrollService(DBConnection, IPayrollService):
    def generate_payroll(self, employee_id, start_date, end_date):
        try:
            self.cursor.execute(
                """SELECT *
                                FROM PayRoll
                                WHERE EmployeeID=? AND PayPeriodStartDate=? AND PayPeriodEndDate = ?""",
                (
                    employee_id,
                    start_date,
                    end_date,
                ),
            )
            pay_roll_data = self.cursor.fetchall()
            if pay_roll_data:
                print(pay_roll_data)
            else:
                raise PayrollGenerationException(employee_id)
        except Exception as e:
            print("OOPS ERROR HAPPENED")

    def get_pay_roll_by_id(self, payroll_id):
        try:
            self.cursor.execute("SELECT * FROM PayRoll WHERE PayrollID=?", (payroll_id))
            pay_roll_data = self.cursor.fetchall()
            print(pay_roll_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_pay_rolls_for_employee(self, employee_id):
        try:
            self.cursor.execute(
                "SELECT * FROM PayRoll WHERE EmployeeID=?", (employee_id)
            )
            pay_roll_data = self.cursor.fetchall()
            print(pay_roll_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_pay_rolls_for_period(self, start_date, end_date):
        try:
            self.cursor.execute(
                """SELECT *
                                FROM PayRoll
                                WHERE PayPeriodStartDate=? AND PayPeriodEndDate = ?""",
                (
                    start_date,
                    end_date,
                ),
            )
            pay_roll_data = self.cursor.fetchall()
            print(pay_roll_data)
            self.conn.commit()
        except Exception as e:
            print(e)
