import admin, student, instructor, question, exam
from databaseConnector import  connector
conn = connector()

def check_student(userName,password):
    cursor = conn.cursor()
    cursor.execute("check_student ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            return val
        
def check_instructor(userName,password):
    cursor = conn.cursor()
    cursor.execute("check_instructor ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            return val
        
        
def check_admin(userName,password):
    cursor = conn.cursor()
    cursor.execute(" check_admin ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            return val
        
def initializing():
    option= int( input("wlecome to Examination-system\n-------------------------------\nTo log in press 1 \nTo sign up press 2\n"))
    option = int(option)
    if option == 1:
        loginMenu()
    elif option == 2: # in student table
        print("please enter your first name")
        fname = input()
        print("please enter your last name")
        lname = input()
        print("please enter your username")
        username = input()
        print("please enter your password")
        password = input()
        cursor = conn.cursor()
        cursor.execute(
        "insert into student(FirstName,LastName, username, password) values (?,?,?,?);",
         (fname,lname, username, password)   
            )
        conn.commit()
        
        loginMenu()

def loginMenu():
  type= int( input("wlecome to Examination-system\n-------------------------------\nchoose ur type to login\n1-Admin\n2-instructor\n3-Student\n") )
  while type>3 or type<1:
    type= int (input("invalid type please try again"))
    
    
    username=input("username: ")
    password=input("password: ")
        
    if type == 1:
        check = check_admin(username,password)
        if check != 0:
            adminUser()
        else:
            print("\nplease try again\n")
            loginMenu()
        # adminUser()
    elif type == 2:
        check = check_instructor(username,password)
        if check != 0:
            instructorUser()
        else:
            print("\nplease try again\n")
            loginMenu()
    elif type == 3:
        stdID = check_student(username,password)
        if stdID != 0:
            studentUser(stdID)
        else:
            print("\nplease try again\n")
            loginMenu()

def studentUser(stdID):
    flag= True
    while flag:
        print("PRESS 1:\n\tTo enroll new course. \nPRESS 2:\n\tTo get your approved courses. \nPRESS 3:\n\tTo take exam\nPRESS 4:\n\tTo get your grades.\nPRESS 0:\n\tTo LOGOUT")
        userFunction = int(input())
        st1=student.Student(stdID,"a")
        if userFunction == 1:
            crsName = input(" insert the course name.\n\t>>")
            st1.enroll(crsName)
        elif userFunction == 2:
            st1.getCourses()
        elif userFunction == 3:
            examID = int(input("Please insert the exam id\n\t>>"))
            st1.takeExam(examID)
        elif userFunction==4:
            st1.getGrades()
        elif userFunction==0:
            flag= False
            loginMenu()
        else:
            print("please choose 1, 2, 3 or 4")

def adminUser():
    ad1= admin.Admin("a")
    flag= True
    while flag:
        print("PRESS 1:\n\tTo add new course, \nPRESS 2:\n\tTo edit course, \nPRESS 3:\n\tTo delete course, \nPRESS 4:\n\tinsert new instructor, \nPRESS 5:\n\tTo edit instructor. \nPRESS 6:\n\tTo delete instructor. \nPRESS 7:\n\tTo Approve courses \nPRESS 8:\n\tTo generate report.\nPRESS 0:\n\tTo LOGOUT")

        userFunction = int(input())
        if userFunction == 1:
            courseName = input("Insert the course name")
            insID = input("Insert the associated instructorID with this course")
            ad1.addCourse(courseName, insID)
        elif userFunction == 2:
            old = input("please insert the course name you want to change")
            new = input("please insert the new course name")
            ad1.editCourseName(old, new)
        elif userFunction == 3:
            courseName = input("please insert the course name")
            ad1.deleteCourse(courseName)
        elif userFunction == 4:
            print("Please Fill the following:\n")
            InstructorFName = input("Instructor's First name: ")
            InstructorLName = input("Instructor's Last name: ")
            userName = input("Instructor's Username: ")
            password = input("Instructor's Password: ")
            ins1 = instructor.Instrucor(InstructorFName, InstructorLName, userName, password)
            ad1.addInstructor(ins1.fname, ins1.lname, ins1.username, ins1.password)
        elif userFunction == 5:
            InstructorID = input("please insert the instructor id")
            InstructorName = input("please insert the instructor name")
            ad1.editInstructorUsername(InstructorID, InstructorName)
        elif userFunction == 6:
            InstructorID = input("please insert the instructor id")
            ad1.deleteInstructor(InstructorID)
        elif userFunction == 7:
            ad1.approveDeclineStudents()
        elif userFunction == 8:
            ad1.generateReport()
        elif userFunction == 0:
            flag = False
            loginMenu()
        else:
            print("please select a number from 1 to 8 or PRESS 0 to LOGOUT")
            adminUser()
   
def instructorUser():
    flag=True
    while flag:
        print("PRESS 1:\n\tTo add new question.\nPRESS 2:\n\tTo Generate exam.\nPRESS 3:\n\tTo LOGOUT")
        userInput = int(input())
        if userInput == 1:
            fillQuestion()
        elif userInput == 2:
            GenerateExam()
        elif userInput == 3:
            flag = False
    return
    


def fillQuestion():
    ins1 = instructor.Instrucor("a")
    print("Please Enter the following:\n ")
    crsID = input("Course id: ")
    questionBody = input("Question body:\n >> ")
    choiceA = input(" - choice A: ")
    choiceB = input(" - choice B: ")
    choiceC = input(" - Choice C: ")
    choiceD = input(" - Choice D: ")
    correctAns = input("The Correct Answer: ")
    ques = question.Question(questionBody, crsID, choiceA, choiceB, choiceC, choiceD, correctAns)
    ins1.addQuestion(ques)

def GenerateExam():
    ins1 = instructor.Instrucor("a")
    crsID = int(input("please enter the course id"))
    NumOfQuestion = input("please enter the number of questions")
    exam1 = exam.Exam(crsID, NumOfQuestion)
    ins1.generateExam(exam1)

initializing()
