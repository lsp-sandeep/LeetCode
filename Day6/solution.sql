SELECT
    L.name AS Employee
FROM Employee AS L
LEFT JOIN Employee AS R
    ON L.managerId = R.id
WHERE L.salary > R.salary
;