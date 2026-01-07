To find the number of flights arriving in Aberdeen, you would typically join the `flights` table with the `airports` table on the destination airport code and then filter by the city name 'Aberdeen' and count the results.

Here's the SQL query that accomplishes this:

```sql
SELECT
  COUNT(*)
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.destairport = T2.airportcode
WHERE
  T2.city = 'Aberdeen';
```

### Explanation:

1.  **`SELECT COUNT(*)`**: This counts all the rows that match the criteria, effectively giving the total number of flights.
2.  **`FROM flights AS T1`**: Specifies that we are querying the `flights` table and aliasing it as `T1` for brevity.
3.  **`INNER JOIN airports AS T2 ON T1.destairport = T2.airportcode`**: This joins the `flights` table (`T1`) with the `airports` table (`T2`). The join condition `T1.destairport = T2.airportcode` links flights to their respective destination airports using their airport codes.
4.  **`WHERE T2.city = 'Aberdeen'`**: This clause filters the joined results to include only those flights where the destination airport's city is 'Aberdeen'.