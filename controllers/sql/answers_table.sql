SELECT * FROM answers;

CREATE TABLE answers(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    questionsId INT NOT NULL,
    answer VARCHAR(8000) NOT NULL,
    weighting INT,
    solution VARCHAR(8000) NOT NULL,
    FOREIGN KEY (questionsId) REFERENCES questions(id)
);

-- Insert the answer into the answers table
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Fully Aligned',
    1, 
    'When the digital strategy is fully aligned with the business strategy, digital initiatives directly support the achievement of business objectives. This includes understanding the business’s strategic goals and ensuring that all digital efforts contribute towards these goals'
);
-- Supposed to be - How is your digital strategy aligned with your overall business strategy?

-- Update the questionsId to reference the correct question
UPDATE answers
SET questionsId = (SELECT id FROM questions WHERE question = 'How is your digital strategy aligned with your overall business strategy?')
WHERE questionsId = (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?');

-- Insert the answer into the answers table
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Needs Improvement',
    2, 
    'If the alignment needs improvement, it means that while there is some connection between the digital and business strategies, there are areas where the digital initiatives are not effectively supporting the business objectives. This could be due to a lack of communication, unclear digital goals, or a rapidly changing digital landscape.'
);

-- Amend again - Update the questionsId to reference the correct question
UPDATE answers
SET questionsId = (SELECT id FROM questions WHERE question = 'How is your digital strategy aligned with your overall business strategy?')
WHERE questionsId = (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?');

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How is your digital strategy aligned with your overall business strategy?'), 
    'No Plan in Place',
    3, 
    'Without a plan in place, digital initiatives may be disjointed and not contribute effectively to business objectives. It’s crucial to develop a digital strategy that aligns with the business strategy to ensure that digital initiatives are driving the organization towards its goals.'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'Who is responsible for driving the digital strategy in your organisation?'), 
    'Chief Information Officer (CIO)',
    1, 
    'Responsible for aligningg technology with the organisations strategic goals'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'Who is responsible for driving the digital strategy in your organisation?'), 
    'Chief Technology Officer (CTO)',
    2, 
    'Focuses on external customer-facing technologies and how they align with business operation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'Who is responsible for driving the digital strategy in your organisation?'), 
    'Digital Transformation Manager',
    3, 
    'Directly manages the implmentation of digital transformation projects'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'Who is responsible for driving the digital strategy in your organisation?'), 
    'Chief Digital Officer (CDO)',
    4, 
    'Often leads the digital transformation initiatives across the entire organisation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'Who is responsible for driving the digital strategy in your organisation?'), 
    'IT Director/Manager',
    5, 
    'Oversees the IT infrastructure that supports the digital tranformation projects'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'Who is responsible for driving the digital strategy in your organisation?'), 
    'Business Unit Leader',
    6, 
    'Integrates digital strategy within their specific department or unit'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'Who is responsible for driving the digital strategy in your organisation?'), 
    'Marketing Director',
    7, 
    'Drives the digital marketing aspect of the strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'Who is responsible for driving the digital strategy in your organisation?'), 
    'Data Analytics Leader',
    8, 
    'Provides data-driven marketing aspect of the strategy'
);

-- Question three secton 1
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How often is your digital strategy reviewed and updated?'), 
    'Continuous',
    1, 
    ' Continuous monitoring is the most effective as it allows for real-time adjustments and can quickly identify issues or opportunities'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How often is your digital strategy reviewed and updated?'), 
    'Monthly',
    2, 
    'Monthly reviews can be effective for tracking progress and making minor adjustments to the strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How often is your digital strategy reviewed and updated?'), 
    'Quarterly',
    3, 
    'Quarterly reviews provide a balance between being responsive to changes and not having to constantly adjust your strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How often is your digital strategy reviewed and updated?'), 
    'Annual',
    4, 
    'An annual review is important for reassessing overall goals and making major updates to the strategy.'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How often is your digital strategy reviewed and updated?'), 
    'Never',
    5, 
    'Not reviewing the digital strategy is the least effective approach. The digital landscape is constantly evolving, and strategies need to be updated regularly to stay competitive'
);

-- Question four secton 1

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of your digital strategy?'), 
    'Return on Investment (ROI)',
    1, 
    'This is often considered the most important metric as it directly relates to the profitability of your digital initiatives'
);
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of your digital strategy?'), 
    'Conversion Rates',
    2, 
    'This measures the effectiveness of your digital strategy in driving desired actions, making it a key indicator of success'
);
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of your digital strategy?'), 
    'Customer Acquisition Cost (CAC) and Customer Lifetime Value (CLV)',
    3, 
    'These metrics provide insights into the cost-effectiveness of your customer acquisition strategies and the value that customers bring over their lifetime'
);
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of your digital strategy?'), 
    'Website Traffic',
    4, 
    'High traffic can increase brand visibility and create more opportunities for conversions, making this a crucial metric'
);
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of your digital strategy?'), 
    'Customer Engagement',
    5, 
    'This measures how well you’re able to engage customers with your content and platform, which can impact customer satisfaction and loyalty'
);
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of your digital strategy?'), 
    'Social Media Metrics and Email Marketing Metrics',
    6, 
    'These metrics can provide insights into the effectiveness of your social media and email marketing strategies'
);
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of your digital strategy?'), 
    'SEO Rankings',
    7, 
    'While this is an important metric, its impact can be indirect and long-term, making it lower in the ranking'
);
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of your digital strategy?'), 
    'None of the above',
    8, 
    ''
);

-- Question five secton 1
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Adoption & Performance Metrics',
    1, 
    'Indicates how well new digital tools are being utilized and their impact'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Percentage of AI-Enabled Businesses',
    2, 
    'Reflects the integration of AI which is a key driver of innovation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Percentage of Cloud Deployments',
    3, 
    'Shows the adoption of cloud services which is essential for digital agility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Employee Productivity',
    4, 
    'Enhanced by digital tools directly affecting operational efficiency'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Return on Digiital Investments',
    5, 
    'Measures the financial impacat of digital intiatives'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Customer Experience Metrics',
    6, 
    'A mature digital business provider superior customer experiences'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Reliability & Availability',
    7, 
    'Core aspects of digital serviices that affect user trust and satisfaction'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Revenue from Digital Technology',
    8, 
    'Tracks the direct financial gains form digital channel'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Customer Satisfaction Score (CSAT)',
    9, 
    'High satisfaction is often a result off digital improvements'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Customer Lifetime Value',
    10, 
    'Higher CLV can be achieved with better digital engagement strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Conversion Rate',
    11, 
    'Improved through effective digital marketing and sales funnels'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Website Traffic',
    12, 
    'More traffic can indicate successful digital marketing efforts'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Social Media Engagement',
    13, 
    'Engagement can improve with mature digital marketing strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Brand Engagement On Website',
    14, 
    'Indicates how digital content resonates with users'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Customer Effort Service (CES)',
    15, 
    'Lower effort scores can result in streamlined digital processes'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Active Usage Metrics',
    16, 
    'Shows engagement, which can be enchanced with digital maturity'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Traffic Sources',
    17, 
    'Understanding sources help refine digital marketing strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Landing Page Conversions',
    18, 
    'Effective digital strategies can improve these rates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Inbound Marketing ROI',
    19, 
    'A mature digital strategy can yield higher returns on inbound marketing'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'Social Media Traffic',
    20, 
    'Reflects the effectiveness of social mediiia within the digital strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What key performance indicators (KPIs) are used to track your digital strategy?'), 
    'None of the above',
    21, 
    ''
);

-- Question six secton 1

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that all employees understand and align with the digital strategy?'), 
    'Clear Communication',
    1, 
    'Articulate the digital strategy and its relevance to the company’s vision'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that all employees understand and align with the digital strategy?'), 
    'Engagement',
    2, 
    'Involve employees in strategy development to foster ownership'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that all employees understand and align with the digital strategy?'), 
    'Training',
    3, 
    'Offer comprehensive training for the necessary digital skills'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that all employees understand and align with the digital strategy?'), 
    'Feedback',
    4, 
    'Implement a feedback loop for continuous strategy refinement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that all employees understand and align with the digital strategy?'), 
    'Leadership',
    5, 
    'Ensure leaders exemplify and advocate for the digital strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that all employees understand and align with the digital strategy?'), 
    'Incentives',
    6, 
    'Align rewards and recognition with digital strategy goals'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that all employees understand and align with the digital strategy?'), 
    'Monitoring',
    7, 
    'Regularly track progress and adjust the strategy as needed'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that all employees understand and align with the digital strategy?'), 
    'None of the above',
    24, 
    ''
);

