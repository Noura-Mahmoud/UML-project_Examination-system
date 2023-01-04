from databaseConnector import connector
conn = connector()

import person as p 
class Instrucor(p.Person):
  def __init__(self, name, id):
    p.Person.__init__(self, name)
    self.courses = []
    self.id = id
  
  def getExamId(self):
    cursor = conn.cursor()
    cursor.execute("select top 1 ExamID from Exam order by ExamID desc;")
    for row in cursor:
        print(row)
        for val in row:
          print("the exam id is: ?", (val))
    
  def generateExam(self, exam):
    cursor = conn.cursor()
    cursor.execute("generateExam ?,?;",(exam.courseID,exam.NumOfQuestion))
    conn.commit()
    # return examid of the generated exam
    self.getExamId()
    
  def addQuestion(self,ques):
    cursor = conn.cursor()
    cursor.execute("addQuestion ?,?,?,?,?,?,?;",(ques.questionBody, ques.crsID, ques.choiceA, ques.choiceB, ques.choiceC, ques.choiceD, ques.correctAns))
    conn.commit()
    
  # def loadCourseList(self):
  #   cursor = conn.cursor()
  #   cursor.execute("select crsID from course where insID = ?;", (self.id))
  #   for row in cursor:
  #       # print(row)
  #       for val in row:
  #         self.courses.append(val)

# #connec to database
# conn = pyodbc.connect(
#         "Driver={SQL Server Native Client 11.0};"
#         "Server=Mikasa;"
#         "Database=Examination_System;"
#         "Trusted_Connection=yes;"
#     )


