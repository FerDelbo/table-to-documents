To find the flight numbers of flights leaving from Aberdeen, you can use the following SQL query.

## Query to List Flight Numbers from Aberdeen

To retrieve the flight numbers for all flights departing from the city of 'Aberdeen', you need to join the `flights` table with the `airports` table on their respective airport codes and then filter by the city name.

### SQL Query

```sql
SELECT
  T1.flightno
FROM flights AS T1
JOIN airports AS T2
  ON T1.sourceairport = T2.airportcode
WHERE
  T2.city = 'Aberdeen';
```

### Explanation

*   **`SELECT T1.flightno`**: This specifies that you want to retrieve the `flightno` column from the `flights` table (aliased as `T1`).
*   **`FROM flights AS T1 JOIN airports AS T2 ON T1.sourceairport = T2.airportcode`**: This clause joins the `flights` table (`T1`) with the `airports` table (`T2`). The join condition `T1.sourceairport = T2.airportcode` links flights to their respective source airports.
*   **`WHERE T2.city = 'Aberdeen'`**: This filters the results to include only those flights where the city of the source airport (from the `airports` table, aliased as `T2`) is 'Aberdeen'.