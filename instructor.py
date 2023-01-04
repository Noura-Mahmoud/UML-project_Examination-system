from databaseConnector import connector
conn = connector()

import person as p 
class Instrucor(p.Person):
  def __init__(self, name):
    p.Person.__init__(self, name)
  
  def getExamId(self):
    cursor = conn.cursor()
    cursor.execute("select top 1 ExamID from Exam order by ExamID desc;")
    for row in cursor:
        print(row)
    
  def generateExam(self,courseID, NumOfQuestion):
    cursor = conn.cursor()
    cursor.execute("generateExam ?,?;",(courseID,NumOfQuestion))
    conn.commit()
    # return examid of the generated exam
    self.getExamId()
    
  def addQuestion(self,questionBody, crsID, choiceA, choiceB, choiceC, choiceD, correctAns):
    cursor = conn.cursor()
    cursor.execute("addQuestion ?,?,?,?,?,?,?;",(questionBody, crsID, choiceA, choiceB, choiceC, choiceD, correctAns))
    conn.commit()
    

# #connec to database
# conn = pyodbc.connect(
#         "Driver={SQL Server Native Client 11.0};"
#         "Server=Mikasa;"
#         "Database=Examination_System;"
#         "Trusted_Connection=yes;"
#     )



# ins1 = Instrucor ("khaled")
# ins1.addQuestion(conn,'what is your name',1,'raneem','noura','hamada','ak','ak')
# ins1.addQuestion(conn,'what is your name',1,'raneem','noura','hamada','ak','ak')
# ins1.addQuestion(conn,'what is your name',1,'raneem','noura','hamada','ak','ak')
# ins1.addQuestion(conn,'what is your name',1,'raneem','noura','hamada','ak','ak')
# ins1.addQuestion(conn,'what is your name',1,'raneem','noura','hamada','ak','ak')
# ins1.addQuestion(conn,'what is your name',1,'raneem','noura','hamada','ak','ak')

# ins1.generateExam(conn, 1,5)

