import person as p 
from databaseConnector import connector
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

    def editInstructor(self, instructor):
        # code to edit an instructor
        pass

    def deleteInstructor(self, instructorID):
         cursor = conn.cursor()
         cursor.execute(
                "DELETE FROM instructor WHERE insID = ? ;",
                (instructorID)   
                )
         conn.commit()


adm1 = Admin("admin")

# adm1.addCourse("OOP",3)
# adm1.editCourseName("OOP","hamada")
# adm1.deleteCourse("hamada")

# adm1.addInstructor("Hamada","Helal","hamd","lol")
# adm1.deleteInstructor(6)