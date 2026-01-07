```markdown
# Number of Cars with More Than 4 Cylinders

To determine the number of cars that have more than 4 cylinders, you would typically execute a SQL query that counts rows in the `cars_data` table, applying a filter on the `cylinders` column.

## SQL Query

The SQL query to achieve this is:

```sql
SELECT count(*) FROM cars_data WHERE cylinders > 4
```

### Explanation

*   `SELECT count(*)`: This part of the query counts the total number of rows that satisfy the specified condition. Each row represents a car in the `cars_data` table.
*   `FROM cars_data`: This indicates that the query is targeting the `cars_data` table.
*   `WHERE cylinders > 4`: This is the filtering condition. It ensures that only cars with a `cylinders` value strictly greater than 4 are included in the count.

This query will return a single numerical value representing the total count of cars that have more than 4 cylinders in the `cars_data` table.
```