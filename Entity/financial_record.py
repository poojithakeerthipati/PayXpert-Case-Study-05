class FinancialRecord:
    def __init__(self, employee_id, record_date, description, amount, record_type):
        self.employee_id = employee_id
        self.record_date = record_date
        self.description = description
        self.amount = amount
        self.record_type = record_type
