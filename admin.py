import person as p 
from databaseConnector import array_to_table, connector
from prettytable import PrettyTable
from rep_menu import reportClass
conn = connector()



class Admin(p.Person):
    def __init__(self, name):
        p.Person.__init__(self, name)

    def addCourse(self, course_name, ins_id):
          cursor = conn.cursor()
          cursor.execute(
                "insert into course(CrsName,insID) values (?,?);",
                (course_name,ins_id)   
                )
          conn.commit()

    def deleteCourse(self, course_name):
          cursor = conn.cursor()
          cursor.execute(
                "DELETE FROM course WHERE crsName = ? ;",
                (course_name)   
                )
          conn.commit()

    def editCourseName(self,oldCourseName,newCourseName):
        cursor = conn.cursor()
        cursor.execute(
                "UPDATE course SET crsName = ? WHERE crsName = ?;",
                (newCourseName,oldCourseName)   
                )
        conn.commit()

    def addInstructor(self, firstName, secondName, username, password):
         cursor = conn.cursor()
         cursor.execute(
                "insert into instructor values (?,?,?,?);",
                (firstName, secondName, username, password)   
                )
         conn.commit()

    def editInstructorUsername(self, InstructorID, username):
            cursor = conn.cursor()
            cursor.execute(
                  "UPDATE instructor SET username = ? WHERE insID = ?;",
                  (username,InstructorID)   
                  )
            conn.commit()
            

    def deleteInstructor(self, instructorID):
         cursor = conn.cursor()
         cursor.execute(
                "DELETE FROM instructor WHERE insID = ? ;",
                (instructorID)   
                )
         conn.commit()



    def approveDeclineStudents(self):
            cursor = conn.cursor()
            cursor.execute("getNumOfStudentsWithPendingCourses")
            NumOfStudentsWithPendingCourses = cursor.fetchone()[0]   
            print("There's "+ str(NumOfStudentsWithPendingCourses) + " students with pending courses")
            cursor.execute("getPendingCoursesTable")
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["stdID", "Num of pending courses"]
            for row in rows:
                  table.add_row([row[0], row[1]])
            print(table)

            stdIDs = input("Enter stdIDs SEPERATED BY a comma to see their pending courses: ")
            #stdIDs = stdIDs.split(',')
            print(stdIDs)
            cursor.execute("getPendingCoursesByStdID ?" ,(stdIDs))
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["Row#","stdID","CrsName","crsID","state"]
            for row in rows:
                   table.add_row([row[0], row[1], row[2], row[3], row[4]])
            print(table)
            rowToUpdate = input("Enter the number of rows you wish to update  SEPERATED BY a comma: ")
            rowToUpdate = [int(x) for x in rowToUpdate.split(",")]

            for i in rowToUpdate:
                  cursor.execute("ApproveCourse ?,?" ,(rows[i-1][1],rows[i-1][3]))
           
            conn.commit()

    def generateReport(self):
          r1 = reportClass()
          r1.menu()
            

# adm1 = Admin("admin")

# adm1.approveDeclineStudents()
# adm1.addCourse("OOP",3)
# adm1.editCourseName("OOP","hamada")
# adm1.deleteCourse("hamada")

# adm1.addInstructor("Hamada","Helal","hamd","lol")
# adm1.deleteInstructor(6)