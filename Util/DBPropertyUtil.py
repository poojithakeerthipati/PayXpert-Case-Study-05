class PropertyUtil:
    @staticmethod
    def get_property_string():
        SERVER_NAME = "DESKTOP-BJQV7BU\SQLEXPRESS"
        DATABASE_NAME = "PayXpertDB1"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={SERVER_NAME};"
            f"Database={DATABASE_NAME};"
            f"Trusted_Connection=yes;"
        )
        return conn_str