-- Question seven secton 1

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challenges have you faced in implementing your digital strategy?'), 
    'None of the above',
    1, 
    ''
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challenges have you faced in implementing your digital strategy?'), 
    'Alignment',
    2, 
    'It’s crucial that all parts of the organization are working towards the same goals'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challenges have you faced in implementing your digital strategy?'), 
    'Resistance to Change',
    3, 
    'Overcoming this can determine the success or failure of the strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challenges have you faced in implementing your digital strategy?'), 
    'Skill Gaps',
    4, 
    'Without the necessary skills, employees cannot effectively contribute to the strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challenges have you faced in implementing your digital strategy?'), 
    'Resource Allocation',
    5, 
    'Adequate resources are necessary to support the changes'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challenges have you faced in implementing your digital strategy?'), 
    'Data Management',
    6, 
    'The ability to handle data securely and efficiently is vital'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challenges have you faced in implementing your digital strategy?'), 
    'Keeping Pace',
    7, 
    'Staying current with technology is important for maintaining a competitive edge'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challenges have you faced in implementing your digital strategy?'), 
    'Measuring Success',
    8, 
    'Knowing if the strategy is working helps to guide future decisions'
);

-- Question eight secton 1

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?'), 
    'Feedback Mechanisms',
    1, 
    'The foundation for gathering valuable insights'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?'), 
    'Data Analysis',
    2, 
    'Critical for understanding the impact and guiding decisions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?'), 
    'Regular Reviews',
    3, 
    'Essential for keeping the strategy relevant and effective'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?'), 
    'Adaptability',
    4, 
    'Allows the strategy to evolve based on new information'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?'), 
    'Communication',
    5, 
    'Ensures that everyone is aware of changes and the reasons behind them'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?'), 
    'Documentation',
    6, 
    'Provides a clear history of changes and supports future decision-making'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?'), 
    'None of the above',
    21, 
    ''
);

UPDATE answers
SET weighting = 8
WHERE questionsId = (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?')
AND answer = 'None of the above'
AND weighting = 21;

UPDATE answers
SET weighting = 7
WHERE questionsId = (SELECT id FROM questions WHERE question = 'How do you incorporate feedback and lessons learned into your digital strategy?')
AND answer = 'None of the above'
AND weighting = 8;

-- Question nine secton 1
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you integrate emerging technologies into your digital strategy?'), 
    'Strategic Fit',
    1, 
    'Ensures that the technology supports the business objectives'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you integrate emerging technologies into your digital strategy?'), 
    'Research',
    2, 
    'Fundamental for understanding the potential and limitations of new technologies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you integrate emerging technologies into your digital strategy?'), 
    'Risk Assessment',
    3, 
    'Critical for making informed decisions about technology adoption'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you integrate emerging technologies into your digital strategy?'), 
    'Pilot Projects',
    4, 
    'Allows for testing and learning before committing resources'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you integrate emerging technologies into your digital strategy?'), 
    'Training',
    5, 
    'Equips employees with the necessary skills to utilize new technologies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you integrate emerging technologies into your digital strategy?'), 
    'Scalability',
    6, 
    'Important for planning the future growth and impact of the technology'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you integrate emerging technologies into your digital strategy?'), 
    'None of the above',
    21, 
    ''
);

-- Question ten secton 1
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your digital strategy address the customer journey?'), 
    'Understanding Needs',
    1, 
    'The basis for a customer-centric strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your digital strategy address the customer journey?'), 
    'Personalization',
    2, 
    'Key to making customers feel valued and understood'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your digital strategy address the customer journey?'), 
    'Seamless Experience',
    3, 
    'Seamless user experience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your digital strategy address the customer journey?'), 
    'Customer Feedback',
    4, 
    'Vital for continuous improvement of the customer journey'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your digital strategy address the customer journey?'), 
    'Engagement',
    5, 
    'Important for building long-term customer relationships'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your digital strategy address the customer journey?'), 
    'Measurement',
    6, 
    'Necessary to evaluate and refine the customer journey'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your digital strategy address the customer journey?'), 
    'None of the above',
    7, 
    ''
);

-- Question one secton 2
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Data Analysis',
    1, 
    'The ability to interpret and leverage data is crucial for driving business decisions and strategy in a mature digital company'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Cybersecurity',
    2, 
    'As companies grow and become more reliant on digital tools and platforms, the need for robust cybersecurity measures increases'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Cloud Computing',
    3, 
    'Mature digital companies often need the scalability that cloud computing provides. It also allows for cost savings and increased collaboration'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Artificial Intelligence and Machine Learning',
    4,
    'Mature digital companies often have large amounts of data at their disposal. Utilizing AI and machine learning can help these companies make the most of this data'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Software Development',
    5,
    'Whether it’s for maintaining a company website or developing internal tools, software development skills are key'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Project Management',
    6,
    'Efficient project management is crucial to keep all parts of the company running smoothly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Digital Marketing',
    7,
    'Even for mature companies reaching new customers and maintaining brand awareness is important'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'UX/UI Design',
    8,
    'Ensuring a positive user experience can be a key differentiator for mature digital companies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Remote collaboration Tools',
    9,
    'As companies grow  they may have employees or partners in various locations, making these tools essential'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What specific digital skills are most important in your organisation?'), 
    'Blockchain Technology',
    10,
    'Some mature digital companies may find blockchain technology increasingly relevant, particularly if they’re in the financial sector'
);

-- Question two secton 2
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the digital skills of new hires?'), 
    'Skill-Specific Tests',
    1,
    'These tests are designed to assess the specific digital skills required for the job, making them a top priority'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the digital skills of new hires?'), 
    'Certifications and Qualifications',
    2,
    'A candidate’s educational background and relevant certifications can be a good indicator of their digital skills'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the digital skills of new hires?'), 
    'Practical Exercises',
    3,
    'These give the candidate a task similar to what they would be doing on the job, providing a practical assessment of their skills'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the digital skills of new hires?'), 
    'Behavioral Interview Questions',
    4,
    'These questions require the candidate to explain how they’ve used their digital skills in the past, offering insight into their practical experience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the digital skills of new hires?'), 
    'Online Assessments',
    5,
    'Online platforms offer assessments for different digital skills, providing a standardized measure of a candidate’s abilities'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the digital skills of new hires?'), 
    'Peer Review',
    6,
    'Involving team members who have strong digital skills in the interview process can provide valuable insights and help assess the candidate’s skill level'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the digital skills of new hires?'), 
    'Hiring via Recruiter',
    7,
    'Recruiters often have a keen eye for spotting the necessary digital skills in potential candidates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the digital skills of new hires?'), 
    'None of the above',
    8,
    'Worrying indicator of poor hiring practices'
);

-- Question three secton 2
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Training Programs',
    1,
    'These are often the most direct and effective way to upskill employees, as they can be tailored to the specific needs of the organization and its employees'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Online Learning Platforms',
    2,
    'These platforms offer a wide range of courses and can be accessed at any time, making them a very flexible upskilling option'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Workshops and Seminars',
    3,
    'These can provide intensive, focused learning experiences and the opportunity to ask questions and interact with experts'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Learning and Development Budget',
    4,
    'This demonstrates the organization’s commitment to upskilling and allows employees to take ownership of their own learning'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Mentorship Programs',
    5,
    'These can provide personalized guidance and support, which can be particularly effective for complex digital skills'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Project-Based Learning',
    6,
    'This provides hands-on experience, which can often lead to deeper understanding and better retention of new skills'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Encourage Self-Learning',
    7,
    'This fosters a culture of continuous learning, which is crucial in the fast-paced digital world'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Regular Assessments and Feedback',
    8,
    'These ensure that upskilling efforts are effective and allow for adjustments as needed'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Recognize and Reward Learning',
    9,
    'Recognition and rewards can motivate employees to engage in upskilling'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'Stay Updated',
    10,
    'Keeping up-to-date with the latest digital trends and technologies ensures that upskilling efforts remain relevant'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your strategy for upskilling employees in digital areas?'), 
    'None of the above',
    11,
    'No upskilling is attemped'
);

-- Question four secton 2

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Leadership Support',
    1,
    'Leaders acting as role models and actively supporting their team’s learning efforts can have the greatest impact on fostering a learning culture'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Promote a Growth Mindset',
    2,
    'Encouraging employees to view challenges as opportunities for growth is fundamental to a learning culture'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Provide Learning Resources',
    3,
    'Providing a variety of learning resources is a direct and effective way to support employee learning'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Learning and Development Programs',
    4,
    'Structured programs can ensure that all employees have equal learning opportunities and can help to systematically upskill the entire organization'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Encourage Self-Learning',
    5,
    'Allowing employees time for self-learning can foster a sense of ownership and personal development'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Regular Skill Assessments',
    6,
    'Regular assessments can help track progress, identify gaps, and keep employees motivated'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Feedback Culture',
    7,
    'A culture of constructive feedback can help employees identify areas for improvement and take steps to develop those areas'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Recognize and Reward Learning',
    8,
    'Recognition and rewards can motivate employees to engage in upskilling'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Create Learning Communities',
    9,
    'Learning communities can provide a supportive environment for shared learning and knowledge exchange'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'Stay Updated',
    10,
    'Keeping up-to-date with the latest digital trends and technologies ensures that learning efforts remain relevant and forward-looking'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you foster a culture of continuous learning in digital skills?'), 
    'None of the above',
    11,
    'No culture of continuous learning in digital skills'
);

