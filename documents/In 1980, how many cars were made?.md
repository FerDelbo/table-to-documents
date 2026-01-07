This document provides the SQL query to determine the number of cars manufactured in the year 1980.

## Query to Find the Number of Cars Made in 1980

To count the total number of cars produced in a specific year, such as 1980, you can query the `cars_data` table and filter by the `year` column.

### SQL Query

```sql
SELECT
  COUNT(*)
FROM cars_data
WHERE
  year = 1980;
```

### Explanation

*   `SELECT COUNT(*)`: This part of the query counts all rows that match the specified criteria.
*   `FROM cars_data`: This indicates that the query will retrieve data from the `cars_data` table.
*   `WHERE year = 1980`: This clause filters the results to include only those records where the `year` column is equal to 1980.

This query will return a single numerical value representing the total count of cars manufactured in 1980 according to the dataset.