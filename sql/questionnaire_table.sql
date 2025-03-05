-- This code is purely for assessment purposes and is not intended for actual implementation in any real-life system.

SELECT * FROM questionnaire;

-- Create the questionnaire table
CREATE TABLE questionnaire(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    title VARCHAR(8000) NOT NULL
);

-- Insert MVP questionnaire
INSERT INTO questionnaire (title) VALUES ('Digital Maturity Questionnaire MVP');