-- Question four secton 2

DELETE FROM answers
WHERE questionsId = 51
  AND answer = 'Data Analysis'
  AND weighting = 1
  AND solution = 'The ability to analyze and interpret data effectively is crucial for driving business decisions and strategy';

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Data Analysis',
    1,
    'The ability to analyze and interpret data effectively is crucial for driving business decisions and strategy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Cybersecurity',
    2,
    'Protecting against sophisticated cyber threats is increasingly important as organizations become more reliant on digital tools and platforms'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Cloud Computing',
    3,
    'As many organizations move to the cloud understanding how to leverage cloud technologies effectively is key'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Artificial Intelligence and Machine Learning',
    4,
    'These complex fields are becoming increasingly relevant, and a lack of expertise in them can hinder an organization’s ability to stay competitive'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Software Development',
    5,
    'Knowledge of the latest programming languages and development methodologies is important for maintaining and improving digital products and services'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Digital Marketing',
    6,
    'Keeping up with the latest digital marketing strategies and tools is crucial for reaching customers and driving sales'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'UX/UI Design',
    7,
    'Creating user-friendly digital experiences can significantly impact customer satisfaction and retention'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Project Management',
    8,
    'Effective management of digital projects can greatly influence the success of those projects'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Remote Collaboration',
    9,
    'With the rise of remote work effective use of remote collaboration tools is becoming increasingly important'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What digital skills gaps exist in your organisation?' LIMIT 1), 
    'Blockchain Technology',
    10,
    'While not relevant to all organizations, those in certain sectors (like finance) may find a lack of understanding about blockchain technology to be a significant gap'
);

-- Question six secton 2

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you plan to address these digital skills gaps?'), 
    'Training and Development Programs',
    1,
    'Implementing comprehensive training programs for existing employees can help to improve their digital skills. This could include workshops, online courses, or even bringing in experts for in-house training sessions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you plan to address these digital skills gaps?'), 
    'Hiring New Talent',
    2,
    'If certain skills are severely lacking within the organization, it might be beneficial to hire new employees who possess these skills. This can bring in fresh perspectives and help to fill immediate gaps'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you plan to address these digital skills gaps?'), 
    'Encouraging Continuous Learning',
    3,
    'Promoting a culture of continuous learning can encourage employees to regularly update their skills and stay abreast of the latest digital trends'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you plan to address these digital skills gaps?'), 
    'Leveraging Technology',
    4,
    'Utilize digital tools and platforms that can facilitate upskilling and reskilling. There are numerous online platforms that offer courses on everything from data analysis to UX/UI design'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you plan to address these digital skills gaps?'), 
    'Partnerships with Educational Institutions',
    5,
    'Collaborating with universities or vocational schools can help to ensure a steady influx of new hires who possess the latest digital skills. It can also provide opportunities for existing employees to further their education'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you plan to address these digital skills gaps?'), 
    'Outsourcing',
    6,
    'For highly specialized skills, such as AI and Machine Learning or Blockchain Technology, it might be more cost-effective and efficient to outsource these tasks to specialized firms or consultants'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you plan to address these digital skills gaps?'), 
    'None of the above',
    7,
    ''
);

-- Question seven secton 2
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the rapidly evolving digital skills landscape?'), 
    'Continuous Learning',
    1,
    'The digital world is constantly evolving, so it’s important to be a lifelong learner. This could involve taking online courses, attending workshops or webinars, or reading up on the latest trends and technologies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the rapidly evolving digital skills landscape?'), 
    'Networking',
    2,
    'Engaging with others in your field can provide valuable insights and keep you informed about new developments. This could be through professional networking sites, industry events, or online communities'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the rapidly evolving digital skills landscape?'), 
    'Following Industry News',
    3,
    'Regularly reading industry news and reports can help you stay on top of the latest trends and advancements in digital technology'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the rapidly evolving digital skills landscape?'), 
    'Hands-On Practice',
    4,
    'Applying new skills in real-world contexts is one of the best ways to understand and master them. This could involve working on projects that utilize new technologies or techniques'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the rapidly evolving digital skills landscape?'), 
    'Mentorship',
    5,
    'Learning from someone more experienced in your field can provide valuable guidance and insights. A mentor can also help you navigate the ever-changing digital landscape'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the rapidly evolving digital skills landscape?'), 
    'Certifications',
    6,
    'Earning certifications in new digital skills can not only help you learn them but also validate your knowledge to others'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the rapidly evolving digital skills landscape?'), 
    'None of the above',
    7,
    ''
);

-- Question eight secton 2

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your organisation has the digital skills needed to stay competitive?'), 
    'Skills Assessment',
    1,
    'Regularly assess the digital skills of your employees to identify any gaps. This can be done through surveys, interviews, or performance reviews'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your organisation has the digital skills needed to stay competitive?'), 
    'Training and Development',
    2,
    'Implement comprehensive training programs to upskill existing employees. This could include workshops, online courses, or even bringing in experts for in-house training sessions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your organisation has the digital skills needed to stay competitive?'), 
    'Hiring Strategy',
    3,
    'When hiring new employees, prioritize candidates with the digital skills that your organization needs. This might involve updating job descriptions or working with recruiters who specialize in the digital field'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your organisation has the digital skills needed to stay competitive?'), 
    'Encourage Continuous Learning',
    4,
    'Foster a culture of continuous learning within your organization. Encourage employees to stay updated on the latest digital trends and technologies, and provide them with the resources to do so'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your organisation has the digital skills needed to stay competitive?'), 
    'Leverage Technology',
    5,
    'Utilize digital tools and platforms that can facilitate upskilling and reskilling. There are numerous online platforms that offer courses on everything from data analysis to UX/UI design'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your organisation has the digital skills needed to stay competitive?'), 
    'Partnerships',
    6,
    'Collaborate with educational institutions or industry organizations to ensure a steady influx of new hires with the latest digital skills. This can also provide opportunities for existing employees to further their education'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your organisation has the digital skills needed to stay competitive?'), 
    'Outsourcing',
    7,
    'For highly specialized skills, consider outsourcing to specialized firms or consultants. This can be a cost-effective way to access expertise that isn’t available in-house'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your organisation has the digital skills needed to stay competitive?'), 
    'None of the above',
    8,
    ''
);

-- Question nine secton 2

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your workforce is adaptable to new digital tools and platforms?'), 
    'Training and Development',
    1,
    'Provide comprehensive training on new tools and platforms. This could include hands-on workshops, online tutorials, or even bringing in experts for in-house training sessions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your workforce is adaptable to new digital tools and platforms?'), 
    'Support and Resources',
    2,
    'Provide ongoing support and resources for employees to learn and adapt to new tools. This could include a dedicated IT support team, self-help resources, or user manuals'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your workforce is adaptable to new digital tools and platforms?'), 
    'Culture of Adaptability',
    3,
    'Foster a culture that values adaptability and continuous learning. Encourage employees to be open to new technologies and to continuously update their skills'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your workforce is adaptable to new digital tools and platforms?'), 
    'Pilot Testing',
    4,
    'Before rolling out a new tool or platform across the organization, conduct a pilot test with a small group of employees. This can help to identify any potential issues or training needs'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your workforce is adaptable to new digital tools and platforms?'), 
    'Feedback Mechanisms',
    5,
    'Implement mechanisms for employees to provide feedback on new tools and platforms. This can help to identify any issues or areas for improvement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your workforce is adaptable to new digital tools and platforms?'), 
    'Leadership Involvement',
    6,
    'Leaders should be involved in the process and act as role models in adapting to new digital tools. This can help to drive engagement and adoption among employees'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your workforce is adaptable to new digital tools and platforms?'), 
    'None of the above',
    7,
    ''
);

-- Question ten secton 2

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What initiatives do you have in place to attract digital talent?'), 
    'Competitive Compensation',
    1,
    'Offering competitive salaries and benefits is often the most direct way to attract talented professionals'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What initiatives do you have in place to attract digital talent?'), 
    'Career Development Opportunities',
    2,
    'Providing clear paths for career advancement can make your organization more attractive to ambitious digital professionals'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What initiatives do you have in place to attract digital talent?'), 
    'Continuous Learning and Development',
    3,
    'Offering opportunities for continuous learning and development can attract individuals who are eager to improve their skills and stay updated with the latest digital trends'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What initiatives do you have in place to attract digital talent?'), 
    'Workplace Culture',
    4,
    'A positive, inclusive, and innovative workplace culture can make your organization a more attractive place to work'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What initiatives do you have in place to attract digital talent?'), 
    'Flexible Work Arrangements',
    5,
    'With the rise of remote work, offering flexible work arrangements can be a major draw for digital talent'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What initiatives do you have in place to attract digital talent?'), 
    'Interesting Projects',
    6,
    'The opportunity to work on innovative and challenging projects can attract digital professionals who are looking for a place to apply and grow their skills'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What initiatives do you have in place to attract digital talent?'), 
    'Employer Branding',
    7,
    'A strong employer brand that showcases your organization’s values, mission, and culture can help to attract digital talent'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What initiatives do you have in place to attract digital talent?'), 
    'None of the above',
    8,
    ''
);

