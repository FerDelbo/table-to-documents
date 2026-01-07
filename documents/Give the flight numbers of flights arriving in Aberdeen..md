To retrieve the flight numbers of flights arriving in Aberdeen, you can use the following SQL query:

```sql
SELECT T1.flightno
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.destairport = T2.airportcode
WHERE
  T2.city = 'Aberdeen';
```

### Explanation:

This query works by joining two tables, `flights` and `airports`, to link flight information with airport location details.

1.  **`SELECT T1.flightno`**: This specifies that we want to retrieve the `flightno` (flight number) from the `flights` table.
2.  **`FROM flights AS T1 JOIN airports AS T2 ON T1.destairport = T2.airportcode`**:
    *   We start by selecting from the `flights` table, aliased as `T1`.
    *   We then perform an `INNER JOIN` with the `airports` table, aliased as `T2`.
    *   The join condition `T1.destairport = T2.airportcode` links flights to their destination airport's details using the `destairport` column in `flights` and the `airportcode` in `airports`.
3.  **`WHERE T2.city = 'Aberdeen'`**: This clause filters the results to include only those flights where the `city` of the destination airport (from the `airports` table, `T2`) is 'Aberdeen'.

The result will be a list of flight numbers corresponding to all flights that have 'Aberdeen' as their destination city.