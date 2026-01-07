```markdown
# Flight Numbers for Flights Arriving at Aberdeen

To retrieve the flight numbers for all flights arriving at the city of "Aberdeen", you can execute an SQL query that joins the `flights` table with the `airports` table. This allows filtering by the city name associated with the destination airport.

## SQL Query

```sql
SELECT
  T1.flightno
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.destairport = T2.airportcode
WHERE
  T2.city = 'Aberdeen';
```

### Explanation

*   **`SELECT T1.flightno`**: This specifies that the query should return the `flightno` (flight number) from the `flights` table (aliased as `T1`).
*   **`FROM flights AS T1`**: This indicates that the primary table for the query is `flights`, and it's given the alias `T1` for brevity.
*   **`INNER JOIN airports AS T2 ON T1.destairport = T2.airportcode`**: This performs an inner join between the `flights` table (`T1`) and the `airports` table (`T2`). The join condition `T1.destairport = T2.airportcode` links flights to their destination airports based on their respective airport codes.
*   **`WHERE T2.city = 'Aberdeen'`**: This clause filters the joined results to include only those records where the `city` column in the `airports` table (`T2`) is 'Aberdeen'. This ensures that only flights arriving at an airport in Aberdeen are considered.

This query will provide a list of all flight numbers corresponding to flights that have "Aberdeen" as their destination city.
```