from databaseConnector import connector
conn = connector()

import person as p 
class Admin(p.Person):
    def __init__(self, id, name):
        p.Person.__init__(self, id, name)
        
    def addCourse(crs):
        pass
    
    def editCourse(courseID, courseName):
        pass
        
    def deleteCourse(courseID):
        pass
        
    def addInstructor(ins):
        pass
    
    def editInstructor(InstructorID, InstructorName):
        pass
        
    def deleteInstructor(InstructorID):
        pass
    
    def approveDeclineStudents():
        pass
    
    def generateReport():
        pass
    