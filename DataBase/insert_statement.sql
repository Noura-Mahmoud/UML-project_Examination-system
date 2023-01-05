INSERT INTO student (FirstName, LastName, username, password)
VALUES ('John', 'Doe', 'johndoe123', 'password123'),
('Jane', 'Doe', 'janedoe456', 'password456'),
('Bob', 'Smith', 'bobsmith789', 'password789'),
('Sally', 'Johnson', 'sallyj123', 'password123'),
('Tom', 'Brown', 'tombrown456', 'password456'), 
('Alice', 'Smith', 'alicesmith123', 'password123'),
('Sam', 'Johnson', 'samj456', 'password456'),
('Laura', 'Williams', 'lauraw789', 'password789'),
('Jason', 'Brown', 'jasonbrown123', 'password123'),
('Katie', 'Jones', 'katiej456', 'password456');

INSERT INTO instructor (FirstName, LastName, username, password)
VALUES ('Mark', 'Williams', 'markw123', 'password123'),
('Emma', 'Jones', 'emmaj456', 'password456'),
('Kevin', 'Smith', 'kevins789', 'password789'),
('Ashley', 'Johnson', 'ashleyj123', 'password123'),
('Mike', 'Brown', 'mikebrown456', 'password456'),
('Elizabeth', 'Williams', 'elizabethw123', 'password123'),
('John', 'Jones', 'johnj456', 'password456'),
('Michael', 'Smith', 'michael789', 'password789'),
('Jessica', 'Johnson', 'jessicaj123', 'password123'),
('Rob', 'Brown', 'robbrown456', 'password456');

INSERT INTO Admin (FirstName, LastName, username, password)
VALUES ('Adam', 'Smith', 'adamsmith123', 'password123'),
('Emily', 'Jones', 'emilyj456', 'password456'),
('Brian', 'Williams', 'brianw789', 'password789'),
('Samantha', 'Johnson', 'samanthaj123', 'password123'),
('Chris', 'Brown', 'chrisbrown456', 'password456'),
('Elizabeth', 'Williams', 'elizabethw123', 'password123'),
('John', 'Jones', 'johnj456', 'password456'),
('Michael', 'Smith', 'michael789', 'password789'),
('Jessica', 'Johnson', 'jessicaj123', 'password123'),
('Rob', 'Brown', 'robbrown456', 'password456');

INSERT INTO course (CrsName, insID)
VALUES ('Mathematics', 1),
('Biology', 2),
('Computer Science', 3),
('Physics', 4),
('Chemistry', 5),
('English', 6),
('History', 7),
('Geography', 8),
('Music', 9),
('Art', 10);

INSERT INTO std_course (stdID, crsID)
VALUES (1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO Exam (ExamDescription, ExamDurationMinutes, crsID)
VALUES ('Midterm Exam', 60, 1),
('Final Exam', 90, 2),
('Quiz 1', 30, 3),
('Quiz 2', 45, 4),
('Homework', 15, 5),
('Midterm Exam', 60, 6),
('Final Exam', 90, 7),
('Quiz 1', 30, 8),
('Quiz 2', 45, 9),
('Homework', 15, 10);

INSERT INTO Question (question, crsID)
VALUES ('What is the capital of France?', 1),
('How does photosynthesis work?', 2),
('What is the syntax for a for loop in Java?', 3),
('What is the formula for finding the area of a triangle?', 4),
('What is the boiling point of water in degrees Celsius?', 5),
('What is the capital of Australia?', 6),
('Who was the first president of the United States?', 7),
('What is the highest mountain in the world?', 8),
('What is the unit of frequency?', 9),
('Who painted the Mona Lisa?', 10);

INSERT INTO Choices (A, B, C, D, correctAnswer, quesID)
VALUES ('Paris', 'Berlin', 'London', 'Rome', 'Paris', 1),
('Carbon dioxide is converted into glucose', 'Glucose is converted into oxygen', 'Oxygen is converted into carbon dioxide', 'Carbon dioxide is converted into oxygen', 'Carbon dioxide is converted into glucose', 2),
('for (int i = 0; i < 10; i++)', 'for (i = 0; i < 10; i++)', 'for i in range(10)', 'for (i <= 10; i++)', 'for (int i = 0; i < 10; i++)', 3),
('A = bh/2', 'A = s(s-a)(s-b)(s-c)', 'A = (b+c)h/2', 'A = bh', 'A = bh/2', 4),
('0 degrees Celsius', '100 degrees Celsius', '32 degrees Fahrenheit', '212 degrees Fahrenheit', '100 degrees Celsius', 5),
('Sydney', 'Canberra', 'Perth', 'Melbourne', 'Canberra', 1),
('John Adams', 'George Washington', 'Thomas Jefferson', 'Benjamin Franklin', 'George Washington', 2),
('Mount Everest', 'Mount Kilimanjaro', 'Mount Fuji', 'Mount K2', 'Mount Everest', 3),
('Hertz', 'Joule', 'Watt', 'Ohm', 'Hertz', 4),
('Leonardo da Vinci', 'Michelangelo', 'Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 5);

INSERT INTO student_exam (examID, stdID, grade)
VALUES (1, 1, 85),
(2, 2, 92),
(3, 3, 73),
(4, 4, 95),
(5, 5, 60),
(6, 6, 85),
(7, 7, 92),
(8, 8, 73),
(9, 9, 95),
(10, 10, 60);

INSERT INTO std_answers (stdID, quesID, answer)
VALUES (1, 1, 'Paris'),
(2, 2, 'Carbon dioxide is converted into glucose'),
(3, 3, 'for (int i = 0; i < 10; i++)'),
(4, 4, 'A = bh/2'),
(5, 5, '100 degrees Celsius'),
(6, 6, 'Canberra'),
(7, 7, 'George Washington'),
(8, 8, 'Mount Everest'),
(9, 9, 'Hertz'),
(10, 10, 'Leonardo da Vinci');