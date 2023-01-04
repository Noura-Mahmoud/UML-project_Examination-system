----------------------------------------------
--		STUDENT AND EXAM PROCEDURES
----------------------------------------------

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

CREATE or ALTER PROCEDURE GetApprovedCourses
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


CREATE OR ALTER PROCEDURE SolveQuestion
    @stdID int,
    @quesID int,
    @answer varchar(50)
AS
BEGIN
    IF EXISTS (SELECT 1 FROM std_answers WHERE stdID = @stdID AND quesID = @quesID)
    BEGIN
        UPDATE std_answers
        SET answer = @answer
        WHERE stdID = @stdID AND quesID = @quesID;
    END
    ELSE
    BEGIN
        INSERT INTO std_answers (stdID, quesID, answer)
        VALUES (@stdID, @quesID, @answer);
    END
END




CREATE OR ALTER PROCEDURE CheckAnswer
    @stdID int,
    @quesID int
AS
BEGIN
    SELECT
        CASE WHEN sa.answer = c.correctAnswer THEN 1 ELSE 0 END AS 'Result'
    FROM std_answers sa
    INNER JOIN Choices c ON sa.quesID = c.quesID
    WHERE sa.stdID = @stdID AND sa.quesID = @quesID;
END

CREATE OR ALTER FUNCTION GetExamTable(@examID int)
RETURNS TABLE
AS
RETURN
(
    SELECT Q.quesID, Q.question, C.A, C.B, C.C, C.D
    FROM exam_question EQ
    INNER JOIN question Q ON EQ.quesID = Q.quesID
    INNER JOIN choices C ON Q.quesID = C.quesID
    WHERE EQ.examID = @examID
);

SELECT quesID FROM GetExamTable(1)


CREATE OR ALTER PROCEDURE CheckExamAnswers
    @stdID int,
    @examID int
AS
BEGIN
    SELECT sa.quesID,
        CASE WHEN sa.answer = c.correctAnswer THEN 'true' ELSE 'false' END AS 'result'
    FROM std_answers sa
    INNER JOIN Choices c ON sa.quesID = c.quesID
    WHERE sa.stdID = @stdID AND sa.quesID IN (SELECT quesID FROM getExamTable(@examID))
END



-- testing stored procedures

select * from std_answers
EXEC CheckExamAnswers @stdID = 1, @examID = 1
EXEC CheckAnswer @stdID = 1, @quesID = 1;
select * from Exam


select * from student
select * from course
EXEC GetExam @examID = 2

EXEC SolveQuestion @stdID = 1, @quesID = 1, @answer = 4
select * from std_answers
select * from Choices

TRUNCATE TABLE std_answers;

exec GetStudentGrades 1 ;
exec GetApprovedCourses 1;

SELECT @@SERVERNAME

select * from student
getExaminfo 1

EXECUTE getExam 1

SELECT * FROM getExam 1