----------------------------------------------
--STUDENT
----------------------------------------------
select * from student
select * from course
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

CREATE OR ALTER PROCEDURE GetExam
    @examID int
AS
BEGIN
    SELECT Q.quesID, Q.question, C.A, C.B, C.C, C.D
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

select * from student
getExaminfo 1
