-- problem 177 leetcode: https://leetcode.com/problems/nth-highest-salary/description/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare M int;
set M = N-1; #to get N-th highest salary, you need to skip the first N-1 salaries
RETURN (
    SELECT DISTINCT Salary from Employee order by Salary Desc Limit M,1
);
END 