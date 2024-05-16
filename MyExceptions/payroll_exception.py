class PayrollGenerationException(Exception):
    def __init__(self, payroll_id):
        super().__init__(
            f"Payroll can not be generated , As the employee with {payroll_id} was not found"
        )
