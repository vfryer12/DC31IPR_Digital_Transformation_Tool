USER_ANSWER_WEIGHTS = """WITH sectquest
AS (
	SELECT s.section
		,q.id AS questionsId
	FROM sections AS s
	INNER JOIN questions AS q ON q.sectionid = s.id
	)
	,useransweight
AS (
	SELECT ua.answersId
		,a.weighting
		,a.questionsId
	FROM useranswers AS ua
	INNER JOIN answers AS a ON ua.answersId = a.id
	WHERE ua.userid = %s
	)
	,section_answer_weight
AS (
	SELECT sq.section
		,uw.answersid
		,uw.weighting
	FROM useransweight AS uw
	INNER JOIN sectquest AS sq ON uw.questionsId = sq.questionsId
	)
SELECT section
	,answersid
	,weighting
FROM section_answer_weight
"""

GET_USER_SOLUTIONS ="""WITH user_answers AS (
        SELECT ua.questionsid, ua.answersId
        FROM userAnswers AS ua
        WHERE ua.userId = %s
    ),
    ranked_answers AS (
        SELECT q.question, a.questionsid, a.id AS answersId, a.weighting, a.solution, q.sectionid,
               ROW_NUMBER() OVER(PARTITION BY a.questionsId ORDER BY a.weighting ASC) AS weight_row_rank
        FROM user_answers AS ua
        INNER JOIN answers AS a ON ua.questionsid = a.questionsid
        inner join questions as q on q.id = a.questionsid
    )
    SELECT question, questionsid, answersId, weighting, solution, weight_row_rank, sectionid
    FROM (
        SELECT ra.*, 
               MAX(CASE WHEN ua.answersId = ra.answersId THEN weight_row_rank ELSE NULL END) 
               OVER (PARTITION BY ra.questionsId) AS user_weight_row_rank
        FROM ranked_answers AS ra
        LEFT JOIN user_answers AS ua ON ua.answersId = ra.answersId
    ) AS X
    WHERE weight_row_rank <= 3 AND weight_row_rank <= user_weight_row_rank;
"""