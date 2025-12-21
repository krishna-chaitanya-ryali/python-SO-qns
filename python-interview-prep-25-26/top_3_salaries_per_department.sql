WITH RankedSalaries AS (
    SELECT
        e.EmployeeName,
        d.DepartmentName,
        e.Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.DepartmentID
            ORDER BY e.Salary DESC
        ) AS SalaryRank
    FROM Employees e
    JOIN Departments d
        ON e.DepartmentID = d.DepartmentID
)

SELECT
    DepartmentName,
    EmployeeName,
    Salary
FROM RankedSalaries
WHERE SalaryRank <= 3;

--I use a window function with DENSE_RANK() partitioned by department to
--rank salaries and then filter the top three per department.”