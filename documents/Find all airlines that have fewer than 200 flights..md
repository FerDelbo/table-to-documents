To find all airlines that have fewer than 200 flights, you would query the database to count the number of flights for each airline and then filter for those with a count less than 200.

```sql
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
GROUP BY
  T1.airline
HAVING
  COUNT(*) < 200;
```

### Explanation:

1.  **`SELECT T1.airline`**: This specifies that the query should return the `airline` name from the `airlines` table.
2.  **`FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.airline`**: This joins the `airlines` table (aliased as `T1`) with the `flights` table (aliased as `T2`). The join condition `T1.uid = T2.airline` links flights to their respective airlines using the unique identifier (`uid` in `airlines` and `airline` in `flights`).
3.  **`GROUP BY T1.airline`**: This groups the results by each unique airline name. This is necessary to count the total flights per airline.
4.  **`HAVING COUNT(*) < 200`**: After grouping, this filters the grouped results. It includes only those airlines where the total count of their flights (`COUNT(*)`) is less than 200. `HAVING` is used to filter aggregate results, similar to how `WHERE` filters individual rows.

This query will provide a list of airline names that operate fewer than 200 flights.