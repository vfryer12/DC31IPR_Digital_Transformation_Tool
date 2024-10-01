SELECT * FROM userAnswers;

CREATE TABLE userAnswers(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    answersId INT NOT NULL,
    userId INT NOT NULL,
    questionsId INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES user(id),
    FOREIGN KEY (answersId) REFERENCES answers(id),
    FOREIGN KEY (questionsId) REFERENCES questions(id)
);