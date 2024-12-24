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

GET_USER_SOLUTIONS ="""with user_answers as
(
	select ua.questionsid
		, ua.answersId
from userAnswers as ua
where ua.userId = %s
)

, ranked_answers as 
(
select a.questionsId
	, answersId
	, weighting
	, solution
	, ROW_NUMBER() over(
		PARTITION by a.questionsId
order by
		weighting asc
	) as weight_row_rank
from user_answers as ua
inner join answers as a on
	ua.questionsid = a.questionsid
)

SELECT questionsId, answersId, weighting,solution, weight_row_rank
FROM(
SELECT ra.*
, max(case when ua.answersId = ra.answersId then weight_row_rank else NULL end) over(PARTITION by ra.questionsId) as user_weight_row_rank
from ranked_answers as ra
left join user_answers as ua on
ua.answersId = ra.answersId
) AS X
WHERE weight_row_rank <= 3
and weight_row_rank <= user_weight_row_rank
"""