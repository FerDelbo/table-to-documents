The number of flights departing from Aberdeen can be found by querying the `flights` and `airports` tables. You need to join these two tables on the `sourceairport` column from the `flights` table and the `airportcode` column from the `airports` table. Then, filter the results where the `city` in the `airports` table is 'Aberdeen' and count the total number of flights.

Here's the Markdown document providing the SQL query:

# Number of Flights Departing from Aberdeen

This document provides the SQL query to determine the total number of flights departing from the city of 'Aberdeen'.

## SQL Query

To count the number of flights departing from 'Aberdeen', you need to perform a join operation between the `flights` table (which contains flight information including source airports) and the `airports` table (which contains airport details including the city). The join will link flights to their corresponding source airports, and a `WHERE` clause will filter for airports located in 'Aberdeen'. Finally, the `COUNT(*)` aggregate function will give the total number of such flights.

```sql
SELECT
  COUNT(*)
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.SourceAirport = T2.AirportCode
WHERE
  T2.City = 'Aberdeen';
```

### Explanation of the Query:

*   **`SELECT COUNT(*)`**: This counts all rows that match the criteria, effectively giving the total number of flights.
*   **`FROM flights AS T1`**: Specifies that we are querying the `flights` table and aliasing it as `T1` for brevity.
*   **`INNER JOIN airports AS T2 ON T1.SourceAirport = T2.AirportCode`**: This joins the `flights` table (`T1`) with the `airports` table (`T2`). The join condition `T1.SourceAirport = T2.AirportCode` links each flight to its originating airport's details.
*   **`WHERE T2.City = 'Aberdeen'`**: This clause filters the joined results, ensuring that only flights departing from airports located in the city 'Aberdeen' are considered.