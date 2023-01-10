import person as p
from databaseConnector import *

conn = connector()


class Student(p.Person):
    def __init__(self, stdID, firstName, lastName = "", username="", password=""):
        p.Person.__init__(self, firstName, lastName, username, password)
        self.stdID = stdID
        self.firstName = firstName
        self.lastName = lastName

    def enroll(self, crsName):
        cursor = conn.cursor()
        cursor.execute("EXEC EnrollStudentByCourseName @stdID = ?, @crsName = ?", self.stdID, crsName)
        cursor.commit()

    def get_exam_info(self, examID):
        cursor = conn.cursor()
        cursor.execute("EXEC GetExamInfo @examID = ?", examID)
        exam_info = cursor.fetchone()
        print("=======================")
        print("Exam Description: " + exam_info.ExamDescription)
        print("Exam Duration: " + str(exam_info.ExamDurationMinutes) + " minutes")
        print("Course: " + exam_info.CrsName)
        print("=======================")

    def get_exam_questions(self, examID):
        cursor = conn.cursor()
        cursor.execute("EXEC GetExam @examID = ?", examID)
        columns = [column[0] for column in cursor.description]
        questions = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        return questions


    def answer_questions(self, questions):
        for question in questions:
            print('\n'+question['question'])
            print("A. " + question['A'])
            print("B. " + question['B'])
            print("C. " + question['C'])
            print("D. " + question['D'])
            studentChoice = input("Choose the appropriate letter A, B, C or D: ")
            studentChoice = studentChoice.capitalize()
            cursor = conn.cursor()
            cursor.execute("EXEC SolveQuestion @stdID = ?, @quesID = ?, @answer = ?", self.stdID, question['quesID'],
                          question[studentChoice])
            cursor.commit()
        print("=============================")
        print("Exam submitted successfully!")
    

    def takeExam(self, examID):
        self.get_exam_info(examID)
        questions = self.get_exam_questions(examID)
        self.answer_questions(questions)
        self._correctExam(examID)

    def getCourses(self, return_data=False):
        cursor = conn.cursor()
        cursor.execute("EXEC GetApprovedCourses @stdID = ?", self.stdID)
        rows = cursor.fetchall()
        field_names = ["Course Name"]
        data = [field_names] + [[row.CrsName] for row in rows]

        if return_data:
            return data
        else:
            table = array_to_table(data)
            print(table)

    def getGrades(self, return_data=False):
        cursor = conn.cursor()
        cursor.execute("EXEC GetStudentGrades @stdID = ?", self.stdID)
        rows = cursor.fetchall()
        field_names = ["Course Name", "Exam Description", "Grade"]
        data = [field_names] + [[row.CrsName, row.ExamDescription, row.grade] for row in rows]

        if return_data:
            return data
        else:
            table = array_to_table(data)
            print(table)

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

    def _correctExam(self,examID):
        cursor = conn.cursor()
        cursor.execute("EXEC storeStudentGrades ?, ?", self.stdID, examID)
        cursor.commit()



    # def checkExamAnswers(self, examID, return_data=False):
    #     cursor = conn.cursor()
    #     cursor.execute("EXEC CheckExamAnswers @stdID = ?, @examID = ?", self.stdID, examID)
    #     rows = cursor.fetchall()
    #     field_names = ["Question ID", "Solved"]
    #     data = [field_names] + [[row.quesID, row.result] for row in rows]
    #     if return_data:
    #         return data
    #     else:
    #         table = array_to_table(data)
    #         print(table)
    #
    # def countCorrectAnswers(self, examID):
    #     data = self.checkExamAnswers(examID, return_data=True)
    #     true_count = 0
    #     for row in data[1:]:
    #         if row[1] == "true":
    #             true_count += 1
    #     total_count = len(data) - 1  # Subtract 1 to account for the field names row
    #     percentage = true_count / total_count * 100
    #     percentage_rounded = round(percentage)
    #     return percentage_rounded


# s1 = Student(1,"a")
# s1.takeExam(13)