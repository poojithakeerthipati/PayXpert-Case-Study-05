class DataBaseConnectionException(Exception):
    def __init__(self):
        super().__init__(f"database Connection was not given properly")
