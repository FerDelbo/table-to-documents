To determine the number of concerts held in the years 2014 or 2015, you would query the `concert` table.

## Query for Number of Concerts in 2014 or 2015

This section provides the SQL query to count the total number of concerts that occurred in either 2014 or 2015.

### SQL Query

```sql
SELECT count(*)
FROM concert
WHERE year = 2014 OR year = 2015;
```

### Explanation

*   `SELECT count(*)`: This clause is used to count the total number of rows (concerts) that satisfy the specified conditions.
*   `FROM concert`: This indicates that the query is retrieving data from the `concert` table.
*   `WHERE year = 2014 OR year = 2015`: This is the filtering condition. It selects only those records where the `year` column is either 2014 or 2015.

This query will return a single numerical value representing the total count of concerts that took place in either of the specified years.