-- Question one secton 3
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'All of the above',
    1,
    ''
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Define Clear Objectives',
    2,
    'Establishing clear goals is crucial as it guides the entire evaluation process'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Assess Alignment with Your Business',
    3,
    'Ensuring the technology fits your business strategy and processes is essential for seamless integration'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Feasibility and Viability Check',
    4,
    'Analyzing technical and financial feasibility ensures the technology can be realistically implemented'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Risk Analysis',
    5,
    'Identifying and mitigating potential risks is vital to avoid future issues'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Performance Against KPIs',
    6,
    'Measuring performance against key indicators ensures the technology meets your business needs'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Test and Iterate',
    7,
    'Conducting pilot tests helps in understanding real-world performance and making necessary adjustments'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Explore Market Potential',
    8,
    'Understanding market demand and competition helps in assessing the technology’s potential success'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Collaborate and Seek Expert Input',
    9,
    'Gathering insights from experts and stakeholders can provide valuable perspectives'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'User-Friendliness',
    10,
    'Ensuring the technology is easy to use is important for adoption and efficiency'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'Long-Term Vision Assessment',
    11,
    'Considering the long-term impact and sustainability helps in future-proofing your investment'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What is your process for evaluating new digital technologies?'), 
    'None of the above',
    12,
    ''
);

-- Question two secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Clear Communication',
    1,
    'Essential for explaining benefits, addressing concerns, and ensuring everyone is on the same page'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Leadership Support',
    2,
    'Crucial for championing the adoption and addressing challenges'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Comprehensive Training Programs',
    3,
    'Vital for ensuring users understand how to use the new technology effectively'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Change Management Strategies',
    4,
    'Important for handling resistance and ensuring a smooth transition'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'User-Friendly Design',
    5,
    'Helps minimize the learning curve and enhance user experience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Support Systems',
    6,
    'Necessary for assisting users during the transition'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Pilot Testing',
    7,
    'Useful for identifying potential issues and gathering feedback before full-scale rollout'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Gradual Implementation',
    8,
    'Allows users to adapt gradually and reduces the risk of disruption'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Feedback Mechanisms',
    9,
    'Important for continuous improvement based on user feedback'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure a smooth adoption of new digital technologies?'), 
    'Monitor and Evaluate',
    10,
    'Ensures the adoption process is effective and allows for adjustments as needed'
);

-- Question three secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Resistance to Change',
    1,
    'Overcoming reluctance from employees or stakeholders is crucial for successful adoption.'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Lack of Skilled Personnel',
    2,
    'Having the necessary skills within your team is essential for effective implementation and use'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Complexity of Technology',
    3,
    'Ensuring the new technology integrates smoothly with existing systems is vital'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Security Concerns',
    4,
    'Addressing potential security vulnerabilities is critical to protect your organization'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Budget Constraints',
    5,
    'Managing the costs associated with new technologies is important to stay within budget'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Inadequate Training',
    6,
    'Providing sufficient training is necessary to ensure proper use and productivity'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Cultural Mindset',
    7,
    'Cultivating a culture that embraces change can significantly impact adoption success'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Siloed Organizational Structure',
    8,
    'Promoting collaboration between departments is important for organization-wide implementation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Continuous Evolution of Customer Needs',
    9,
    'Keeping up with changing customer expectations is essential for staying competitive'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What challengers have you faced in adopting new digital technologies?'), 
    'Measuring ROI',
    10,
    'Accurately measuring the return on investment helps justify the expense and assess the technology’s value'
);

-- Question four secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'User Adoption Rate',
    1,
    'A high adoption rate is crucial as it indicates widespread acceptance and use of the technology'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'Performance Metrics',
    2,
    'Vital for ensuring users understand how to use the new technology effectively'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'Return on Investment (ROI)',
    3,
    'Calculating the financial return helps justify the investment and assess the overall value'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'User Satisfaction',
    4,
    'Gathering feedback and assessing satisfaction levels provide insights into user experience and acceptance'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'Usage Frequency',
    5,
    'Frequent use of the technology indicates its integration into daily workflows'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'Business Impact',
    6,
    'Analyzing the overall impact on business processes, including efficiency and revenue growth, is important for long-term success'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'Time to Proficiency',
    7,
    'Assessing how quickly users become proficient helps understand the learning curve and training effectiveness'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'Support Requests',
    8,
    'Tracking support requests helps identify common issues and areas needing improvement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'Feature Adoption Rate',
    9,
    'Measuring the use of different features can indicate which aspects of the technology are most valuable'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you measure the success of new technology adoption?'), 
    'Training Completion Rates',
    10,
    'Monitoring training completion ensures users are adequately prepared to use the technology'
);

-- Question five secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Define Clear Business Goals',
    1,
    'Establishing clear objectives is crucial as it guides the entire alignment process'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Collaborate with Stakeholders',
    2,
    'Engaging with key stakeholders ensures the technology meets the needs of different departments and aligns with overall strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Conduct a Needs Assessment',
    3,
    'Identifying gaps and opportunities helps in selecting technologies that add the most value'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Develop a Unified Strategy',
    4,
    'Integrating technology initiatives with business objectives ensures they work together seamlessly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Monitor and Measure Performance',
    5,
    'Regularly assessing performance against KPIs ensures the technology meets business goals'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Data-Driven Decision Making',
    6,
    'Using data and analytics to guide decisions ensures they are based on measurable outcomes'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Implement Governance and Accountability',
    7,
    'Setting up governance structures ensures accountability for meeting business objectives'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Continuous Feedback Loops',
    8,
    'Establishing feedback mechanisms allows for regular assessment and necessary adjustments'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Encourage Cross-Functional Collaboration',
    9,
    'Promoting collaboration across departments ensures the technology is integrated into all relevant areas'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that new technologies align with your business objectives?'), 
    'Adapt and Evolve',
    10,
    'Being prepared to adapt your strategy as business objectives and market conditions change ensures long-term alignment'
);

-- Question six secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Set and Communicate Clear Goals',
    1,
    'Clearly defining and communicating objectives helps everyone understand the purpose and benefits of the change'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Develop a Comprehensive Strategy',
    2,
    'A detailed plan with timelines, resources, and responsibilities ensures a structured approach to implementation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Provide Continuous Training and Support',
    3,
    'Ongoing training and support are crucial for helping employees adapt to the new technology'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Build a Dedicated Change Management Team',
    4,
    'A team with the right mix of skills can effectively lead and manage the change process'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Plan for Resistance',
    5,
    'Anticipating and addressing resistance helps in smooth transition and increases acceptance'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Encourage Employee Involvement',
    6,
    'Involving employees in the process increases buy-in and helps identify potential issues early'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Monitor and Evaluate Progress',
    7,
    'Regular assessment and adjustments ensure the adoption process stays on track'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Communicate Regularly',
    8,
    'Keeping everyone informed about progress, challenges, and successes maintains transparency and trust'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Foster a Culture of Innovation',
    9,
    'Promoting a culture that embraces change encourages experimentation and acceptance'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'Celebrate Successes',
    10,
    'Recognizing and celebrating milestones motivates employees and reinforces the benefits of the new technology'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you manage the change associated with new technology adoption?'), 
    'None of the above',
    11,
    ''
);

-- Question seven secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Join Professional Organizations',
    1,
    'Becoming a member of industry-specific organizations can provide access to the latest research, publications, and networking opportunities'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Attend Industry Conferences and Tech Events',
    2,
    'Participating in conferences and events helps you stay informed about the latest developments and innovations'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Follow Tech News and Blogs',
    3,
    'Regularly reading technology news websites, blogs, and subscribing to newsletters keeps you updated on current trends'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Engage on Social Media',
    4,
    'Following tech influencers, joining relevant groups, and participating in discussions on platforms like LinkedIn and Twitter can provide real-time updates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Take Online Courses and Webinars',
    5,
    'Enrolling in online courses and attending webinars can help you learn about new technologies and their applications'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Network with Peers',
    6,
    'Sharing ideas and experiences with colleagues and peers can provide insights into how others are leveraging new technologies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Find a Mentor',
    7,
    'Having a mentor who is knowledgeable about the latest technologies can guide you and provide valuable advice'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Watch TED Talks and Tech Videos',
    8,
    'Watching presentations and videos from experts can offer deep insights into emerging technologies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Participate in Online Forums and Communities',
    9,
    'Engaging in forums like Reddit, Stack Overflow, or specialized tech communities can help you stay informed and solve problems'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'Read Industry Reports and Whitepapers',
    10,
    'Reviewing detailed reports and whitepapers from reputable sources can provide in-depth knowledge about technology trends'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you keep up with the latest digital technology trends?'), 
    'None of the above',
    11,
    ''
);

