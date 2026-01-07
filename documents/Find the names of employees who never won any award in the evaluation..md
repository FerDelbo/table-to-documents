This document provides a SQL query to identify employees who have not received any awards in evaluations, along with an explanation of how the query works.

## Find Employees Who Never Won Any Award in Evaluation

To retrieve the names of employees who have not received any awards in the evaluation system, you can use a SQL query that checks for `employee_id` values not present in the `evaluation` table.

### SQL Query

```sql
SELECT name
FROM employee
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM evaluation
);
```

### Explanation

This query works by utilizing a subquery to identify all `employee_id`s that *do* exist in the `evaluation` table (meaning they have received at least one award or evaluation). The main query then selects employee names whose `employee_id` is *not* found in the results of this subquery.

1.  **`SELECT name FROM employee`**: This is the outer query that selects the `name` column from the `employee` table. This is the ultimate information we want to retrieve.
2.  **`WHERE employee_id NOT IN (...)`**: This clause filters the results from the `employee` table. It includes only those employees whose `employee_id` is *not* present in the set of `employee_id`s returned by the subquery.
3.  **`(SELECT employee_id FROM evaluation)`**: This is the subquery. It selects all unique `employee_id`s from the `evaluation` table. Each `employee_id` in this result set represents an employee who has received at least one award or evaluation.

By combining these parts, the query effectively lists the names of all employees who have no corresponding entries in the `evaluation` table, thus identifying those who have never won any award.

### Tables Involved

*   **`employee`**: Contains information about employees, including their `name` and `employee_id`.
*   **`evaluation`**: Records details about employee evaluations or awards, linked by `employee_id`.