To determine the number of United Airlines flights destined for the city of Aberdeen, you would execute an SQL query that joins the `flights`, `airports`, and `airlines` tables. This query filters flights by the airline name "United Airlines" and the destination city "Aberdeen", then counts the resulting flights.

```markdown
# Counting United Airlines Flights to Aberdeen

This document outlines the SQL query required to find the total number of flights operated by "United Airlines" that arrive at "Aberdeen" city.

## SQL Query

The following SQL query achieves this by joining the `flights`, `airports`, and `airlines` tables, and applying `WHERE` clauses to filter by airline name and destination city.

```sql
SELECT
  COUNT(*)
FROM flights AS T1
JOIN airports AS T2
  ON T1.destairport = T2.airportcode
JOIN airlines AS T3
  ON T3.uid = T1.airline
WHERE
  T2.city = 'Aberdeen' AND T3.airline = 'United Airlines';
```

## Query Explanation

*   **`SELECT COUNT(*)`**: This part of the query counts the total number of rows that match the specified criteria, effectively counting the flights.
*   **`FROM flights AS T1`**: Specifies that we are querying the `flights` table, aliased as `T1` for brevity.
*   **`JOIN airports AS T2 ON T1.destairport = T2.airportcode`**: This joins the `flights` table (`T1`) with the `airports` table (`T2`). The join condition `T1.destairport = T2.airportcode` links flights to their destination airport information using the airport code.
*   **`JOIN airlines AS T3 ON T3.uid = T1.airline`**: This joins the `flights` table (`T1`) with the `airlines` table (`T3`). The join condition `T3.uid = T1.airline` links flights to their operating airline using the airline's unique identifier.
*   **`WHERE T2.city = 'Aberdeen'`**: This condition filters the results to include only those flights where the destination airport's city (from the `airports` table) is 'Aberdeen'.
*   **`AND T3.airline = 'United Airlines'`**: This condition further narrows down the results to include only flights operated by the airline named 'United Airlines' (from the `airlines` table).

## Tables Involved

*   `flights`: Contains information about individual flights, including `destairport` (destination airport code) and `airline` (airline unique ID).
*   `airports`: Contains details about airports, including `airportcode` and `city`.
*   `airlines`: Contains details about airlines, including `uid` (unique ID) and `airline` (airline name).

This structured query ensures that only flights matching both the specific airline and destination city are counted, providing an accurate answer to the question.
```