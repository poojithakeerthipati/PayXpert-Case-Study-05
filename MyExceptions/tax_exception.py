class TaxCalculationException(Exception):
    def __init__(self, employee_id):
        super().__init__(f"Tax with {employee_id} was not calculated")
