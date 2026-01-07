To count the number of employees for each city, you can use the following SQL query:

```sql
SELECT count(*), city FROM employee GROUP BY city
```

### Explanation

This query performs the following actions:

*   **`SELECT count(*), city`**: This specifies that you want to retrieve two pieces of information:
    *   `count(*)`: The total number of rows (employees) in each group.
    *   `city`: The city name.
*   **`FROM employee`**: This indicates that the data should be retrieved from the `employee` table.
*   **`GROUP BY city`**: This clause groups the rows based on the `city` column. The `count(*)` function will then count the employees within each unique city group.