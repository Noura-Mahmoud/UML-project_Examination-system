import person as p 
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
    
  def getGrades(self):
    return self.grades
  
  def getApprovedCourses():
    pass
    # retrieve from database where course status id "approved"
  
  
    

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Student("John", 36)

# print(p1) 

s1 = Student("a")
print(s1.Name)