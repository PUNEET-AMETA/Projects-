CREATE DATABASE hr_analytics;
USE hr_analytics;
select * from employees;

SELECT
ROUND(
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0
/
COUNT(*),
2
) AS Attrition_Rate
FROM employees;

SELECT
Department,
COUNT(*) AS TotalEmployees,
SUM(
CASE
WHEN Attrition='Yes'
THEN 1
ELSE 0
END
) AS EmployeesLeft
FROM employees
GROUP BY Department;

SELECT
OverTime,
COUNT(*) AS TotalEmployees,
SUM(
CASE
WHEN Attrition='Yes'
THEN 1
ELSE 0
END
) AS AttritionCount
FROM employees
GROUP BY OverTime;

SELECT
JobRole,
COUNT(*) TotalEmployees,
SUM(
CASE
WHEN Attrition='Yes'
THEN 1
ELSE 0
END
) EmployeesLeft
FROM employees
GROUP BY JobRole
ORDER BY EmployeesLeft DESC;

SELECT
MaritalStatus,
COUNT(*) TotalEmployees,
SUM(
CASE
WHEN Attrition='Yes'
THEN 1
ELSE 0
END
) AttritionCount
FROM employees
GROUP BY MaritalStatus;


SELECT
Attrition,
AVG(MonthlyIncome) AvgSalary
FROM employees
GROUP BY Attrition;

SELECT
JobSatisfaction,
COUNT(*) Employees,
SUM(
CASE
WHEN Attrition='Yes'
THEN 1
ELSE 0
END
) AttritionCount
FROM employees
GROUP BY JobSatisfaction;


SELECT
BusinessTravel,
COUNT(*) Employees,
SUM(
CASE
WHEN Attrition='Yes'
THEN 1
ELSE 0
END
) AttritionCount
FROM employees
GROUP BY BusinessTravel;

