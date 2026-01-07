To find the number of cars with over 6 cylinders, you can use the following SQL query:

```sql
SELECT count(*) FROM cars_data WHERE cylinders > 6
```

### Explanation

This query operates on the `cars_data` table and performs the following actions:

1.  **`SELECT count(*)`**: This counts all rows that satisfy the condition specified in the `WHERE` clause.
2.  **`FROM cars_data`**: This indicates that the data is being retrieved from the `cars_data` table.
3.  **`WHERE cylinders > 6`**: This is the filtering condition. It specifies that only cars with a `cylinders` value greater than 6 should be included in the count.

This query will return a single numerical value representing the total count of cars that have more than 6 cylinders.