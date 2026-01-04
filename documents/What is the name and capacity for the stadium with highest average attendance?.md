To find the name and capacity of the stadium with the highest average attendance, you would typically query a database table containing stadium information, ordering the results by average attendance in descending order and limiting to the top result.

### SQL Query

```sql
SELECT name, capacity
FROM stadium
ORDER BY average DESC
LIMIT 1;
```

### Explanation

*   **`SELECT name, capacity`**: This specifies that you want to retrieve the `name` and `capacity` columns from the stadium table.
*   **`FROM stadium`**: This indicates that the data should be retrieved from the `stadium` table.
*   **`ORDER BY average DESC`**: This sorts the results based on the `average` column in descending order. This places the stadium with the highest average attendance at the top.
*   **`LIMIT 1`**: This clause restricts the output to only the first row after sorting, which corresponds to the stadium with the highest average attendance.

By executing this SQL query, you would obtain the name and capacity of the stadium that has the highest recorded average attendance.