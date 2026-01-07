The question asks to identify the employee who received the biggest bonus, returning their name.

The SQL query to achieve this is:

```sql
SELECT T1.name FROM employee AS T1 JOIN evaluation AS T2 ON T1.employee_id = T2.employee_id ORDER BY T2.bonus DESC LIMIT 1
```

### Explanation:

1.  **`SELECT T1.name`**: This specifies that the query should return the `name` column from the `employee` table (aliased as `T1`).
2.  **`FROM employee AS T1 JOIN evaluation AS T2 ON T1.employee_id = T2.employee_id`**: This performs an inner join between the `employee` table (`T1`) and the `evaluation` table (`T2`). The join condition `T1.employee_id = T2.employee_id` links employees to their evaluations based on their common `employee_id`.
3.  **`ORDER BY T2.bonus DESC`**: This sorts the results in descending order based on the `bonus` column from the `evaluation` table (`T2`). This ensures that the employee with the highest bonus appears first.
4.  **`LIMIT 1`**: This restricts the output to only the first row, which, after sorting, will be the employee who received the biggest bonus.