To identify countries where there are both singers above 40 years old and singers below 30 years old, you can use a SQL query involving the `INTERSECT` operator. This operation combines the results of two `SELECT` statements, returning only the distinct rows that are output by both queries.

### SQL Query

```sql
SELECT country
FROM singer
WHERE age > 40
INTERSECT
SELECT country
FROM singer
WHERE age < 30;
```

### Explanation

1.  **First `SELECT` Statement (`SELECT country FROM singer WHERE age > 40`)**:
    *   This part of the query selects the `country` from the `singer` table.
    *   The `WHERE age > 40` clause filters these results to include only singers whose age is strictly greater than 40. This gives us a list of countries where there is at least one singer above 40.

2.  **Second `SELECT` Statement (`SELECT country FROM singer WHERE age < 30`)**:
    *   Similarly, this part selects the `country` from the `singer` table.
    *   The `WHERE age < 30` clause filters these results to include only singers whose age is strictly less than 30. This provides a list of countries where there is at least one singer below 30.

3.  **`INTERSECT` Operator**:
    *   The `INTERSECT` operator then takes the unique countries from the result set of the first query and compares them with the unique countries from the result set of the second query.
    *   It returns only those countries that appear in *both* result sets. This effectively identifies countries that have at least one singer over 40 AND at least one singer under 30.

### Interpreting the Results

The output of this query will be a list of distinct country names. Each country in this list will satisfy the condition of having at least one singer older than 40 and at least one singer younger than 30. If a country does not have both types of singers, it will not appear in the final result.