-- Question eight secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Regularly Review and Update',
    1,
    'Periodic reviews and updates are crucial to keep the technology stack current'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Stay Informed on Industry Trends',
    2,
    'Keeping up with the latest trends ensures you are aware of new advancements and best practices'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Implement Continuous Integration and Deployment (CI/CD)',
    3,
    'Automating integration and deployment helps maintain an up-to-date stack'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Conduct Regular Audits',
    4,
    'Regular audits assess performance, security, and scalability, allowing for necessary adjustments'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Engage with the Developer Community',
    5,
    'Participation in developer forums and communities keeps you informed about new tools and practices'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Foster a Culture of Learning',
    6,
    'Encouraging continuous learning and experimentation helps the team stay updated with new technologies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Collaborate with Vendors and Partners',
    7,
    'Working closely with vendors ensures you are aware of new releases and updates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Adopt Modular Architecture',
    8,
    'Designing with modular components allows for easy upgrades without affecting the entire system'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Monitor and Analyze Performance',
    9,
    'Using monitoring tools to track performance helps identify areas for improvement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'Plan for Scalability and Future Growth',
    10,
    'Ensuring the stack is scalable accommodates future growth and changes in business requirements'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you ensure that your technology stack remains up-to-date and relevant?'), 
    'None of the above',
    11,
    ''
);

-- Question nine secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Conduct a Comprehensive Risk Assessment',
    1,
    'Identifying potential threats and vulnerabilities is crucial for understanding the full scope of risks'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Develop a Risk Mitigation Plan',
    2,
     'Creating a plan to address identified risks including contingency measures is essential for preparedness'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Perform a Cost-Benefit Analysis',
    3,
     'Evaluating the financial implications helps in understanding the potential costs and benefits'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Conduct Cybersecurity Assessments',
    4,
     'Ensuring the technology is secure is vital to protect against potential security vulnerabilities'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Implement Pilot Testing',
    5,
     'Testing in a controlled environment helps identify issues before full-scale implementation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Monitor Regulatory Compliance',
    6,
     'Ensuring compliance with relevant regulations and standards avoids legal and compliance risks'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Engage with Stakeholders',
    7,
	'Gathering diverse perspectives from various departments provides a comprehensive view of potential risks'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Analyze Historical Data',
    8,
	'Reviewing past experiences with similar technologies helps identify common risks and mitigation strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Use Risk Assessment Tools',
    9,
	'Utilizing specialized tools and software systematically evaluates and manages risks'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How do you assess the risks associated with the adoption of new technologies?'), 
    'Seek Expert Consultation',
    10,
	'Consulting with industry experts provides valuable insights into potential risks and best practices for mitigation'
);

-- Question ten secton 3

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Communicate the Benefits',
    1,
	'Clearly explaining the advantages helps employees understand the value and reduces resistance'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Involve Employees Early',
    2,
	'Engaging employees in the planning process increases buy-in and reduces pushback'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Provide Comprehensive Training',
    3,
	'Ensuring employees feel confident and competent with the new technology is crucial for smooth adoption'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Address Concerns Openly',
    4,
	'Creating an open forum for concerns builds trust and addresses issues promptly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Implement Change Management Strategies',
    5,
    'A structured change management plan guides the transition effectively'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Foster a Positive Culture',
    6,
    'Promoting a culture that embraces change encourages employees to adapt and experiment'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Provide Ongoing Support',
    7,
    'Continuous support systems help employees during the transition and reduce frustration'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Showcase Success Stories',
    8,
    'Highlighting successful examples builds confidence and demonstrates the technology’s benefits'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Offer Incentive',
    9,
    'Providing incentives for early adopters encourages participation and enthusiasm'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'Monitor and Adjust',
    10,
    'Regularly monitoring the process and making adjustments based on feedback ensures continuous improvement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'What strategies do you use to overcome resistance to new technology adoption?'), 
    'None of the above',
    11,
    ''
);


-- Question one secton 4
INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Market Research and Analysis',
    1,
    'The team conducts regular market research and competitive analysis to understand emerging trends and shifts in the market. This helps us stay ahead of the curve'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Customer Feedback and Insights',
    2,
    'Actively seek feedback from  customers and analyze their behavior and preferences. This helps the company understand market demands and adapt to new trends accordingly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Networking and Conferences',
    3,
    'The team frequently attends industry conferences, webinars, and networking events. These gatherings provide valuable insights and opportunities to learn from experts and peers'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Professional Organizations',
    4,
    'Members of several professional organizations and associations. These memberships provide access to exclusive resources, research, and industry reports'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Regular Industry Reading',
    5,
    'Subscribe to and regularly read industry-specific publications, blogs, and newsletters. This helps us stay informed about the latest trends and developments'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Social Media Monitoring',
    6,
    'Follow key influencers, thought leaders, and organizations on social media platforms like LinkedIn, Twitter, and Facebook. This allows us to get real-time updates and insights'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Technology Tools and Alerts',
    7,
    'Various technology tools and set up alerts for industry keywords. This ensures we receive timely updates on any significant changes or innovations'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Internal Knowledge Sharing',
    8,
    'Regular internal meetings and knowledge-sharing sessions where team members present and discuss the latest trends and how they can be applied to our work'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Online Courses and Certifications',
    9,
    'Encourage our employees to take online courses and earn certifications in relevant digital marketing and technology fields. This continuous learning approach ensures we are always up-to-date'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company stay updated with the latest digital trends in the market?'), 
    'Mentorship and Collaboration',
    10,
    'Have a mentorship program where experienced professionals guide newer team members. Additionally, we collaborate with other companies and experts to share knowledge and best practices'
);

-- Question two secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How have market trends influenced your companys digital maturity?'), 
    'Data-Driven Decision Making',
    1,
    'The rise of big data and analytics has significantly impacted our digital maturity. We now rely heavily on data-driven insights to inform our strategic decisions, optimize operations, and improve overall business performance'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How have market trends influenced your companys digital maturity?'), 
    'Enhanced Customer Experience',
    2,
    'The increasing demand for personalized and seamless customer experiences has driven us to enhance our digital capabilities. We have invested in advanced analytics and AI to better understand and anticipate customer needs, leading to more tailored and engaging interactions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How have market trends influenced your companys digital maturity?'), 
    'Agility and Adaptability',
    3,
    'Market volatility and the need for quick responses to changing conditions have influenced our digital maturity. We have focused on building a more agile and adaptable digital infrastructure, allowing us to pivot quickly and efficiently in response to market shifts'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How have market trends influenced your companys digital maturity?'), 
    'Innovation and Competitive Edge',
    4,
    'Staying ahead of market trends has encouraged us to continuously innovate. By embracing emerging technologies and digital solutions, we have maintained a competitive edge and positioned ourselves as leaders in our industry'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How have market trends influenced your companys digital maturity?'), 
    'Accelerated Digital Transformation',
    5,
    'Market trends, especially the rapid shift towards digital-first interactions, have pushed us to accelerate our digital transformation initiatives. This has involved adopting new technologies and digital tools to stay competitive and meet customer expectations'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How have market trends influenced your companys digital maturity?'), 
    'Operational Efficiency',
    6,
    'Market trends emphasizing efficiency and cost-effectiveness have led us to streamline our operations through digital automation and process optimization. This has not only reduced costs but also improved productivity and service delivery'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How have market trends influenced your companys digital maturity?'), 
    'Employee Empowerment',
    7,
    'The need to keep up with market trends has also impacted our internal processes. We have invested in digital training and upskilling programs for our employees, ensuring they are equipped with the necessary skills to thrive in a digital-first environment'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How have market trends influenced your companys digital maturity?'), 
    'Sustainability Initiatives',
    8,
    'Growing awareness and demand for sustainable practices have influenced our digital maturity. We have integrated digital solutions to monitor and reduce our environmental impact, aligning with market trends towards sustainability'
);

