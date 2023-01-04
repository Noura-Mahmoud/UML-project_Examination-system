import pyodbc
import admin, student, instructor

conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=Mikasa;"
        "Database=ExaminationSystem;"
        "Trusted_Connection=yes;"
        "MARS_Connection=Yes"
    )
def check_student(userName,password):
    cursor = conn.cursor()
    cursor.execute("check_student ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            print(val)
            return val
        
def check_instructor(userName,password):
    cursor = conn.cursor()
    cursor.execute("check_instructor ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            print(val)
            return val
        
        
def check_admin(userName,password):
    cursor = conn.cursor()
    cursor.execute(" check_admin ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            print(val)
            return val
        
def initializing():
    # print("To log in press 1 \nTo sign up press 2")
    option = input("To log in press 1 \nTo sign up press 2\n")# parse int
    # option = int(input())
    option = int(option)
    if option == 1:
        # print("please enter your username")
        # username = input()
        # print("please enter your password")
        # password = input()
        # print("please enter your role, whether you are student, instructor or admin")
        # role = input()
        print(option)
        loginMenu()
    elif option == 2: # in student table
        print("please enter your username")
        username = input()
        print("please enter your password")
        password = input()
        # signUp(username, password)
        # initializing() # to login after sign up
        
def loginMenu():
  type= int( input("wlecome to Examination-system\n-------------------------------\nchoose ur type to login\n1-Admin\n2-instructor\n3-Student\n") )
  while type>3 or type<1:
    type= int (input("invalid type please try again"))
    
    
  username=input("user name:")
  password=input("user password:")
    
  if type == 1:
      check = check_admin(username,password)
      if check != 0:
        adminUser()
    # adminUser()
  elif type == 2:
      check = check_instructor(username,password)
      if check != 0:
        instructorUser()
  elif type == 3:
      stdID = check_student(username,password)
      if stdID != 0:
        studentUser(stdID)
    # check_student(username,password)
    # stdID = check_student(username,password)
    # studentUser(stdID)
        
  

def studentUser(stdID):
    print("if you want to enroll new course press 1, get approved courses press 2 or take exam press 3")
    userFunction = int(input())
    # userFunction = input()
    st1=student.Student("a")
    if userFunction == 1:
        print("please insert the exam id")
        # crsID = input()
        crsID = int(input())
        st1.enroll(crsID)
    elif userFunction == 2:
        st1.getApprovedCourses(stdID)
    elif userFunction == 3:
        print("please insert the exam id")
        # examID = input()
        examID = int(input())
        st1.takeExam(examID)
        
        

def adminUser():
    print("if you want to add new course press 1, \nedit course press 2, \ndelete course press 3, \ninsert new instructor press 4, \nedit instructor press 5, \ndelete instructor press 6, \nto decide student state in a specific course press 7 \nor generate report press 8")
    # userFunction = input()
    ad1= admin.Admin("a")
    userFunction = int(input())
    if userFunction == 1:
        print("please insert the course name")
        courseName = input()
        ad1.addCourse(courseName)
    elif userFunction == 2:
        print("please insert the course id")
        courseID = input()
        print("please insert the new course name")
        courseName = input()
        ad1.editCourse(courseID, courseName)
    elif userFunction == 3:
        print("please insert the course id")
        courseID = input()
        ad1.deleteCourse(courseID)
    elif userFunction == 4:
        print("please insert the instructor name")
        InstructorName = input()
        ad1.addInstructor(InstructorName)
    elif userFunction == 5:
        print("please insert the instructor id")
        InstructorID = input()
        print("please insert the instructor name")
        InstructorName = input()
        ad1.editInstructor(InstructorID, InstructorName)
    elif userFunction == 6:
        print("please insert the instructor id")
        InstructorID = input()
        ad1.deleteInstructor(InstructorID)
    elif userFunction == 7:
        print("please insert the student id")
        stdID = input()
        print("please insert the course id")
        crsID = input()
        print("please insert your decision 'approved' or 'declined'")
        decision = input()
        ad1.approveDeclineStudents(stdID, crsID, decision)
    elif userFunction == 8:
        ad1.generateReport()
        
        

def instructorUser():
    print("if you want to add new question press 1, \ngenerate exam press 2")
    # userFunction = input()
    userFunction = int(input())
    ins1 = instructor.Instrucor("a")
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
        ins1.addQuestion(questionBody, crsID, choiceA, choiceB, choiceC, choiceD, correctAns)
    elif userFunction == 2:
        print("please enter the course id")
        # crsID = input()
        crsID = int(input())
        print("please enter the number of questions")
        NumOfQuestion = input()
        ins1.generateExam(crsID, NumOfQuestion)
    
    
initializing()

# cursor = conn.cursor()
# cursor.execute(" select * from student where stdID = 1;")
# for row in cursor:
#     for val in row:
#         print("val")
#         print(val)
#     print("row")
#     print(row)