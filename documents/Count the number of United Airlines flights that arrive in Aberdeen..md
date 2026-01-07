The following document provides the SQL query to count the number of United Airlines flights arriving in Aberdeen, along with an explanation of its components.

# Counting United Airlines Flights Arriving in Aberdeen

To determine the number of flights operated by "United Airlines" that have "Aberdeen" as their destination city, you can use a SQL query that joins the `flights`, `airports`, and `airlines` tables.

## SQL Query

```sql
SELECT
  COUNT(*)
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.destairport = T2.airportcode
INNER JOIN airlines AS T3
  ON T3.uid = T1.airline
WHERE
  T2.city = 'Aberdeen' AND T3.airline = 'United Airlines';
```

## Query Explanation

This query performs the following actions to achieve the desired result:

*   **`SELECT COUNT(*)`**: This counts all rows that match the specified criteria, effectively giving the total number of flights.
*   **`FROM flights AS T1`**: It starts by selecting from the `flights` table, aliased as `T1`. This table presumably contains individual flight records, including source and destination airports and the operating airline.
*   **`INNER JOIN airports AS T2 ON T1.destairport = T2.airportcode`**:
    *   An `INNER JOIN` is used to connect `flights` (T1) with the `airports` table (aliased as `T2`).
    *   The join condition `T1.destairport = T2.airportcode` links flights to their destination airport details using the airport code.
*   **`INNER JOIN airlines AS T3 ON T3.uid = T1.airline`**:
    *   Another `INNER JOIN` connects `flights` (T1) with the `airlines` table (aliased as `T3`).
    *   The join condition `T3.uid = T1.airline` links flights to their operating airline using the airline's unique identifier.
*   **`WHERE T2.city = 'Aberdeen' AND T3.airline = 'United Airlines'`**: This clause filters the joined results:
    *   `T2.city = 'Aberdeen'`: Ensures that only flights arriving at an airport located in "Aberdeen" are considered.
    *   `T3.airline = 'United Airlines'`: Further filters the results to include only those flights operated by "United Airlines".

By combining these operations, the query precisely identifies and counts all flights that fit both criteria: being a "United Airlines" flight and arriving in "Aberdeen".