-- Question three secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Adopting AI and Machine Learning',
    1,
    'We plan to integrate AI and machine learning into our operations to enhance decision-making, automate processes, and provide personalized customer experiences. These technologies will help us stay competitive and efficient'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Investing in Data Analytics',
    2,
    'By leveraging advanced data analytics, we aim to gain deeper insights into market trends, customer behavior, and operational performance. This will enable us to make more informed strategic decisions and identify new growth opportunities'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Enhancing Cybersecurity Measures',
    3,
    'As digital threats evolve, we are committed to strengthening our cybersecurity infrastructure. This includes adopting the latest security technologies and protocols to protect our data and ensure the trust of our customers'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Embracing Cloud Computing',
    4,
    'We plan to expand our use of cloud computing to improve scalability, flexibility, and collaboration across our organization. This will allow us to quickly adapt to changing market demands and support remote work'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Developing Digital Products and Services',
    5,
    'We are focused on developing new digital products and services that meet the evolving needs of our customers. This includes leveraging emerging technologies to create innovative solutions that provide value and differentiate us in the market'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Implementing IoT Solutions',
    6,
    'We plan to leverage the Internet of Things (IoT) to optimize our operations, improve asset management, and enhance customer experiences. IoT solutions will provide real-time data and insights that can drive efficiency and innovation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Collaborating with Tech Partners',
    7,
    'We plan to collaborate with leading technology partners to stay at the forefront of digital innovation. These partnerships will provide us with access to cutting-edge technologies and expertise that can drive our digital transformation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Fostering a Culture of Innovation',
    8,
    'Foster a culture of innovation by encouraging experimentation and continuous learning. This includes investing in employee training and development programs to keep our team updated with the latest digital trends'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Exploring Blockchain Technology',
    9,
    'Exploring the potential of blockchain technology to enhance transparency, security, and efficiency in our supply chain and financial transactions. This could lead to significant improvements in trust and operational efficiency'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to leverage emerging digital trends?'), 
    'Sustainability through Digital Solutions',
    10,
    'Leveraging digital technologies to support our sustainability initiatives. This includes using data analytics to monitor and reduce our environmental impact and adopting energy-efficient technologies'
);

-- Question four secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Leveraging Data and Analytics',
    1,
    'Leverage advanced data analytics to gain insights into market trends and consumer behavior. This data-driven approach helps make informed decisions and optimize digital strategy for better results'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Continuous Market Analysis',
    2,
    'Conduct ongoing market analysis to identify emerging trends and shifts in consumer behavior. This allows proactively adjust digital strategy to stay ahead of the curve and meet evolving customer needs'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Customer Feedback Integration',
    3,
    'Actively seek and integrate customer feedback into digital strategy. By understanding customers’ preferences and pain points can tailor our digital initiatives to better serve their needs'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Agile Methodologies',
    4,
    'Employ agile methodologies in digital projects, enabling  to quickly pivot and adapt to new market trends. This flexibility ensures that we can implement changes rapidly and efficiently'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Investing in Emerging Technologies',
    5,
    'Continuously invest in emerging technologies such as AI, machine learning, and blockchain. These technologies enable innovation and stay competitive in a rapidly changing digital landscape'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Monitoring Competitor Strategies',
    6,
    'Keep a close eye on competitors’ digital strategies to identify best practices and areas for improvement. This competitive intelligence helps us refine our own strategy and stay ahead in the market'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Adapting Marketing Channels',
    7,
    'Regularly evaluate and adapt marketing channels based on market trends. This includes exploring new platforms and adjusting our content strategy to ensure maximum reach and engagement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Collaborative Innovation',
    8,
    'Foster a culture of collaborative innovation by encouraging cross-functional teams to work together on digital projects. This approach ensures diverse perspectives and ideas are considered, leading to more effective and innovative solutions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Strategic Partnerships',
    9,
    'Form strategic partnerships with technology providers and industry experts to leverage their expertise and stay updated with the latest digital innovations. These partnerships help us enhance our digital capabilities and stay competitive'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company adapt its digital strategy based on market trends?'), 
    'Employee Training and Development',
    10,
    'Invest in continuous training and development for employees to keep them updated with the latest digital trends and skills. This ensures our team is well-equipped to implement and adapt our digital strategy effectively'
);

-- Question five secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Advanced Data Analytics',
    1,
    'Utilize advanced data analytics tools to analyze vast amounts of data from various sources. This helps identify patterns and predict future trends with greater accuracy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Leveraging AI and Machine Learning',
    2,
    'Leverage AI and machine learning algorithms to process and analyze data. These technologies help identify trends and make predictions based on historical data and current market conditions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Using Predictive Analytics',
    3,
    'Use predictive analytics to forecast future market trends based on historical data and current market conditions. This helps make informed decisions and stay proactive in the approach'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Market Research and Surveys',
    4,
    'Conduct regular market research and surveys to gather insights directly from consumers and industry experts. This helps stay informed about emerging trends and shifts in the market'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Monitoring Industry Reports',
    5,
    'Keep a close eye on industry reports and publications from leading market research firms. These reports provide valuable forecasts and trend analyses that inform our strategic planning'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Customer Feedback and Behavior Analysis',
    6,
    'Analyze customer feedback and behavior to understand their evolving needs and preferences. This helps anticipate market trends and tailor strategies accordingly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Competitive Analysis',
    7,
    'Conduct thorough competitive analysis to understand how competitors are adapting to market trends. This helps identify opportunities and threats, and adjust strategies accordingly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Trend Monitoring Tools',
    8,
    'Use various trend monitoring tools and platforms to track emerging trends in real-time. These tools provide with timely updates and alerts on significant changes in the market'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Engaging with Thought Leaders',
    9,
    'Actively engage with industry thought leaders and influencers through conferences, webinars, and social media. Their insights and perspectives help stay ahead of the curve and anticipate future trends'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company predict future digital trends in the market?'), 
    'Collaborating with Tech Partners',
    10,
    'Collaborate with technology partners and startups to gain access to cutting-edge innovations and insights. These partnerships help stay updated with the latest advancements and predict future trends'
);

-- Question six secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Investing in Emerging Technologies',
    1,
    'Actively invest in emerging technologies such as AI, machine learning, and blockchain. By staying at the forefront of technological advancements, ensure our operations remain innovative and competitive'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Continuous Learning and Development',
    2,
    'Prioritize continuous learning and development for employees. This includes offering regular training programs, workshops, and access to online courses to ensure team stays updated with the latest digital skills and technologies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Agile and Flexible Approach',
    3,
    'Adopt an agile and flexible approach to projects and processes. This allows to quickly adapt to new digital trends and market demands, ensuring  it remains relevant and responsive'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Customer-Centric Focus',
    4,
    'Maintain a strong focus on  customers’ needs and preferences. By leveraging data analytics and customer feedback,  continuously refine  digital strategies to enhance customer experiences and meet evolving market demands'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Strategic Partnerships',
    5,
    'Form strategic partnerships with leading technology providers and industry experts. These collaborations provide  access to cutting-edge innovations and insights, helping it  stay ahead in the digital race'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Innovation Culture',
    6,
    'Foster a culture of innovation within the organization. Encouraging creativity and experimentation among  employees ensures that  they are always exploring new ideas and solutions to stay competitive'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Regular Market Analysis',
    7,
    'Conduct regular market analysis to monitor emerging trends and shifts in the industry. This proactive approach helps  anticipate changes and adjust  digital strategies accordingly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Upskilling and Reskilling',
    8,
    'Focus on upskilling and reskilling workforce to bridge any digital skills gaps. This ensures employees are equipped with the necessary skills to leverage new technologies and drive digital transformation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Cybersecurity Measures',
    9,
    'Prioritize robust cybersecurity measures to protect digital assets and customer data. Staying ahead of potential threats ensures operations remain secure and trustworthy'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company ensure that it is not left behind in the digital race?'), 
    'Adopting Best Practices',
    10,
    'Continuously adopt and implement best practices in digital transformation. Learning from industry leaders and benchmarking against top performers helps stay competitive and efficient'
);

-- Question seven secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Data-Driven Insights',
    1,
    'Leverage data analytics to monitor market trends and consumer behavior. This helps identify emerging patterns and adjust digital marketing strategies to target the right audience with the right message at the right time'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Personalization and Customer Experience',
    2,
    'By analyzing market trends to better understand customers’ preferences and expectations. This allows you to create personalized marketing campaigns that enhance customer experience and drive engagement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Adapting to Technological Advancements',
    3,
    'Keeping an eye on technological trends allows you to adopt new tools and platforms that can enhance digital marketing efforts. This includes utilizing  AI, machine learning, and automation to improve campaign efficiency and effectiveness'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Content Strategy Optimization',
    4,
    'Use market trends to inform our content strategy, ensuring that content is relevant, timely, and resonates with the target audience. This includes creating content around trending topics and using popular formats like videos and infographics'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Social Media Engagement',
    5,
    'Monitoring trends on social media platforms helps stay relevant and engage with the audience effectively. Tailor social media strategies to align with current trends, increasing reach and engagement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'SEO and SEM Strategies',
    6,
    'Market trends influence search engine optimization (SEO) and search engine marketing (SEM) strategies. By staying updated with the latest search trends and algorithm changes can optimize online presence and improve search rankings'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Competitive Analysis',
    7,
    'Continuously analyze competitors’ strategies and market positioning. Understanding how they respond to market trends helps refine our own strategies and identify opportunities for differentiation'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Customer Feedback and Surveys',
    8,
    'Regularly collect and analyze customer feedback and conduct surveys to understand market trends from the consumer’s perspective. This direct input helps refine digital marketing strategies to better meet customer needs'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Influencer and Partnership Collaborations',
    9,
    'Identify and collaborate with influencers and partners who are aligned with current market trends. This helps us expand reach and credibility within target market'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its digital marketing strategy?'), 
    'Agile Marketing Approach',
    10,
    'Adopt an agile marketing approach, allowing you to quickly adapt strategies based on real-time market trends. This flexibility ensures that remain responsive and relevant in a fast-changing digital landscape'
);

