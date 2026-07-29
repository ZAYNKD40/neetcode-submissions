-- Write your query below
--want student highest score and exam id, if same high score on multiple exam return with smallest exam_id so order by exam id ASC?
-- return student_id, exam_id and score, ordered by student id)
Select distinct on (student_id) student_id, exam_id, score -- only choose the first one, distinct on distinct condition
From exam_results
Order by student_id, score desc, exam_id -- priority order