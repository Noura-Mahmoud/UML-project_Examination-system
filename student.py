import person as p 
from databaseConnector import connector
conn = connector()


class Student(p.Person):
  def __init__(self, name):
    p.Person.__init__(self, name)
    self.grades = dict()
    
  def enroll(courseID):
    pass
    # bussiness to add this to database with "waiting" status
  
  def takeExam(examID):
    pass
    # view exam for the student and take his answers
    
  def getGrades(self, stdID):
    cursor = conn.cursor()
    cursor.execute(
        "GetStudentGrades ?",
         (stdID)   
        )
        
    for row in cursor:
         print(row)
  
  def getApprovedCourses():
        cursor = conn.cursor()
        cursor.execute(
            "GetStudentGrades ?",
            (stdID)   
            )
            
        for row in cursor:
            print(row)
  
  
  
    

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Student("John", 36)

# print(p1) 

s1 = Student("a")
print(s1.Name)
s1.getGrades(2)