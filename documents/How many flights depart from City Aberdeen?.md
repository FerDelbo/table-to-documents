To determine the number of flights departing from the city of Aberdeen, you can use a SQL query that joins the `flights` table with the `airports` table and filters by the city name.

### SQL Query

```sql
SELECT
  COUNT(*)
FROM flights AS T1
JOIN airports AS T2
  ON T1.sourceairport = T2.airportcode
WHERE
  T2.city = 'Aberdeen';
```

### Explanation

This SQL query performs the following actions:

1.  **`SELECT COUNT(*)`**: This counts the total number of rows that satisfy the specified conditions. Each row represents a flight.
2.  **`FROM flights AS T1 JOIN airports AS T2 ON T1.sourceairport = T2.airportcode`**: This joins the `flights` table (aliased as `T1`) with the `airports` table (aliased as `T2`). The join condition `T1.sourceairport = T2.airportcode` links flights to their respective source airports based on the airport code.
3.  **`WHERE T2.city = 'Aberdeen'`**: This clause filters the joined results to include only those flights where the `city` column in the `airports` table (representing the source airport's city) is 'Aberdeen'.

In essence, the query counts all flights where the departure airport is located in "Aberdeen".

### Tables Involved

*   **`flights`**: Contains information about individual flights, including `sourceairport` (the airport code from which the flight departs).
*   **`airports`**: Contains details about airports, including `airportcode` and `city`.