To find the number of cars that have over 6 cylinders, you can use a SQL query to count the entries in the `cars_data` table where the `cylinders` column has a value greater than 6.

## SQL Query

```sql
SELECT count(*)
FROM cars_data
WHERE cylinders > 6;
```

### Explanation

*   `SELECT count(*)`: This part of the query counts all rows that satisfy the specified conditions.
*   `FROM cars_data`: This indicates that the query will operate on the `cars_data` table.
*   `WHERE cylinders > 6`: This is the filtering condition. It ensures that only cars with a `cylinders` value strictly greater than 6 are included in the count.