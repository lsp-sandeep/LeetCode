SELECT
    MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)
ORDER BY 1 DESC
;