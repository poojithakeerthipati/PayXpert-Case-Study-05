class InvalidInputException(Exception):
    def __init__(self):
        super().__init__(f"Inavalid Input")
