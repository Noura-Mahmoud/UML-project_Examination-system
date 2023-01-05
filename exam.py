from databaseConnector import *

conn = connector()


class Exam():
    def __init__(self, examID, courseID="", NumOfQuestion=""):
        self.examID = examID
        self.question =[]
        self.courseID =courseID
        self.NumOfQuestion =NumOfQuestion
        self.description = " "
        self.duration = " "

    def checkExamAnswers(self, stdID, return_data=False):
        cursor = conn.cursor()
        cursor.execute("EXEC CheckExamAnswers @stdID = ?, @examID = ?", stdID, self.examID)
        rows = cursor.fetchall()
        field_names = ["Question ID", "Solved"]
        data = [field_names] + [[row.quesID, row.result] for row in rows]
        if return_data:
            return data
        else:
            table = array_to_table(data)
            print(table)

    def countCorrectAnswers(self,stdID):
        data = self.checkExamAnswers(stdID, return_data=True)
        true_count = 0
        for row in data[1:]:
            if row[1] == "true":
                true_count += 1
        total_count = len(data) - 1  # Subtract 1 to account for the field names row
        percentage = true_count / total_count * 100
        percentage_rounded = round(percentage)
        return percentage_rounded

# exam = Exam(1)
# percentage = exam.countCorrectAnswers(1)
# print(f"The student got {percentage}% of the answers correct.")
