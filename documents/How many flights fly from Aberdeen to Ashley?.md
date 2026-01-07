To determine the number of flights from Aberdeen to Ashley, you would query a database that contains flight and airport information.

## SQL Query

The following SQL query can be used to count the flights:

```sql
SELECT
  COUNT(*)
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.destairport = T2.airportcode
INNER JOIN airports AS T3
  ON T1.sourceairport = T3.airportcode
WHERE
  T2.city = 'Ashley' AND T3.city = 'Aberdeen';
```

### Explanation

*   **`SELECT COUNT(*)`**: This counts all rows that match the criteria, effectively counting the number of flights.
*   **`FROM flights AS T1`**: Specifies that we are querying the `flights` table, aliased as `T1`.
*   **`INNER JOIN airports AS T2 ON T1.destairport = T2.airportcode`**: This joins the `flights` table with the `airports` table (aliased as `T2`) to get information about the destination airport. The join condition links `destairport` in the `flights` table to `airportcode` in the `airports` table.
*   **`INNER JOIN airports AS T3 ON T1.sourceairport = T3.airportcode`**: This second `INNER JOIN` connects the `flights` table with the `airports` table again (aliased as `T3`) to retrieve information about the source airport. The join condition links `sourceairport` in the `flights` table to `airportcode` in the `airports` table.
*   **`WHERE T2.city = 'Ashley' AND T3.city = 'Aberdeen'`**: This clause filters the results:
    *   `T2.city = 'Ashley'`: Ensures that the destination city is 'Ashley'.
    *   `T3.city = 'Aberdeen'`: Ensures that the source city is 'Aberdeen'.

## Tables Involved

The query involves three database tables:

1.  **`flights`**:
    *   Contains information about individual flights.
    *   Likely includes columns such as `flight_id`, `sourceairport`, and `destairport` (referencing airport codes).
2.  **`airports`**:
    *   Contains details about various airports.
    *   Likely includes columns such as `airportcode`, `airportname`, and `city`.

By joining these tables and applying the specified filters, the query accurately identifies and counts all flights originating from Aberdeen and arriving in Ashley.