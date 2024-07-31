-- Problem 180: https://leetcode.com/problems/consecutive-numbers/solutions/3359304/easy-and-simple-solution-using-lead-try-this/

-- cte is common table expression where you can write auxillary queries to generate temporarily uses. only exist
    --during the duration of the queries

--lead(col_name,nums) over() is retrieves the value of col_name from the nums row (nums row ahead)

WITH cte AS (
    SELECT num,
           LEAD(num, 1) OVER() AS num1,
           LEAD(num, 2) OVER() AS num2
    FROM logs
    ORDER by id asc
)

SELECT DISTINCT num AS ConsecutiveNums 
FROM cte 
WHERE (num = num1) AND (num = num2)


-- another solution using inner queries
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        id,
        LAG(num) OVER (ORDER BY id) AS PrevNum,
        num,
        LEAD(num) OVER (ORDER BY id) AS NextNum
    FROM Logs) l
WHERE num = PrevNum AND num = NextNum