class FinancialRecordException(Exception):
    def __init__(self):
        super().__init__(f"Cant get the record as it was not found")
