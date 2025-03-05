-- This code is purely for assessment purposes and is not intended for actual implementation in any real-life system.

SELECT * FROM questions;

-- Create the questions table
CREATE TABLE questions(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    sectionId INT NOT NULL,
    question VARCHAR(8000) NOT NULL,
    FOREIGN KEY (sectionId) REFERENCES sections(id)
);

-- Insert the question into the questions table from the Digital Strategy section
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'How is your digital strategy aligned with your overall business strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'Who is responsible for driving the digital strategy in yoiur organisation?');

-- Update the question to correct the typo
UPDATE questions
SET question = 'Who is responsible for driving the digital strategy in your organisation?'
WHERE question = 'Who is responsible for driving the digital strategy in yoiur organisation?';

INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'How often is your digital strategy reviewed and updated?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'How do you measure the success of your digital strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'What key performance indicators (KPIs) are used to track your digital strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'How do you ensure that all employees understand and align with the digital strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'What challenges have you faced in implementing your digital strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'How do you incorporate feedback and lessons learned into your digital strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'How do you integrate emerging technologies into your digital strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Strategy'), 'How does your digital strategy address the customer journey?');

-- Insert the question into the questions table from the Digital Skills section
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'What specific digital skills are most important in your organisation?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'How do you assess the digital skills of new hires?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'What is your strategy for upskilling employees in digital areas?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'How do you foster a culture of continuous learning in digital skills?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'What digital skills gaps exist in your organisation');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'How do you plan to address these digital skills gaps?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'How do you keep up with the rapidly evolving digital skills landscape?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'How do you ensure that your organisation has the digital skills needed to stay competitive?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'How do you ensure that your workforce is adaptable to new digital tools and platforms?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Skills'), 'What initiatives do you have in place to attract digital talent?');

-- Insert the question into the questions table from the Technology Adoption section
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'What is your process for evaluating new digital technologies?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'How do you ensure a smooth adoption of new digital technologies?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'What challengers have you faced in adopting new digital technologies?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'How do you measure the success of new technology adoption?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'How do you ensure that new technologies align with your business objectives?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'How do you manage the change associated with new technology adoption?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'How do you keep up with the latest digital technology trends?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'How do you ensure that your technology stack remains up-to-date and relevant?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'How do you assess the risks associated with the adoption of new technologies?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Technology Adoption'), 'What strategies do you use to overcome resistance to new technology adoption?');

-- Insert the question into the questions table from the Market Trends section
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company stay updated with the latest digital trends in the market?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How have market trends influenced your companys digital maturity?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company plan to leverage emerging digital trends?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company adapt its digital strategy based on market trends?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company predict future digital trends in the market?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company ensure that it is not left behind in the digital race?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company use market trends to inform its digital marketing strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company use market trends to inform its product development strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company use market trends to inform its customer service strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Market Trends'), 'How does your company use market trends to inform its sales strategy?');

-- Insert the question into the questions table from the Digital Marketing section
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company leverage digital marketing to reach its target audience?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company measure the success of its digital marketing efforts?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company plan to improve its digital marketing strategies?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company use data analytics in its digital marketing efforts?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company handle SEO for its digital content?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company use social media in its digital marketing strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company use email marketing in its digital marketing strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company use content marketing in its digital marketing strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company use influencer marketing in its digital marketing strategy?');
INSERT INTO questions (sectionId, question)
VALUES ((SELECT id FROM sections WHERE section = 'Digital Marketing'), 'How does your company use video marketing in its digital marketing strategy?');