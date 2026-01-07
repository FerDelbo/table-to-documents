The following document provides the SQL query and an explanation to find the number of flights landing in the city of Aberdeen or Abilene.

```markdown
# Find the Number of Flights Landing in Aberdeen or Abilene

To determine the total number of flights that land in either the city of Aberdeen or the city of Abilene, we need to query the `flights` table and join it with the `airports` table to filter by city name.

## SQL Query

```sql
SELECT
  COUNT(*)
FROM flights AS T1
INNER JOIN airports AS T2
  ON T1.destairport = T2.airportcode
WHERE
  T2.city = 'Aberdeen' OR T2.city = 'Abilene';
```

## Explanation

1.  **`SELECT COUNT(*)`**: This counts all rows that match the criteria, effectively giving us the total number of flights.
2.  **`FROM flights AS T1`**: We start by selecting from the `flights` table, aliased as `T1`. This table contains information about individual flights, including their destination airports.
3.  **`INNER JOIN airports AS T2 ON T1.destairport = T2.airportcode`**: To link flight records to airport city information, we perform an `INNER JOIN` with the `airports` table (aliased as `T2`). The join condition connects `destairport` (destination airport code) from the `flights` table to `airportcode` in the `airports` table.
4.  **`WHERE T2.city = 'Aberdeen' OR T2.city = 'Abilene'`**: This is the filtering condition. It restricts the results to only include flights where the `city` of the destination airport (`T2.city`) is either 'Aberdeen' or 'Abilene'. The `OR` operator ensures that flights landing in either city are included in the count.

This query will return a single number representing the total count of flights that have Aberdeen or Abilene as their destination city.
```