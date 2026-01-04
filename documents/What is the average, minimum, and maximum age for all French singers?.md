To find the average, minimum, and maximum age for all French singers, you would use an SQL query that leverages aggregate functions (`AVG`, `MIN`, `MAX`) on the `age` column, filtered by the `country` column in the `singer` table.

## SQL Query

```sql
SELECT
  AVG(age),
  MIN(age),
  MAX(age)
FROM singer
WHERE
  country = 'France';
```

## Explanation

1.  **`SELECT AVG(age), MIN(age), MAX(age)`**: This part of the query specifies the data you want to retrieve.
    *   `AVG(age)`: Calculates the arithmetic mean (average) of all ages.
    *   `MIN(age)`: Finds the lowest age among the selected records.
    *   `MAX(age)`: Finds the highest age among the selected records.
    *   These are aggregate functions that operate on a set of rows and return a single summary row.

2.  **`FROM singer`**: This indicates that the data will be retrieved from the `singer` table.

3.  **`WHERE country = 'France'`**: This is the filtering condition. It ensures that only rows where the `country` column has the value 'France' are considered for the aggregation. This effectively narrows down the calculation to only French singers.

This query will return a single row containing three values: the average age, the minimum age, and the maximum age of all singers whose country is listed as 'France'.