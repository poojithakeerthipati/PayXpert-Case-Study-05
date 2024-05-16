from Util.DBConn import DBConnection
from abc import ABC, abstractmethod
from tabulate import tabulate


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
    def generate_payroll(self, Payroll):
        try:
            self.cursor.execute(
                """SELECT *
                                FROM PayRoll
                                WHERE EmployeeID=? AND PayPeriodStartDate='?'AND PayPeriodEndDate = '?'""",
                (
                    Payroll.employee_id,
                    Payroll.pay_period_start_date,
                    Payroll.pay_period_end_date,
                ),
            )
            pay_roll_data = self.cursor.fetchall()
            print(pay_roll_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_pay_roll_by_id(self, payroll_id):
        try:
            self.cursor.execute("SELECT * FROM PayRoll WHERE PayrollID=?", (payroll_id))
            pay_roll_data = self.cursor.fetchall()
            print(pay_roll_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_pay_rolls_for_employee(self, Payroll):
        try:
            self.cursor.execute(
                "SELECT * FROM PayRoll WHERE EmployeeID=?", (Payroll.employee_id)
            )
            pay_roll_data = self.cursor.fetchall()
            print(pay_roll_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_pay_rolls_for_period(self, Payroll):
        try:
            self.cursor.execute(
                """SELECT *
                                FROM PayRoll
                                WHERE PayPeriodStartDate='?'AND PayPeriodEndDate = '?'""",
                (
                    Payroll.pay_period_start_date,
                    Payroll.pay_period_end_date,
                ),
            )
            pay_roll_data = self.cursor.fetchall()
            print(pay_roll_data)
            self.conn.commit()
        except Exception as e:
            print(e)
