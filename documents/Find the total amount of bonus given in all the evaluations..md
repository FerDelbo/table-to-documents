To find the total amount of bonus given in all evaluations, you would typically query the `evaluation` table and sum the `bonus` column.

## SQL Query

```sql
SELECT SUM(bonus)
FROM evaluation;
```

### Explanation

*   `SELECT SUM(bonus)`: This part of the query calculates the sum of all values in the `bonus` column. The `SUM()` aggregate function is used to get the total amount.
*   `FROM evaluation`: This specifies that the data should be retrieved from the `evaluation` table.

This query will return a single value representing the total bonus amount from all entries in the `evaluation` table.