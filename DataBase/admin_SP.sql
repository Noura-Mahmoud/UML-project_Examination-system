
CREATE or ALTER PROC getNumOfStudentsWithPendingCourses
AS
	SELECT cast (count (*) as int) as [Num of Requests]
	FROM (
			SELECT stdID
			FROM course C
			INNER JOIN std_course SC ON SC.crsID = C.crsID
			WHERE SC.state = 'pending' 
			GROUP BY stdID) myTable

getNumOfStudentsWithPendingCourses


CREATE or ALTER PROC getPendingCoursesTable 
AS
	SELECT stdID, count (stdID) as [Num of pending courses]
	FROM course C
	INNER JOIN std_course SC ON SC.crsID = C.crsID
	WHERE SC.state = 'pending' 
	GROUP BY stdID
	


CREATE or alter PROCEDURE getPendingCoursesByStdID
	@stdID_list VARCHAR(255)
AS
BEGIN
	DECLARE @query varchar(500)
    SET @query = CONCAT('SELECT 
                            ROW_NUMBER() OVER(ORDER BY stdID ASC) AS Row#,
                            stdID,CrsName,c.crsID,state
                            FROM course C
                            INNER JOIN std_course SC ON SC.crsID = C.crsID
                            WHERE SC.state = ''pending'' 
                            AND stdID IN (', @stdID_list, ')
                            ORDER BY stdID');
    EXECUTE ( @query)
END
 


 CREATE PROC ApproveCourse
	@studentID INT,
	@courseID	INT
AS 
	UPDATE std_course
	SET state = 'Approved'
	WHERE stdID = @studentID
	AND crsID = @courseID

ApproveCourse 1,1




-- testing 
SELECT ROW_NUMBER() OVER(ORDER BY stdID ASC) AS RowNum,
                      stdID,CrsName,c.crsID,state
               FROM course C
               INNER JOIN std_course SC ON SC.crsID = C.crsID
               WHERE SC.state = 'pending' 
               ORDER BY stdID



