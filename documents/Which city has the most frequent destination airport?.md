To determine which city has the most frequent destination airport, you would query the database to count the number of flights arriving at airports in each city and then identify the city with the highest count.

Here's the SQL query to achieve this:

```sql
SELECT
  T1.city
FROM airports AS T1
INNER JOIN flights AS T2
  ON T1.airportcode = T2.destairport
GROUP BY
  T1.city
ORDER BY
  COUNT(*) DESC
LIMIT 1;
```

### Explanation:

1.  **`SELECT T1.city`**: This specifies that the output should include the name of the city.
2.  **`FROM airports AS T1 JOIN flights AS T2 ON T1.airportcode = T2.destairport`**: This performs an `INNER JOIN` between the `airports` table (aliased as `T1`) and the `flights` table (aliased as `T2`). The join condition links an airport in the `airports` table to its corresponding destination airport in the `flights` table using `airportcode` and `destairport`.
3.  **`GROUP BY T1.city`**: This groups the results by city, so that the `COUNT(*)` function can tally flights for each distinct city.
4.  **`ORDER BY COUNT(*) DESC`**: This sorts the grouped cities in descending order based on the total number of arriving flights (the count of records within each city group).
5.  **`LIMIT 1`**: This restricts the output to only the top entry, which will be the city with the most frequent destination airport.