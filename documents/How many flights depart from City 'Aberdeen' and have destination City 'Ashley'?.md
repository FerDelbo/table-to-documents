To determine the number of flights departing from 'Aberdeen' and arriving in 'Ashley', you can use a SQL query that joins the `flights` table with the `airports` table twice (once for the source airport and once for the destination airport) and filters by the specified city names.

```markdown
# Counting Flights Between Specific Cities

This document provides the SQL query to find the total number of flights that originate from 'Aberdeen' and have 'Ashley' as their destination.

## SQL Query

To retrieve the count of flights departing from 'Aberdeen' and arriving in 'Ashley', execute the following SQL query:

```sql
SELECT
  COUNT(*)
FROM flights AS T1
JOIN airports AS T2
  ON T1.destairport = T2.airportcode
JOIN airports AS T3
  ON T1.sourceairport = T3.airportcode
WHERE
  T2.city = 'Ashley' AND T3.city = 'Aberdeen';
```

## Query Explanation

*   **`SELECT COUNT(*)`**: This clause counts all rows that satisfy the conditions defined in the `WHERE` clause, effectively giving us the total number of flights.
*   **`FROM flights AS T1`**: We start by selecting from the `flights` table, aliased as `T1`. This table presumably contains information about individual flights, including source and destination airports.
*   **`JOIN airports AS T2 ON T1.destairport = T2.airportcode`**: This joins the `flights` table (`T1`) with the `airports` table, aliased as `T2`. This join links flights to their destination airport details using the `destairport` and `airportcode` columns.
*   **`JOIN airports AS T3 ON T1.sourceairport = T3.airportcode`**: Similarly, this second join connects the `flights` table (`T1`) to another instance of the `airports` table, aliased as `T3`. This join is used to get details about the flight's *source* airport using `sourceairport` and `airportcode`.
*   **`WHERE T2.city = 'Ashley' AND T3.city = 'Aberdeen'`**: This is the filtering condition.
    *   `T2.city = 'Ashley'`: Ensures that the destination city (from the `T2` alias of the `airports` table) is 'Ashley'.
    *   `T3.city = 'Aberdeen'`: Ensures that the source city (from the `T3` alias of the `airports` table) is 'Aberdeen'.

## Expected Output

The query will return a single numerical value representing the total count of flights that match the specified criteria (departing from 'Aberdeen' and arriving in 'Ashley').

| COUNT(*) |
| :------- |
| N        |

Where 'N' is the total number of such flights found in the database.
```