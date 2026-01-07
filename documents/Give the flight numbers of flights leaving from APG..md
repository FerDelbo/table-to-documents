To retrieve the flight numbers of flights departing from the airport with the code 'APG', you would query the `flights` table, filtering by the `sourceairport` column.

## Querying Flight Numbers from a Specific Departure Airport

This document outlines the SQL query required to find all flight numbers for flights originating from a particular airport, identified by its airport code.

### SQL Query

To get the flight numbers of flights departing from 'APG' airport, use the following SQL statement:

```sql
SELECT flightno
FROM flights
WHERE sourceairport = 'APG';
```

### Explanation

*   **`SELECT flightno`**: This specifies that you want to retrieve the values from the `flightno` column, which contains the unique identification numbers for each flight.
*   **`FROM flights`**: This indicates that the data should be retrieved from the `flights` table.
*   **`WHERE sourceairport = 'APG'`**: This is the filtering condition. It ensures that only rows where the `sourceairport` column matches the airport code 'APG' are included in the result set. This effectively filters for flights that depart from 'APG'.