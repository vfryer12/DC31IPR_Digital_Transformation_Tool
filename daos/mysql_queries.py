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