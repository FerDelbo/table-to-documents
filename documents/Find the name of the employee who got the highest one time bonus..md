This document outlines the SQL query required to find the name of the employee who received the highest one-time bonus, along with a detailed explanation of the query's components.

## Find the Employee with the Highest One-Time Bonus

To identify the employee with the highest one-time bonus, we need to query the `employee` and `evaluation` tables, join them on their common employee ID, and then sort the results by bonus in descending order, taking only the top entry.

### SQL Query

```sql
SELECT T1.name
FROM employee AS T1
JOIN evaluation AS T2
  ON T1.employee_id = T2.employee_id
ORDER BY T2.bonus DESC
LIMIT 1;
```

### Explanation

Let's break down the SQL query step by step:

1.  **`SELECT T1.name`**:
    *   This clause specifies that we want to retrieve the `name` column.
    *   `T1` is an alias for the `employee` table, making the query more concise and readable.

2.  **`FROM employee AS T1`**:
    *   This indicates that our primary data source is the `employee` table, aliased as `T1`. This table presumably contains employee details, including their names.

3.  **`JOIN evaluation AS T2 ON T1.employee_id = T2.employee_id`**:
    *   This performs an `INNER JOIN` between the `employee` table (`T1`) and the `evaluation` table (`T2`).
    *   The `ON T1.employee_id = T2.employee_id` condition links rows from both tables where the `employee_id` matches. This is crucial for connecting an employee's name to their bonus information. The `evaluation` table is expected to contain bonus amounts and be linked to employees via `employee_id`.

4.  **`ORDER BY T2.bonus DESC`**:
    *   This clause sorts the joined results.
    *   `T2.bonus` refers to the bonus amount from the `evaluation` table.
    *   `DESC` specifies a descending order, meaning the highest bonus amounts will appear first.

5.  **`LIMIT 1`**:
    *   This clause restricts the output to only the first row after sorting. Since we sorted by `bonus` in descending order, this effectively gives us the employee associated with the highest bonus.

### Result

This query will return a single result: the **name** of the employee who received the largest one-time bonus. If multiple employees have the exact same highest bonus, the specific employee returned might depend on the database system's default tie-breaking behavior (e.g., based on `employee_id`).