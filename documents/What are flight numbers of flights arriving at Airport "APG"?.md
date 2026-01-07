To retrieve the flight numbers of flights arriving at Airport "APG", you can use the following SQL query:

```sql
SELECT flightno FROM flights WHERE destairport = 'APG'
```

### Explanation

This query selects the `flightno` (flight number) from the `flights` table. The `WHERE` clause filters the results to include only those flights where the `destairport` (destination airport) matches 'APG'.