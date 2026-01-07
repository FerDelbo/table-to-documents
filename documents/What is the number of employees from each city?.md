To find the number of employees from each city, you can use the following SQL query:

```sql
SELECT count(*), city
FROM employee
GROUP BY city;
```

### Explanation

This query performs the following actions:

1.  **`SELECT count(*), city`**: It selects two columns:
    *   `count(*)`: This aggregate function counts the total number of rows (employees) for each group.
    *   `city`: This is the column that holds the city name for each employee.
2.  **`FROM employee`**: Specifies that the data should be retrieved from the `employee` table.
3.  **`GROUP BY city`**: This clause groups the rows that have the same `city` value. The `count(*)` function then operates on these groups, providing a count for each distinct city.

This will return a result set where each row represents a unique city and the total number of employees residing in that city.