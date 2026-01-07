To find the flight numbers of flights departing from the city "Aberdeen", you would execute a SQL query that joins the `flights` table with the `airports` table and filters by the city name in the `airports` table.

```sql
SELECT
  T1.FlightNo
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.SourceAirport = T2.AirportCode
WHERE
  T2.City = 'Aberdeen';
```