To retrieve the names of employees sorted by their age in ascending order, you can use the following SQL query:

```sql
SELECT name FROM employee ORDER BY age ASC;
```

### Explanation

*   **`SELECT name`**: This specifies that you want to retrieve the `name` column from the `employee` table.
*   **`FROM employee`**: This indicates that the data should be fetched from the `employee` table.
*   **`ORDER BY age ASC`**: This clause sorts the results based on the `age` column. `ASC` (ascending) ensures that the names are listed from the youngest employee to the oldest. If `ASC` is omitted, the default behavior is usually ascending order, but explicitly stating it makes the query clearer.