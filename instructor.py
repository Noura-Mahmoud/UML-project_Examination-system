import person as p 
class Instructor(p.Person):
  def __init__(self, name):
    p.Person.__init__(self, name)
  
  def getExamId(self,conn):
    cursor = conn.cursor()
    cursor.execute("select top 1 ExamID from Exam order by ExamID desc;")
    for row in cursor:
        print(row)
    
  def generateExam(self,conn,courseID, NumOfQuestion):
    cursor = conn.cursor()
    cursor.execute("generateExam ?,?;",(courseID,NumOfQuestion))
    conn.commit()
    # return examid of the generated exam
    self.getExamId(conn)
    
  def addQuestion(self,conn,questionBody, crsID, choiceA, choiceB, choiceC, choiceD, correctAns):
    cursor = conn.cursor()
    cursor.execute("addQuestion ?,?,?,?,?,?,?;",(questionBody, crsID, choiceA, choiceB, choiceC, choiceD, correctAns))
    conn.commit()
