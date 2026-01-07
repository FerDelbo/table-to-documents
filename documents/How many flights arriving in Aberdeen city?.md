To find the number of flights arriving in Aberdeen city, you would use the following SQL query:

```sql
SELECT count(*)
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.destairport = T2.airportcode
WHERE
  T2.city = 'Aberdeen';
```