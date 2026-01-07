To determine the number of flights landing in Aberdeen or Abilene, we need to query the `flights` and `airports` tables.

### SQL Query

```sql
SELECT
  COUNT(*)
FROM flights AS t1
JOIN airports AS t2
  ON t1.destairport = t2.airportcode
WHERE
  t2.city = 'Aberdeen' OR t2.city = 'Abilene';
```

### Explanation

1.  **`SELECT COUNT(*)`**: This counts the total number of rows that satisfy the conditions specified in the `WHERE` clause. Each row represents a flight.
2.  **`FROM flights AS t1`**: We start by selecting from the `flights` table, aliasing it as `t1` for brevity. This table contains information about individual flights.
3.  **`JOIN airports AS t2 ON t1.destairport = t2.airportcode`**: We join the `flights` table (`t1`) with the `airports` table (`t2`). The join condition `t1.destairport = t2.airportcode` links flights to their destination airports. This is crucial because the city information (Aberdeen or Abilene) is stored in the `airports` table, not directly in the `flights` table.
4.  **`WHERE t2.city = 'Aberdeen' OR t2.city = 'Abilene'`**: This clause filters the results to include only those flights where the destination airport's city is either 'Aberdeen' or 'Abilene'. This directly addresses the question of "flights landing in Aberdeen or Abilene".