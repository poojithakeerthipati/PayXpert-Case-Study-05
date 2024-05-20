from tabulate import tabulate
from Util.DBConn import DBConnection
from abc import ABC, abstractmethod
from MyExceptions import FinancialRecordException


class IFinancialService(ABC):
    @abstractmethod
    def add_financial_record(self, FinancialRecord):
        pass

    @abstractmethod
    def get_financial_record_by_id(self, record_id):
        pass

    @abstractmethod
    def get_financial_records_for_employee(self, Financialrecord):
        pass

    @abstractmethod
    def get_financial_records_for_date(self, FinancialRecord):
        pass


class FinancialService(DBConnection, IFinancialService):
    def add_financial_record(self, description, amount, record_type):
        try:
            self.cursor.execute(
                "INSERT INTO FinancialRecord(RecordDate=GETDATE(), Description, Amount, RecordType) VALUES=(?,?,?)",
                (
                    description,
                    amount,
                    record_type,
                ),
            )
            record_data = self.cursor.fetchall()
            if record_data:
                print(record_data)
            else:
                raise FinancialRecordException()
        except Exception as e:
            print("OOPS Error Happened")

    def get_financial_record_by_id(self, record_id):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord inner join Employee on FinancialRecord.EmployeeID = Employee.EmployeeID where RecordID=? ",
                (record_id),
            )
            record_data = self.cursor.fetchall()
            if record_data:
                print(record_data)
            else:
                raise FinancialRecordException
        except Exception as e:
            print(e)

    def get_financial_records_for_employee(self, employee_id):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord  WHERE EmployeeID=?",
                (employee_id),
            )
            record_data = self.cursor.fetchall()
            print(record_data)
        except Exception as e:
            print(e)

    def get_financial_records_for_date(self, record_date):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord inner join Employee on FinancialRecord.EmployeeID = Employee.EmployeeID WHERE RecordDate=?",
                (record_date),
            )
            record_data = self.cursor.fetchall()
            print(record_data)
        except Exception as e:
            print(e)
