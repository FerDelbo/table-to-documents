To find the average weight for each type of pet, you can use the following SQL query:

```sql
SELECT avg(weight), pettype FROM pets GROUP BY pettype
```

### Explanation

This query performs the following actions:

1.  **`SELECT avg(weight), pettype`**: It selects the average `weight` and the `pettype` from the `pets` table.
2.  **`FROM pets`**: Specifies that the data should be retrieved from the `pets` table.
3.  **`GROUP BY pettype`**: Groups the results by `pettype`, so the `avg(weight)` function calculates the average weight for each distinct pet type.