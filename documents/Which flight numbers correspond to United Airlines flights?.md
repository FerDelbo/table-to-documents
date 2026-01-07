To retrieve the flight numbers corresponding to United Airlines flights, you can use a SQL query that joins the `flights` table with the `airlines` table and filters the results by the airline name.

## SQL Query

Here is the SQL query to find the flight numbers for United Airlines:

```sql
SELECT T1.flightno
FROM flights AS T1
JOIN airlines AS T2
  ON T2.uid = T1.airline
WHERE T2.airline = 'United Airlines';
```

## Query Explanation

*   **`SELECT T1.flightno`**: This specifies that the query should return the `flightno` column from the `flights` table (aliased as `T1`).
*   **`FROM flights AS T1`**: This indicates that we are querying the `flights` table and assigning it the alias `T1` for brevity.
*   **`JOIN airlines AS T2 ON T2.uid = T1.airline`**: This performs an INNER JOIN between the `flights` table (T1) and the `airlines` table (T2). The join condition `T2.uid = T1.airline` links flights to their respective airlines using the unique identifier (`uid`) from the `airlines` table and the `airline` foreign key in the `flights` table.
*   **`WHERE T2.airline = 'United Airlines'`**: This clause filters the joined results to include only those records where the `airline` name in the `airlines` table (T2) is 'United Airlines'.

This query effectively identifies all flights associated with "United Airlines" and returns their flight numbers.