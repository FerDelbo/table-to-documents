To find the average weight for each pet type, you can use the following SQL query:

```sql
SELECT avg(weight), pettype FROM pets GROUP BY pettype
```

### Explanation

This query performs the following actions:

*   **`SELECT avg(weight), pettype`**: This specifies that you want to retrieve two pieces of information:
    *   The average of the `weight` column.
    *   The `pettype` itself.
*   **`FROM pets`**: This indicates that the data should be retrieved from the `pets` table.
*   **`GROUP BY pettype`**: This clause groups the rows that have the same `pettype` together. The `avg(weight)` function is then applied to each of these groups, calculating the average weight for each distinct pet type.