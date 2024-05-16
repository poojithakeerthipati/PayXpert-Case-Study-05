from Util.DBConn import DBConnection
from abc import ABC, abstractmethod
from tabulate import tabulate
from MyExceptions import TaxCalculationException, InvalidInputException


class ITaxService(ABC):
    @abstractmethod
    def calculate_tax(self, Tax):
        pass

    @abstractmethod
    def get_tax_by_id(self, tax_id):
        pass

    @abstractmethod
    def get_tax_for_employee(self, Tax):
        pass

    @abstractmethod
    def get_tax_for_year(self, Tax):
        pass


class TaxService(DBConnection, ITaxService):
    def calculate_tax(self, employee_id, tax_year):
        try:
            tax_rate = 0.2
            self.cursor.execute(
                "SELECT TaxableIncome FROM Tax WHERE EmployeeID=? AND TaxYear=?",
                (employee_id, tax_year),
            )
            taxable_income = self.cursor.fetchone()
            if taxable_income:
                tax_amount = float(taxable_income[0]) * tax_rate
                return tax_amount
            else:
                raise TaxCalculationException(employee_id)
        except Exception as e:
            print(e)

    def get_tax_by_id(self, tax_id):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxID=?", (tax_id))
            tax_data = self.cursor.fetchall()
            if tax_data:
                print(tax_data)
            else:
                raise TaxCalculationException(tax_id)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_tax_for_employee(self, employee_id):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE EmployeeID=?", (employee_id))
            tax_data = self.cursor.fetchall()
            print(tax_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_tax_for_year(self, tax_year):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxYear=?", (tax_year))
            tax_data = self.cursor.fetchall()
            print(tax_data)
            self.conn.commit()
        except Exception as e:
            print(e)
