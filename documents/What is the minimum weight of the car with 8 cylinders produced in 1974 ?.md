```markdown
# Minimum Weight of Cars with 8 Cylinders Produced in 1974

This document provides the SQL query to determine the minimum weight of cars that have 8 cylinders and were produced in the year 1974.

## SQL Query

To retrieve the minimum weight, you would query the `cars_data` table, filtering for `cylinders` equal to 8 and `year` equal to 1974, and then apply the `MIN()` aggregate function to the `weight` column.

```sql
SELECT MIN(weight)
FROM cars_data
WHERE cylinders = 8 AND year = 1974;
```

## Explanation

*   **`SELECT MIN(weight)`**: This clause selects the minimum value from the `weight` column.
*   **`FROM cars_data`**: This specifies that the query will be executed against the `cars_data` table.
*   **`WHERE cylinders = 8 AND year = 1974`**: This `WHERE` clause filters the rows to include only those cars that meet both conditions: having 8 cylinders and being produced in the year 1974.

This query will return a single value representing the lowest recorded weight among all cars that satisfy the specified criteria.
```