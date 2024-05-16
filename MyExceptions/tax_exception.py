class TaxCalculationException(Exception):
    def __init__(self, tax_id):
        super().__init__(f"employee with {tax_id} was not found")
