To find the code of the airport with the least number of flights, you can use the following SQL query. This query identifies airports that appear in either the `sourceairport` or `destairport` columns of the `flights` table and then orders them by the total count of flights (both arriving and departing) in ascending order, limiting the result to the top one.

### SQL Query

```sql
SELECT
  T1.airportcode
FROM airports AS T1
JOIN flights AS T2
  ON T1.airportcode = T2.destairport
  OR T1.airportcode = T2.sourceairport
GROUP BY
  T1.airportcode
ORDER BY
  COUNT(*)
LIMIT 1;
```

### Explanation

1.  **`FROM airports AS T1 JOIN flights AS T2 ON T1.airportcode = T2.destairport OR T1.airportcode = T2.sourceairport`**:
    *   This part joins the `airports` table (aliased as `T1`) with the `flights` table (aliased as `T2`).
    *   The `ON` clause specifies that an airport is relevant if its `airportcode` matches either the `destairport` (destination airport) or `sourceairport` (source airport) in the `flights` table. This ensures that all flights associated with an airport, whether arriving or departing, are considered.

2.  **`GROUP BY T1.airportcode`**:
    *   This groups the results by `airportcode`, so that `COUNT(*)` calculates the total number of flights for each distinct airport.

3.  **`ORDER BY COUNT(*) LIMIT 1`**:
    *   `ORDER BY COUNT(*)` sorts the airports based on the total number of flights, in ascending order (from least flights to most flights).
    *   `LIMIT 1` restricts the output to only the first row, which corresponds to the airport with the absolute least number of flights.

This query effectively isolates the airport with the minimum number of associated flights.