
make 5 insert statements to std_answers related to the data below
CREATE TABLE std_answers
(
    stdID int,
    quesID int,
    answer varchar(50),
    PRIMARY KEY (stdID, quesID),
    FOREIGN KEY (stdID) REFERENCES student(stdID),
    FOREIGN KEY (quesID) REFERENCES question(quesID)
);


INSERT INTO student (FirstName, LastName, username, password)
VALUES ('John', 'Doe', 'johndoe123', 'password123'),
('Jane', 'Doe', 'janedoe456', 'password456'),
('Bob', 'Smith', 'bobsmith789', 'password789'),
('Sally', 'Johnson', 'sallyj123', 'password123'),
('Tom', 'Brown', 'tombrown456', 'password456');

INSERT INTO instructor (FirstName, LastName, username, password)
VALUES ('Mark', 'Williams', 'markw123', 'password123'),
('Emma', 'Jones', 'emmaj456', 'password456'),
('Kevin', 'Smith', 'kevins789', 'password789'),
('Ashley', 'Johnson', 'ashleyj123', 'password123'),
('Mike', 'Brown', 'mikebrown456', 'password456');

INSERT INTO Admin (FirstName, LastName, username, password)
VALUES ('Adam', 'Smith', 'adamsmith123', 'password123'),
('Emily', 'Jones', 'emilyj456', 'password456'),
('Brian', 'Williams', 'brianw789', 'password789'),
('Samantha', 'Johnson', 'samanthaj123', 'password123'),
('Chris', 'Brown', 'chrisbrown456', 'password456');

INSERT INTO course (CrsName, insID)
VALUES ('Mathematics', 1),
('Biology', 2),
('Computer Science', 3),
('Physics', 4),
('Chemistry', 5);

INSERT INTO std_course (stdID, crsID)
VALUES (1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO Exam (ExamDescription, ExamDurationMinutes, crsID)
VALUES ('Midterm Exam', 60, 1),
('Final Exam', 90, 2),
('Quiz 1', 30, 3),
('Quiz 2', 45, 4),
('Homework', 15, 5);

INSERT INTO Question (question, crsID)
VALUES ('What is the capital of France?', 1),
('How does photosynthesis work?', 2),
('What is the syntax for a for loop in Java?', 3),
('What is the formula for finding the area of a triangle?', 4),
('What is the boiling point of water in degrees Celsius?', 5);

INSERT INTO Choices (A, B, C, D, correctAnswer, quesID)
VALUES ('Paris', 'Berlin', 'London', 'Rome', 'Paris', 1),
('Carbon dioxide is converted into glucose', 'Glucose is converted into oxygen', 'Oxygen is converted into carbon dioxide', 'Carbon dioxide is converted into oxygen', 'Carbon dioxide is converted into glucose', 2),
('for (int i = 0; i < 10; i++)', 'for (i = 0; i < 10; i++)', 'for i in range(10)', 'for (i <= 10; i++)', 'for (int i = 0; i < 10; i++)', 3),
('A = bh/2', 'A = s(s-a)(s-b)(s-c)', 'A = (b+c)h/2', 'A = bh', 'A = bh/2', 4),
('0 degrees Celsius', '100 degrees Celsius', '32 degrees Fahrenheit', '212 degrees Fahrenheit', '100 degrees Celsius', 5);

INSERT INTO student_exam (examID, stdID, grade)
VALUES (1, 1, 85),
(2, 2, 92),
(3, 3, 73),
(4, 4, 95),
(5, 5, 60);


INSERT INTO std_answers (stdID, quesID, answer) VALUES (1, 1, 'Paris');
INSERT INTO std_answers (stdID, quesID, answer) VALUES (2, 2, 'Carbon dioxide is converted into glucose');
INSERT INTO std_answers (stdID, quesID, answer) VALUES (3, 3, 'for (int i = 0; i < 10; i++)');
INSERT INTO std_answers (stdID, quesID, answer) VALUES (4, 4, 'A = bh/2');
INSERT INTO std_answers (stdID, quesID, answer) VALUES (5, 5, '100 degrees Celsius');

