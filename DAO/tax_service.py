from Util.DBConn import DBConnection
from abc import ABC, abstractmethod
from tabulate import tabulate


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
    def calculate_tax(self, Tax):
        try:
            tax_rate = 0.2
            self.cursor.execute(
                "SELECT TaxableIncome FROM Tax WHERE EmployeeID=? AND TaxYear=?",
                (Tax.employee_id, Tax.tax_year),
            )
            taxable_income = self.cursor.fetchone()[0]
            if taxable_income:
                tax_amount = taxable_income * tax_rate
                return tax_amount
            else:
                print("Not found")
                return None
        except Exception as e:
            print(e)

    def get_tax_by_id(self, tax_id):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxID=?", (tax_id))
            tax_data = self.cursor.fetchall()
            print(tax_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_tax_for_employee(self, Tax):
        try:
            self.cursor.execute(
                "SELECT * FROM Tax WHERE EmployeeID=?", (Tax.employee_id)
            )
            tax_data = self.cursor.fetchall()
            print(tax_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_tax_for_year(self, Tax):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxYear=?", (Tax.tax_year))
            tax_data = self.cursor.fetchall()
            print(tax_data)
            self.conn.commit()
        except Exception as e:
            print(e)
