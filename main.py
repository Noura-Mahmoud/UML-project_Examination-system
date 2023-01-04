import course, exam, instructor, admin, student, question
import pyodbc

def initializing():
    print("To log in press 1 \nTo sign up press 2")
    # option = input()# parse int
    option = int(input())
    if option == 1:
        print("please enter your username")
        username = input()
        print("please enter your password")
        password = input()
        print("please enter your role, whether you are student, instructor or admin")
        role = input()
        login(username, password, role)
    elif option == 2: # in student table
        print("please enter your username")
        username = input()
        print("please enter your password")
        password = input()
        signUp(username, password)
        initializing() # to login after sign up
        
def signUp():
    pass

def login():
    # print("please insert 1 if you are an admin, \n2 if you are a student \nand 3 if you are a student")
    # userType = input()
    # print("please insert your login username")
    # userName = input()
    # print("please insert your login password")
    # password = input()
    pass

def studentUser(stdID):
    print("if you want to enroll new course press 1, get approved courses press 2 or take exam press 3")
    userFunction = int(input())
    # userFunction = input()
    if userFunction == 1:
        print("please insert the exam id")
        # crsID = input()
        crsID = int(input())
        student.enroll(crsID)
    elif userFunction == 2:
        student.getApprovedCourses(stdID)
    elif userFunction == 3:
        print("please insert the exam id")
        # examID = input()
        examID = int(input())
        student.takeExam(examID)
        
def adminUser():
    print("if you want to add new course press 1, \nedit course press 2, \ndelete course press 3, \ninsert new instructor press 4, \nedit instructor press 5, \ndelete instructor press 6, \nto decide student state in a specific course press 7 \nor generate report press 8")
    # userFunction = input()
    userFunction = int(input())
    if userFunction == 1:
        print("please insert the course name")
        courseName = input()
        admin.addCourse(courseName)
    elif userFunction == 2:
        print("please insert the course id")
        courseID = input()
        print("please insert the new course name")
        courseName = input()
        admin.editCourse(courseID, courseName)
    elif userFunction == 3:
        print("please insert the course id")
        courseID = input()
        admin.deleteCourse(courseID)
    elif userFunction == 4:
        print("please insert the instructor name")
        InstructorName = input()
        admin.addInstructor(InstructorName)
    elif userFunction == 5:
        print("please insert the instructor id")
        InstructorID = input()
        print("please insert the instructor name")
        InstructorName = input()
        admin.editInstructor(InstructorID, InstructorName)
    elif userFunction == 6:
        print("please insert the instructor id")
        InstructorID = input()
        admin.deleteInstructor(InstructorID)
    elif userFunction == 7:
        print("please insert the student id")
        stdID = input()
        print("please insert the course id")
        crsID = input()
        print("please insert your decision 'approved' or 'declined'")
        decision = input()
        admin.approveDeclineStudents(stdID, crsID, decision)
    elif userFunction == 8:
        admin.generateReport()
        
def instructorUser():
    print("if you want to add new question press 1, \ngenerate exam press 2")
    # userFunction = input()
    userFunction = int(input())
    if userFunction == 1:
        print("please enter the question body")
        questionBody = input()
        print("please enter the course id")
        # crsID = input()
        crsID = int(input())
        print("please enter the choiceA")
        choiceA = input()
        print("please enter the choiceB")
        choiceB = input()
        print("please enter the choiceC")
        choiceC = input()
        print("please enter the choiceD")
        choiceD = input()
        print("please enter the correct answer")
        correctAns = input()
        instructor.addQuestion(questionBody, crsID, choiceA, choiceB, choiceC, choiceD, correctAns)
    elif userFunction == 2:
        print("please enter the course id")
        # crsID = input()
        crsID = int(input())
        print("please enter the number of questions")
        NumOfQuestion = input()
        instructor.generateExam(crsID, NumOfQuestion)
    
# response = 1
# if response != 0:

def checkInput(response):
    if response == 0: #not found
            print("please enter the correct username and password")
            login()
    elif response ==1: #admin
            adminUser()
    elif response == 2:  #instructor
            instructorUser()
    elif response == 3:  #student
            studentUser(id)
def connect():
  #connec to database
  conn = pyodbc.connect(
          "Driver={SQL Server Native Client 11.0};"
          "Server=Mikasa;"
          "Database=ExaminationSystem;"
          "Trusted_Connection=yes;"
      )
  
connect()
initializing()

