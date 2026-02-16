SELECT e.name as Employee
FROM Employee e
JOIN Employee as emp
ON e.managerId = emp.id
WHERE e.salary > emp.salary;