-- Question eight secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its product development strategy?'), 
    'Continuous Market Research',
    1,
    'Staying updated on the latest trends and consumer preferences is crucial for making informed decisions and staying competitive'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its product development strategy?'), 
    'Customer Feedback and Surveys',
    2,
    'Direct feedback from customers provides valuable insights into their needs and preferences, which can directly influence product development'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its product development strategy?'), 
    'Competitive Analysis',
    3,
    'Understanding competitors’ strategies and market positioning helps in identifying opportunities and threats, allowing for strategic adjustments'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its product development strategy?'), 
    'Trend Analysis Tools',
    4,
    'Utilizing advanced tools and software for trend analysis and prediction helps in anticipating market shifts and preparing accordingly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its product development strategy?'), 
    'Industry Reports and Publications',
    5,
    'Reviewing industry reports and publications provides a broader perspective on market dynamics and future trends'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its product development strategy?'), 
    'Collaborations and Partnerships',
    6,
    'Collaborating with industry experts and partners can bring in new technologies and insights, though it might be less frequent than other methods'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its product development strategy?'), 
    'None of the above',
    7,
    ''
);

-- Question nine secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its customer service strategy?'), 
    'Personalized Customer Interactions',
    1,
    'Tailoring responses and recommendations to individual customers significantly enhances satisfaction and loyalty'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its customer service strategy?'), 
    'Omnichannel Integration',
    2,
    'Providing a seamless experience across multiple channels ensures customers can easily reach support through their preferred method'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its customer service strategy?'), 
    'Adopting AI-Powered Support',
    3,
    'Implementing AI and machine learning improves efficiency and allows for 24/7 support, addressing common issues quickly'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its customer service strategy?'), 
    'Voice of Customer (VoC) Programs',
    4,
    'Collecting and analyzing customer feedback helps identify and address pain points, improving overall service quality'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its customer service strategy?'), 
    'Proactive Customer Support',
    5,
    'Anticipating customer needs and issues before they arise can prevent problems and enhance the customer experience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its customer service strategy?'), 
    'Enhanced Data Privacy and Security',
    6,
    'Prioritizing data privacy and security builds trust which is increasingly important to customers'
);

-- Question ten secton 4

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its sales strategy?'), 
    'Identifying Emerging Markets',
    1,
    'Discovering new and growing markets can open up significant opportunities for sales expansion'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its sales strategy?'), 
    'Sales Forecasting',
    2,
    'Accurate sales forecasts based on trend analysis help in better inventory management and setting realistic sales targets'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its sales strategy?'), 
    'Adjusting Sales Tactics',
    3,
    'Adapting sales tactics to current market conditions and consumer preferences ensures the company remains competitive and relevant'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its sales strategy?'), 
    'Product Positioning and Messaging',
    4,
    'Refining product positioning and marketing messages based on trends can attract more customers and enhance brand perception'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its sales strategy?'), 
    'Customer Segmentation',
    5,
    'Tailoring sales approaches to different customer segments based on emerging trends can improve customer engagement and conversion rates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its sales strategy?'), 
    'Competitive Benchmarking',
    6,
    'Monitoring competitors to understand their strategies and market positioning helps in identifying opportunities and threats'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use market trends to inform its sales strategy?'), 
    'None of the above',
    7,
    ''
);

-- Question one secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Search Engine Optimization (SEO)',
    1,
    'Optimizing website content to rank higher in search engine results is crucial for increasing organic traffic and visibility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Social Media Marketing',
    2,
    'Engaging with the audience on social media platforms helps build brand awareness and connect with potential customers'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Content Marketing',
    3,
    'Creating valuable and relevant content establishes the company as an authority in its industry and builds trust with the audience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Pay-Per-Click (PPC) Advertising',
    4,
    'Using targeted PPC ads drives traffic to the website and can lead to higher conversion rates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Email Marketing',
    5,
    'Sending personalized emails keeps subscribers informed and engaged, leading to increased customer loyalty and conversions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Influencer Marketing',
    6,
    'Partnering with influencers can extend the company’s reach and credibility, especially within specific target markets'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Video Marketing',
    7,
    'Creating and sharing videos to engage the audience can effectively showcase the brand and its offerings'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Retargeting Campaigns',
    8,
    'Using retargeting ads to re-engage visitors who have previously interacted with the website can encourage them to complete purchases'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Affiliate Marketing',
    9,
    'Partnering with affiliates who promote the company’s products for a commission can expand the company’s reach and drive sales'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company leverage digital marketing to reach its target audience?'), 
    'Webinars and Live Streams',
    10,
    'Hosting online events to interact with the audience in real-time can engage and educate the audience, fostering a deeper connection with the brand'
);

-- Question two secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Return on Investment (ROI)',
    1,
    'Calculating the financial return generated from digital marketing activities relative to the cost is crucial for understanding overall effectiveness'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Conversion Rate',
    2,
    'Measuring the percentage of website visitors who complete a desired action helps determine the effectiveness of marketing strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Customer Acquisition Cost (CAC)',
    3,
    'Determining the cost associated with acquiring a new customer provides insights into the efficiency of marketing efforts'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Customer Lifetime Value (CLV)',
    4,
    'Estimating the total revenue from a single customer account over time helps understand the long-term value of marketing efforts'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Website Traffic',
    5,
    'Monitoring the number of visitors to the company’s website provides a broad view of the reach and impact of digital marketing'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Lead Generation',
    6,
    'Measuring the number of leads generated helps assess the effectiveness of campaigns in attracting potential customers'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Engagement Metrics',
    7,
    'Tracking user interactions with content on social media and other platforms gauges audience engagement and interest'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Social Media Metrics',
    8,
    'Evaluating the performance of social media campaigns helps understand their impact and reach'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Email Open and Click-Through Rates',
    9,
    'Monitoring the effectiveness of email marketing campaigns provides insights into audience engagement and campaign impact'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company measure the success of its digital marketing efforts?'), 
    'Bounce Rate',
    10,
    'Measuring the percentage of visitors who leave the website after viewing only one page helps identify potential issues with content or user experience'
);

-- Question three secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Utilizing Data Analytics',
    1,
    'Analyzing data to gain insights into customer behavior and campaign performance is crucial for making informed decisions and optimizing strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Enhancing SEO Practices',
    2,
    'Continuously optimizing website content to improve search engine rankings helps increase organic traffic and visibility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Expanding Social Media Presence',
    3,
    'Increasing engagement and reach on social media platforms helps build brand awareness and connect with a broader audience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Investing in Content Marketing',
    4,
    'Producing high-quality, valuable content attracts and retains the target audience, establishing the company as an authority in its industry'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Improving Email Marketing Campaigns',
    5,
    'Enhancing the effectiveness of email marketing efforts through personalization and A/B testing can lead to higher engagement and conversion rates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Implementing Marketing Automation',
    6,
    'Using automation tools to streamline marketing processes saves time and increases efficiency, allowing for more consistent and targeted campaigns'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Leveraging Influencer Partnerships',
    7,
    'Collaborating with influencers to reach a broader audience can enhance credibility and extend the company’s reach'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Expanding Video Marketing',
    8,
    'Increasing the use of video content to engage the audience can effectively showcase the brand and its offerings'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Optimizing Mobile Marketing',
    9,
    'Ensuring marketing efforts are mobile-friendly enhances user experience on smartphones and tablets, which is increasingly important as mobile usage grows'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company plan to improve its digital marketing strategies?'), 
    'Focusing on Customer Experience',
    10,
    'Enhancing the overall customer journey and experience through feedback loops and continuous improvement builds customer loyalty and satisfaction'
);

-- Question four secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Defining Goals and Key Performance Indicators (KPIs)',
    1,
    'Setting clear marketing goals and identifying KPIs is crucial for measuring the success of marketing campaigns'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Analyzing and Interpreting Data',
    2,
    'Using statistical methods to uncover insights and trends from the data helps inform targeted marketing strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Personalizing Marketing Campaigns',
    3,
    'Tailoring marketing messages and offers based on customer data and behavior can significantly enhance engagement and conversion rates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Predictive Analytics',
    4,
    'Using historical data to predict future trends and customer behavior allows for proactive and strategic marketing efforts'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Optimizing Marketing Channels',
    5,
    'Evaluating the performance of different marketing channels ensures resources are allocated to the most effective ones'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Real-Time Analytics',
    6,
    'Monitoring marketing performance in real-time allows for quick adjustments and optimization during live campaigns'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'A/B Testing',
    7,
    'Conducting experiments to compare different versions of marketing materials helps determine the most effective strategies'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Customer Journey Mapping',
    8,
    'Analyzing the customer journey to understand touchpoints and improve the overall experience enhances customer satisfaction and loyalty'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Collecting and Cleansing Data',
    9,
    'Ensuring the accuracy and relevance of data is fundamental for reliable analysis and insights'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use data analytics in its digital marketing efforts?'), 
    'Reporting and Visualization',
    10,
    'Creating visual reports to communicate insights and performance metrics makes it easier for stakeholders to understand and act on the data'
);

