from tabulate import tabulate
from Util.DBConn import DBConnection
from abc import ABC, abstractmethod


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
    def add_financial_record(self, FinancialRecord):
        try:
            self.cursor.execute(
                "INSERT INTO FinancialRecord(RecordDate=GETDATE(), Description, Amount, RecordType) VALUES=(?,?,?)",
                (
                    FinancialRecord.description,
                    FinancialRecord.amount,
                    FinancialRecord.record_type,
                ),
            )
            record_data = self.cursor.fetchall()
            print(record_data)
        except Exception as e:
            print(e)

    def get_financial_record_by_id(self, record_id):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE RecordID=?", (record_id)
            )
            record_data = self.cursor.fetchall()
            print(record_data)
        except Exception as e:
            print(e)

    def get_financial_records_for_employee(self, Financialrecord):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE EmployeeID=?",
                (Financialrecord.employee_id),
            )
            record_data = self.cursor.fetchall()
            print(record_data)
        except Exception as e:
            print(e)

    def get_financial_records_for_date(self, FinancialRecord):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE RecordDate=?",
                (FinancialRecord.record_date),
            )
            record_data = self.cursor.fetchall()
            print(record_data)
        except Exception as e:
            print(e)
