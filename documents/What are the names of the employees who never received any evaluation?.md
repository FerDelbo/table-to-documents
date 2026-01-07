To find the names of employees who have never received any evaluation, you can query the `employee` table and exclude those employee IDs that appear in the `evaluation` table.

```sql
SELECT
  name
FROM employee
WHERE
  employee_id NOT IN (
    SELECT
      employee_id
    FROM evaluation
  );
```

### Explanation

This SQL query works as follows:

1.  **`SELECT name FROM employee`**: This part specifies that we want to retrieve the `name` column from the `employee` table.
2.  **`WHERE employee_id NOT IN (...)`**: This clause filters the results. It includes only those employees whose `employee_id` is *not* found in the subquery.
3.  **`SELECT employee_id FROM evaluation`**: This subquery retrieves all `employee_id` values from the `evaluation` table. These are the IDs of employees who *have* received at least one evaluation.

By combining these, the query effectively returns the names of all employees who do not have any corresponding entries in the `evaluation` table, meaning they have never received an evaluation.