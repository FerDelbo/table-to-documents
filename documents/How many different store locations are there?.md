To determine the number of different store locations, you can query the `shop` table and count the distinct values in the `location` column.

## SQL Query

```sql
SELECT count(DISTINCT location)
FROM shop;
```

## Explanation

*   `SELECT count(DISTINCT location)`: This clause counts the unique values in the `location` column. The `DISTINCT` keyword ensures that each unique location is counted only once, even if multiple shops exist in the same location.
*   `FROM shop`: This specifies that the query should be executed against the `shop` table.