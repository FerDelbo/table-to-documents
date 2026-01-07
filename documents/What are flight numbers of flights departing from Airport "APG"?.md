```markdown
# Flight Numbers of Flights Departing from Airport "APG"

To retrieve the flight numbers of all flights departing from a specific airport, such as "APG", you would query the `flights` table and filter by the `sourceairport` column.

## SQL Query

The SQL query to achieve this is as follows:

```sql
SELECT flightno
FROM flights
WHERE sourceairport = 'APG';
```

## Explanation

*   **`SELECT flightno`**: This specifies that the query should return the `flightno` column, which contains the flight numbers.
*   **`FROM flights`**: This indicates that the data should be retrieved from the `flights` table.
*   **`WHERE sourceairport = 'APG'`**: This is the filtering condition. It ensures that only rows where the `sourceairport` column matches the airport code 'APG' are included in the result set.

This query will provide a list of all flight numbers for departures originating from "APG" airport.
```