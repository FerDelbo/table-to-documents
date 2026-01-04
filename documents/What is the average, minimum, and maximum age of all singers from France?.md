This document provides the SQL query to determine the average, minimum, and maximum age of all singers from France.

## Query for Singer Age Statistics by Country

To find the average, minimum, and maximum age of singers from a specific country, such as France, you would query the `singer` table, filtering by the `country` column.

### SQL Query

```sql
SELECT avg(age), min(age), max(age)
FROM singer
WHERE country = 'France';
```

### Explanation

*   **`SELECT avg(age), min(age), max(age)`**: This part of the query specifies the aggregate functions to be calculated:
    *   `avg(age)`: Calculates the average age of the singers.
    *   `min(age)`: Finds the minimum age among the singers.
    *   `max(age)`: Determines the maximum age among the singers.
*   **`FROM singer`**: This indicates that the data will be retrieved from the `singer` table.
*   **`WHERE country = 'France'`**: This clause filters the results to include only those singers whose `country` is 'France'.

This query will return a single row with three columns: the average age, the minimum age, and the maximum age for all singers identified as being from France in the `singer` table.