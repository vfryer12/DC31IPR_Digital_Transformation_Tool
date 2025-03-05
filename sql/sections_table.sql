-- This code is purely for assessment purposes and is not intended for actual implementation in any real-life system.

SELECT * FROM sections;

-- Create the sections table
CREATE TABLE sections (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    questionnaireId INT NOT NULL,
    section VARCHAR(8000) NOT NULL,
    FOREIGN KEY (questionnaireId) REFERENCES questionnaire(id)
);

ALTER TABLE sections
ADD COLUMN section VARCHAR(8000) NOT NULL;

-- Insert data into sections table
INSERT INTO sections (questionnaireId, section) 
VALUES (1, 'Digital Strategy');
INSERT INTO sections (questionnaireId, section) 
VALUES (1, 'Digital Skills');
INSERT INTO sections (questionnaireId, section) 
VALUES (1, 'Technology Adoption');
INSERT INTO sections (questionnaireId, section) 
VALUES (1, 'Market Trends');
INSERT INTO sections (questionnaireId, section) 
VALUES (1, 'Digital Marketing');