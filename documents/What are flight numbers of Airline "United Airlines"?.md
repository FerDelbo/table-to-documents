To find the flight numbers associated with "United Airlines", you would query the database by joining the `flights` table with the `airlines` table and filtering for the airline name "United Airlines".

Here's the SQL query that answers your question:

```sql
SELECT
  T1.flightno
FROM flights AS T1
INNER JOIN airlines AS T2
  ON T2.uid = T1.airline
WHERE
  T2.airline = 'United Airlines';
```

### Explanation

*   **`SELECT T1.flightno`**: This specifies that you want to retrieve the `flightno` column from the `flights` table (aliased as `T1`).
*   **`FROM flights AS T1`**: This indicates that the primary table for the query is `flights`, and it's given the alias `T1` for brevity.
*   **`INNER JOIN airlines AS T2 ON T2.uid = T1.airline`**: This performs an inner join between the `flights` table (`T1`) and the `airlines` table (`T2`). The join condition `T2.uid = T1.airline` links flights to their respective airlines using their unique identifiers.
*   **`WHERE T2.airline = 'United Airlines'`**: This clause filters the results to include only those flights where the `airline` name in the `airlines` table (`T2`) is 'United Airlines'.