To find the name and capacity of the stadium with the highest average attendance, you would typically query a database using SQL.

```sql
SELECT name, capacity
FROM stadium
ORDER BY average DESC
LIMIT 1;
```

### Explanation of the SQL Query

*   **`SELECT name, capacity`**: This specifies that you want to retrieve two columns: `name` (the name of the stadium) and `capacity` (the capacity of the stadium).
*   **`FROM stadium`**: This indicates that the data should be retrieved from the table named `stadium`.
*   **`ORDER BY average DESC`**: This clause sorts the results based on the `average` column in descending order. This places the stadium with the highest average attendance at the top of the result set.
*   **`LIMIT 1`**: This clause restricts the output to only the first row after sorting, which corresponds to the stadium with the highest average attendance.

This query will return the name and capacity of the single stadium that has the highest recorded average attendance.