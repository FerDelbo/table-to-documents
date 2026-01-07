To determine the number of flights with the destination 'ATO', you can use the following SQL query:

```sql
SELECT count(*) FROM flights WHERE destairport = 'ATO';
```

### Explanation

This query performs the following actions:

1.  **`SELECT count(*)`**: This counts the total number of rows in the `flights` table.
2.  **`FROM flights`**: Specifies that the data is being retrieved from the `flights` table.
3.  **`WHERE destairport = 'ATO'`**: This clause filters the results, ensuring that only flights where the `destairport` (destination airport) column matches the value 'ATO' are included in the count.