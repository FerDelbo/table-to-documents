To find the airlines that have flights arriving at airport 'AHD', you can use the following SQL query:

```sql
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.destairport = 'AHD';
```

### Explanation:

This query retrieves the names of airlines (`T1.airline`) by joining the `airlines` table (aliased as `T1`) with the `flights` table (aliased as `T2`).

1.  **`FROM airlines AS T1`**: Starts by selecting from the `airlines` table, giving it a shorthand `T1`.
2.  **`JOIN flights AS T2 ON T1.uid = T2.airline`**: Connects `airlines` and `flights` tables. It links an airline's unique ID (`T1.uid`) from the `airlines` table to the `airline` column in the `flights` table (`T2.airline`), assuming `T2.airline` stores the `uid` of the operating airline.
3.  **`WHERE T2.destairport = 'AHD'`**: Filters the results to include only those flights where the destination airport (`T2.destairport`) is 'AHD'.
4.  **`SELECT T1.airline`**: Finally, it selects the name of the airline (`airline` column from `T1`) for all matching flights.

This query will return a list of airline names that operate flights arriving at the airport with the code 'AHD'.