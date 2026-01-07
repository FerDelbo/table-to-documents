To find the number of flights operated by 'JetBlue Airways', you would execute the following SQL query:

```sql
SELECT
  COUNT(*)
FROM flights AS T1
INNER JOIN airlines AS T2
  ON T1.airline = T2.uid
WHERE
  T2.airline = 'JetBlue Airways';
```

### Explanation

This query performs the following actions:

1.  **`SELECT COUNT(*)`**: This counts all rows that match the criteria, effectively giving the total number of flights.
2.  **`FROM flights AS T1`**: It starts by selecting from the `flights` table, aliased as `T1`.
3.  **`INNER JOIN airlines AS T2 ON T1.airline = T2.uid`**: It joins the `flights` table (`T1`) with the `airlines` table (`T2`). The join condition `T1.airline = T2.uid` links flights to their respective airline records using the airline's unique identifier.
4.  **`WHERE T2.airline = 'JetBlue Airways'`**: This clause filters the joined results to include only those flights where the `airline` name in the `airlines` table is 'JetBlue Airways'.

### Tables Involved

The query uses the following tables:

*   **`flights`**: Contains information about individual flights.
*   **`airlines`**: Contains details about various airlines, including their names and unique identifiers (`uid`).