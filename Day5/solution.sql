WITH BASE AS (
    SELECT
        id, 
        LAG(num) OVER(ORDER BY id) AS prev_num,
        num AS curr_num,
        LEAD(num) OVER(ORDER BY id) AS next_num
    FROM Logs
)
SELECT DISTINCT
    curr_num AS ConsecutiveNums
FROM BASE
WHERE prev_num = curr_num AND next_num = curr_num
;