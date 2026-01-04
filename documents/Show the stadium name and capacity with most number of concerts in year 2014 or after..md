To retrieve the stadium name and capacity of the stadium with the most concerts in the year 2014 or after, you can use the following SQL query:

```sql
SELECT
  T2.name,
  T2.capacity
FROM concert AS T1
JOIN stadium AS T2
  ON T1.stadium_id = T2.stadium_id
WHERE
  T1.year >= 2014
GROUP BY
  T2.stadium_id
ORDER BY
  COUNT(*) DESC
LIMIT 1;
```

### Explanation:

1.  **`SELECT T2.name, T2.capacity`**: This specifies that you want to retrieve the `name` and `capacity` columns from the `stadium` table (aliased as `T2`).
2.  **`FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id`**: This performs an `INNER JOIN` between the `concert` table (aliased as `T1`) and the `stadium` table (aliased as `T2`). The join condition `T1.stadium_id = T2.stadium_id` links concerts to their respective stadiums.
3.  **`WHERE T1.year >= 2014`**: This filters the results to include only concerts that took place in the year 2014 or any subsequent year.
4.  **`GROUP BY T2.stadium_id`**: This groups the rows by `stadium_id` (from the `stadium` table). This is necessary to count the number of concerts for each unique stadium.
5.  **`ORDER BY COUNT(*) DESC`**: After grouping, this orders the results in descending order based on the count of concerts for each stadium. The stadium with the most concerts will appear first.
6.  **`LIMIT 1`**: This clause restricts the output to only the top row, which corresponds to the stadium with the highest number of concerts in the specified period.