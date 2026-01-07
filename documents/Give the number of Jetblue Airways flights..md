To find the number of JetBlue Airways flights, you would typically join the `flights` table with the `airlines` table to filter by the airline's name and then count the results.

Here's the SQL query that would achieve this:

```sql
SELECT count(*)
FROM flights AS T1
INNER JOIN airlines AS T2
  ON T1.airline = T2.uid
WHERE
  T2.airline = 'JetBlue Airways';
```

### Explanation

1.  **`SELECT count(*)`**: This part of the query counts the total number of rows that satisfy the conditions. In this context, each row represents a flight.
2.  **`FROM flights AS T1`**: We start by selecting from the `flights` table, aliased as `T1` for brevity.
3.  **`INNER JOIN airlines AS T2 ON T1.airline = T2.uid`**: To link flights to their respective airlines, we perform an `INNER JOIN` with the `airlines` table (aliased as `T2`). The join condition `T1.airline = T2.uid` connects flights to airlines based on their unique identifiers.
4.  **`WHERE T2.airline = 'JetBlue Airways'`**: This clause filters the joined results, ensuring that we only count flights where the `airline` name in the `airlines` table is 'JetBlue Airways'.

This query will return a single number representing the total count of flights operated by JetBlue Airways.