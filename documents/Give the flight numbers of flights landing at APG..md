This document provides the SQL query to retrieve the flight numbers of flights landing at APG.

## Flight Numbers of Flights Landing at APG

To find the flight numbers of all flights that have 'APG' as their destination airport, you can use the following SQL query.

### SQL Query

```sql
SELECT flightno
FROM flights
WHERE destairport = 'APG';
```

### Query Explanation

This query performs the following actions:
1.  **`SELECT flightno`**: It selects the `flightno` (flight number) column from the table.
2.  **`FROM flights`**: It specifies that the data should be retrieved from the `flights` table.
3.  **`WHERE destairport = 'APG'`**: It filters the results to include only those flights where the `destairport` (destination airport) column has the value 'APG'.

### Relevant Table

The primary table involved in this query is:

*   `flights`: This table contains information about individual flights, including their flight numbers and destination airports.