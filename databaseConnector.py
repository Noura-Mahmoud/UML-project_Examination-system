import pyodbc
from prettytable import PrettyTable


#connect to database
def connector():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "server=Mikasa;"
        "Database=ExaminationSystem;"
        "Trusted_Connection=yes;"
    )
    return conn

#print tables in a pretty shape:
def create_table(rows, field_names):
    # Create a table to hold the data
    table = PrettyTable()
    table.field_names = field_names

    # Iterate through the rows and add them to the table
    for row in rows:
        table.add_row(row)

    return table

def array_to_table(array):
    # Get the field names from the first row of the array
    field_names = array[0]

    # Create a table with the field names
    table = PrettyTable(field_names)

    # Iterate through the rest of the rows and add them to the table
    for row in array[1:]:
        table.add_row(row)

    return table