-- Question five secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'Keyword Research',
    1,
    'Identifying relevant keywords that potential customers are using to search for products or services is fundamental for effective SEO'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'On-Page Optimization',
    2,
    'Optimizing individual web pages to rank higher and earn more relevant traffic ensures that content is easily discoverable by search engines'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'Content Creation',
    3,
    'Producing high-quality, valuable content that addresses the needs and interests of the target audience is crucial for attracting and retaining visitors'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'Technical SEO',
    4,
    'Improving the technical aspects of the website, such as page load times and mobile-friendliness, enhances performance and visibility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'Link Building',
    5,
    'Acquiring high-quality backlinks from reputable websites improves domain authority and search engine rankings'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'User Experience (UX) Optimization',
    6,
    'Enhancing the overall user experience on the website reduces bounce rates and increases engagement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'Local SEO',
    7,
    'Optimizing the website for local search results helps attract nearby customers and improve local visibility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'Regular Audits and Updates',
    8,
    'Conducting regular SEO audits to identify and fix issues keeps the website up-to-date with the latest SEO best practices'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'Analytics and Reporting',
    9,
    'Monitoring and analyzing SEO performance helps measure success and identify areas for improvement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company handle SEO for its digital content?'), 
    'Competitor Analysis',
    10,
    'Analyzing competitors’ SEO strategies provides insights into opportunities and threats, informing and improving the company’s own efforts'
);

-- Question six secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Building Brand Awareness',
    1,
    'Increasing visibility and recognition of the brand is fundamental for establishing a strong market presence'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Engaging with Customers',
    2,
    'Interacting with customers through comments, messages, and posts helps build a community and foster customer loyalty'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Running Paid Advertising Campaigns',
    3,
    'Using paid ads on social media platforms to reach a targeted audience can significantly boost reach and conversions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Content Promotion',
    4,
    'Sharing valuable content to drive traffic to the company’s website enhances engagement and brand authority'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Providing Customer Support',
    5,
    'Offering customer service through social media channels ensures quick and efficient support, improving customer satisfaction'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Influencer Collaborations',
    6,
    'Partnering with influencers to promote products and services leverages their follower base and enhances credibility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Social Listening',
    7,
    'Monitoring social media channels for mentions of the brand, competitors, and industry trends helps respond quickly to feedback and stay ahead of trends'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Analyzing Performance Metrics',
    8,
    'Tracking and analyzing social media metrics to measure the effectiveness of campaigns allows for data-driven strategy adjustments'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Hosting Contests and Giveaways',
    9,
    'Engaging the audience through interactive campaigns like contests and giveaways increases engagement and brand visibility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use social media in its digital marketing strategy?'), 
    'Creating a Content Calendar',
    10,
    'Planning and scheduling social media posts in advance ensures consistent and strategic content delivery'
);

-- Question seven secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Personalized Campaigns',
    1,
    'Sending tailored emails based on customer preferences and behaviors significantly enhances engagement and conversion rates'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Automated Email Sequences',
    2,
    'Setting up automated email workflows to nurture leads and engage customers ensures consistent communication and efficient lead nurturing'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Promotional Emails',
    3,
    'Sending emails to promote sales, special offers, and new products drives immediate sales and boosts revenue'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Abandoned Cart Emails',
    4,
    'Sending reminders to customers who have left items in their online shopping carts helps recover potentially lost sales'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Newsletters',
    5,
    'Regularly sending newsletters keeps subscribers informed and engaged, maintaining a strong relationship with the audience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Transactional Emails',
    6,
    'Sending order confirmations, shipping notifications, and other transactional emails enhances the post-purchase experience and builds trust'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Re-engagement Campaigns',
    7,
    'Reconnecting with inactive subscribers helps bring them back into the fold and re-engage with the brand'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Event Invitations',
    8,
    'Using email to invite customers to webinars, product launches, and other events increases participation and engagement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Surveys and Feedback Requests',
    9,
    'Gathering customer feedback through email surveys provides valuable insights for improving products and services'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use email marketing in its digital marketing strategy?'), 
    'Educational Content',
    10,
    'Sharing informative and educational content adds value to subscribers and establishes the company as an authority in its field'
);

-- Question eight secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'Creating Valuable Blog Content',
    1,
    'Producing informative and engaging blog posts that address the needs and interests of the target audience is fundamental for attracting and educating potential customers'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'SEO Optimization',
    2,
    'Ensuring all content is optimized for search engines improves visibility and attracts organic traffic, making it easier for potential customers to find the content'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'Developing Video Content',
    3,
    'Creating videos to explain products, share customer testimonials, and provide educational content engages viewers and builds trust'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'Utilizing Social Media',
    4,
    'Sharing content across social media platforms helps reach a wider audience and drive traffic to the website'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'Publishing Ebooks and Whitepapers',
    5,
    'Offering in-depth resources that provide valuable insights and solutions to common problems establishes the company as an authority in its field'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'Hosting Webinars and Live Events',
    6,
    'Conducting online events to educate and interact with the audience in real-time provides value and establishes authority in the industry'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'Email Newsletters',
    7,
    'Sending regular newsletters keeps subscribers informed and engaged with valuable content, maintaining a strong relationship with the audience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'Creating Infographics',
    8,
    'Designing visually appealing infographics simplifies complex information and makes it easily digestible, enhancing engagement'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'Podcasting',
    9,
    'Producing podcasts to discuss industry trends, interview experts, and share company updates provides valuable insights and entertainment'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use content marketing in its digital marketing strategy?'), 
    'User-Generated Content',
    10,
    'Encouraging customers to create and share their own content related to the brand increases engagement and builds a community around the brand'
);

-- Question nine secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Partnering with Relevant Influencers',
    1,
    'Collaborating with influencers who align with the brand’s values and target audience ensures that the promotion reaches the right people'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Creating Authentic Content',
    2,
    'Encouraging influencers to create genuine and relatable content resonates more with their audience, leading to higher engagement and trust'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Leveraging Micro-Influencers',
    3,
    'Partnering with micro-influencers who have smaller but highly engaged followings can be more cost-effective and targeted'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Tracking and Analyzing Performance',
    4,
    'Monitoring the performance of influencer campaigns to measure their effectiveness allows for data-driven adjustments and improvements'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Building Long-Term Relationships',
    5,
    'Establishing ongoing partnerships with influencers creates consistent and long-term collaborations, strengthening the association between the influencer and the brand'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Utilizing Influencer Reviews and Testimonials',
    6,
    'Having influencers provide honest reviews and testimonials builds trust and credibility with their followers'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Creating Sponsored Content',
    7,
    'Paying influencers to create and share content that promotes the brand can significantly boost visibility and reach'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Hosting Giveaways and Contests',
    8,
    'Partnering with influencers to run giveaways and contests encourages audience participation and increases brand visibility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Running Influencer Takeovers',
    9,
    'Allowing influencers to take over the brand’s social media accounts for a day can provide fresh and engaging content'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use influencer marketing in its digital marketing strategy?'), 
    'Utilizing Influencer Content Across Channels',
    10,
    'Repurposing influencer-generated content for use across various marketing channels maximizes its reach and impact'
);

-- Question ten secton 5

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Product Demonstrations',
    1,
    'Showcasing how products work and their benefits helps potential customers understand the product better and make informed purchasing decisions'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Customer Testimonials',
    2,
    'Sharing videos of satisfied customers builds trust and credibility, showing real-life success stories that can influence potential buyers'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Educational Content',
    3,
    'Producing how-to videos, tutorials, and webinars provides valuable information and positions the company as an industry expert'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Video Ads',
    4,
    'Running video advertisements on platforms like YouTube, Facebook, and Instagram targets specific demographics and drives traffic to the company’s website or landing pages'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Social Media Videos',
    5,
    'Creating short, engaging videos for social media platforms captures the audience’s attention quickly and increases brand visibility'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Live Streaming',
    6,
    'Engaging with the audience in real-time through live video broadcasts creates a sense of immediacy and allows for direct interaction with customers'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Explainer Videos',
    7,
    'Simplifying complex concepts or processes through animated or live-action explainer videos makes it easier for the audience to understand the product or service'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Behind-the-Scenes Footage',
    8,
    'Offering a glimpse into the company’s operations and culture humanizes the brand and builds a stronger connection with the audience'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'User-Generated Content',
    9,
    'Encouraging customers to create and share their own videos featuring the company’s products fosters community engagement and authentic promotion'
);

INSERT INTO answers (questionsId, answer, weighting, solution)
VALUES (
    (SELECT id FROM questions WHERE question = 'How does your company use video marketing in its digital marketing strategy?'), 
    'Interactive Videos',
    10,
    'Producing videos that allow viewers to interact and make choices within the video enhances engagement and provides a personalized experience'
);

SELECT * FROM answers