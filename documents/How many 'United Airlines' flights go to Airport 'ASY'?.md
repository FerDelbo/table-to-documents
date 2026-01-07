To determine the number of 'United Airlines' flights that go to Airport 'ASY', you would typically perform a SQL query that joins the `flights` and `airlines` tables, filters by the airline name and the destination airport, and then counts the matching records.

## SQL Query

```sql
SELECT
  COUNT(*)
FROM airlines AS T1
INNER JOIN flights AS T2
  ON T2.airline = T1.uid
WHERE
  T1.airline = 'United Airlines' AND T2.destairport = 'ASY';
```

### Explanation

1.  **`SELECT COUNT(*)`**: This part of the query counts the total number of rows that satisfy the specified conditions. Each row here represents a flight.
2.  **`FROM airlines AS T1 INNER JOIN flights AS T2 ON T2.airline = T1.uid`**:
    *   We are joining two tables: `airlines` (aliased as `T1`) and `flights` (aliased as `T2`).
    *   The `INNER JOIN` ensures that only rows with matching `airline` (from `flights`) and `uid` (from `airlines`) are included in the result. This links flights to their respective airlines.
3.  **`WHERE T1.airline = 'United Airlines' AND T2.destairport = 'ASY'`**:
    *   **`T1.airline = 'United Airlines'`**: This condition filters the results to include only flights operated by 'United Airlines'.
    *   **`T2.destairport = 'ASY'`**: This condition further filters these flights to only those whose destination airport code is 'ASY'.

This query will return a single numerical value representing the count of 'United Airlines' flights arriving at 'ASY' airport.