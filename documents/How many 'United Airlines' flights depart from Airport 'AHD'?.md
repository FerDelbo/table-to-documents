To find the number of 'United Airlines' flights departing from Airport 'AHD', you can use the following SQL query:

```sql
SELECT
  COUNT(*)
FROM airlines AS t1
JOIN flights AS t2
  ON t2.airline = t1.uid
WHERE
  t1.airline = 'United Airlines' AND t2.sourceairport = 'AHD';
```