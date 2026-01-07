This document provides the SQL query to determine the number of United Airlines flights departing from AHD Airport, formatted in Markdown.

## Counting United Airlines Flights from AHD Airport

To find the total number of flights operated by 'United Airlines' that depart from 'AHD Airport', you can use the following SQL query.

### SQL Query

```sql
SELECT
  COUNT(*)
FROM airlines AS T1
JOIN flights AS T2
  ON T2.airline = T1.uid
WHERE
  T1.airline = 'United Airlines' AND T2.sourceairport = 'AHD';
```

### Explanation

This query works by joining two tables, `airlines` and `flights`, and then applying specific filters to count the relevant records.

*   **`FROM airlines AS T1 JOIN flights AS T2 ON T2.airline = T1.uid`**:
    *   The `airlines` table (aliased as `T1`) contains information about different airlines, including their names and unique IDs (`uid`).
    *   The `flights` table (aliased as `T2`) contains details about individual flights, including the airline operating the flight (`airline`) and the departure airport (`sourceairport`).
    *   The `JOIN` clause links these two tables using `T2.airline = T1.uid` to match flights with their corresponding airline details.

*   **`WHERE T1.airline = 'United Airlines' AND T2.sourceairport = 'AHD'`**:
    *   This `WHERE` clause filters the joined data based on two conditions:
        *   `T1.airline = 'United Airlines'`: Ensures that only flights operated by 'United Airlines' are considered.
        *   `T2.sourceairport = 'AHD'`: Further narrows down the results to only include flights departing from 'AHD' airport.

*   **`SELECT COUNT(*)`**:
    *   Finally, `COUNT(*)` counts all the rows that satisfy the conditions specified in the `WHERE` clause. This gives the total number of United Airlines flights originating from AHD Airport.

### Expected Output

The query will return a single numerical value representing the count of flights that meet the specified criteria.