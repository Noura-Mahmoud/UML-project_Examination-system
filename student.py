import person as p
from databaseConnector import *

conn = connector()


class Student(p.Person):
    def __init__(self, stdID, firstName, lastName):
        self.stdID = stdID
        self.firstName = firstName
        self.lastName = lastName

    def enroll(self, crsName):
        cursor = conn.cursor()
        cursor.execute("EXEC EnrollStudentByCourseName @stdID = ?, @crsName = ?", self.stdID, crsName)

    def takeExam(examID):
        pass
        # view exam for the student and take his answers

    def get_data(self, data_type, return_data=False):
        cursor = conn.cursor()
        # Execute the stored procedure
        if data_type == "grades":
            cursor.execute("EXEC GetStudentGrades @stdID = ?", self.stdID)
            # Fetch all rows returned by the stored procedure
            rows = cursor.fetchall()
            # Create a 2D array with the rows and column values
            field_names = ["Course Name", "Exam Description", "Grade"]
            data = [field_names] + [[row.CrsName, row.ExamDescription, row.grade] for row in rows]
        elif data_type == "courses":
            cursor.execute("EXEC GetApprovedCourses @stdID = ?", self.stdID)
            # Fetch all rows returned by the stored procedure
            rows = cursor.fetchall()
            # Create a 2D array with the rows and column values
            field_names = ["Course Name"]
            data = [field_names] + [[row.CrsName] for row in rows]

        if return_data:
            return data
        else:
            table = array_to_table(data)
            print(table)
    #
    # def getGrades(self, stdID):
    #     cursor = conn.cursor()
    #     # Execute the stored procedure
    #     cursor.execute("EXEC GetStudentGrades @stdID = ?", stdID)
    #
    #     # Fetch all rows returned by the stored procedure
    #     rows = cursor.fetchall()
    #
    #     # Create a 2D array with the rows and column values
    #     field_names = ["Course Name", "Exam Description", "Grade"]
    #     grades = [field_names] + [[row.CrsName, row.ExamDescription, row.grade] for row in rows]
    #
    #     return grades
    #
    # def printGrades(self, stdID):
    #     grades = self.getGrades(stdID)
    #     table = array_to_table(grades)
    #     print(table)
    #
    # def printApprovedCourses(self, stdID):
    #     cursor = conn.cursor()
    #     # Execute the stored procedure
    #     cursor.execute("EXEC GetApprovedCourses @stdID = ?", stdID)
    #
    #     # Fetch all rows returned by the stored procedure
    #     rows = cursor.fetchall()
    #
    #     # Create the table
    #     field_names = ["Course Name"]
    #     table = create_table(rows, field_names)
    #
    #     # Print the table
    #     print(table)
    #
    #
    # def getCourses(self, stdID):
    #     cursor = conn.cursor()
    #     # Execute the stored procedure
    #     cursor.execute("EXEC GetApprovedCourses @stdID = ?", stdID)
    #
    #     # Fetch all rows returned by the stored procedure
    #     rows = cursor.fetchall()
    #
    #     # Create a 2D array with the rows and column values
    #     field_names = ["Course Name"]
    #     courses = [field_names] + [[row.CrsName] for row in rows]
    #
    #     return courses
    #
    # def printCourses(self, stdID):
    #     courses = self.getCourses(stdID)
    #     table = array_to_table(courses)
    #     print(table)


#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Student("John", 36)

# print(p1)

s1 = Student(1,"Ahmed","Kamal")
s1.get_data("grades")
