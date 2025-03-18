#database configurations

DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'Mike'
DATABASE_NAME = 'JobsDB'

connection_string = f"DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;"