----------------------------------------------
--STUDENT
----------------------------------------------
select * from student
CREATE TABLE std_answers
(
    stdID int,
    quesID int,
    answer varchar(50),
    PRIMARY KEY (stdID, quesID),
    FOREIGN KEY (stdID) REFERENCES student(stdID),
    FOREIGN KEY (quesID) REFERENCES question(quesID)
);


--Procedure to Enroll Student in a course using ID

CREATE PROCEDURE EnrollStudent
    @stdID int,
    @crsID int
AS
BEGIN
    INSERT INTO std_course (stdID, crsID, state)
    VALUES (@stdID, @crsID, 'Pending')
END

--Procedure to Enroll Student in a course using course name

CREATE PROCEDURE EnrollStudentByCourseName
    @stdID int,
    @crsName varchar(50)
AS
BEGIN
    DECLARE @crsID int
    
    SELECT @crsID = crsID
    FROM course
    WHERE CrsName = @crsName
    
    INSERT INTO std_course (stdID, crsID, state)
    VALUES (@stdID, @crsID, 'Pending')
END

--Procedure to Get Approved courses for a certain student :

CREATE PROCEDURE GetApprovedCourses
    @stdID int
AS
BEGIN
    SELECT C.CrsName
    FROM course C
    INNER JOIN std_course SC ON SC.crsID = C.crsID
    WHERE SC.state = 'Approved' AND SC.stdID = @stdID
END

--Get grades in all exams :
CREATE PROCEDURE GetStudentGrades
    @stdID int
AS
BEGIN
    SELECT C.CrsName, E.ExamDescription, SE.grade
    FROM student_exam SE
    INNER JOIN exam E ON SE.examID = E.ExamID
    INNER JOIN course C ON E.crsID = C.crsID
    WHERE SE.stdID = @stdID
END

--takeExam sutff ??

CREATE PROCEDURE GetExam
    @examID int
AS
BEGIN
    SELECT Q.question, C.A, C.B, C.C, C.D
    FROM exam_question EQ
    INNER JOIN question Q ON EQ.quesID = Q.quesID
    INNER JOIN choices C ON Q.quesID = C.quesID
    WHERE EQ.examID = @examID
END

CREATE PROCEDURE GetExamInfo
    @examID int
AS
BEGIN
    SELECT E.ExamDescription, E.ExamDurationMinutes, C.CrsName, I.FirstName + ' ' + I.LastName AS 'Instructor Name'
    FROM exam E
    INNER JOIN course C ON E.crsID = C.crsID
    INNER JOIN instructor I ON C.insID = I.insID
    WHERE E.ExamID = @examID
END

CREATE PROCEDURE SolveQuestion
    @stdID int,
    @quesID int,
    @answer varchar(50)
AS
BEGIN
    INSERT INTO std_answers (stdID, quesID, answer)
    VALUES (@stdID, @quesID, @answer)
END

exec GetStudentGrades 1 ;
exec GetApprovedCourses 1;

SELECT @@SERVERNAME

-------
-- random values testing the tables
--------

INSERT INTO student (FirstName, LastName)
VALUES ('John', 'Doe'), ('Jane', 'Doe'), ('Bob', 'Smith'), ('Alice', 'Smith')

INSERT INTO instructor (FirstName, LastName)
VALUES ('Professor', 'X'), ('Professor', 'Y'), ('Professor', 'Z')

INSERT INTO admin (FirstName, LastName)
VALUES ('Admin', 'A'), ('Admin', 'B')

INSERT INTO course (CrsName, insID)
VALUES ('Math 101', 1), ('English 101', 2), ('Computer Science 101', 3)

INSERT INTO std_course (stdID, crsID, state)
VALUES (1, 1, 'Pending'), (1, 2, 'Approved'), (2, 3, 'Pending'), (3, 1, 'Approved'), (4, 2, 'Approved')

INSERT INTO exam (ExamDescription, ExamDurationMinutes, crsID)
VALUES ('Midterm Exam', 60, 1), ('Final Exam', 120, 2), ('Quiz 1', 30, 3)

INSERT INTO question (question, crsID)
VALUES ('What is 2 + 2?', 1), ('What is the capital of France?', 2), ('What is the function of the CPU in a computer?', 3)

INSERT INTO choices (A, B, C, D, correctAnswer, quesID)
VALUES ('4', '5', '6', '7', 'A', 1), ('Paris', 'London', 'Berlin', 'Rome', 'A', 2), ('Memory', 'Input/Output', 'Processing', 'Storage', 'C', 3)

INSERT INTO exam_question (examID, quesID)
VALUES (1, 1), (1, 2), (2, 3), (3, 1), (3, 2)

INSERT INTO student_exam (examID, stdID, grade)
VALUES (1, 1, 80), (1, 2, 90), (2, 3, 70), (3, 1, 85), (3, 4, 95)