import pyodbc

#connec to database
def connector():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "server=Youssef;"
        "Database=ExaminationSystem;"
        "Trusted_Connection=yes;"
    )
    return conn
