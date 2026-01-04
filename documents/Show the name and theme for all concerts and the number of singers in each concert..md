This document provides the SQL query and an explanation for retrieving the name, theme, and number of singers for all concerts.

## Query: Show the name and theme for all concerts and the number of singers in each concert.

To obtain the concert name, theme, and the count of singers participating in each concert, you can use the following SQL query.

### SQL Query

```sql
SELECT
  T2.concert_name,
  T2.theme,
  COUNT(*)
FROM singer_in_concert AS T1
JOIN concert AS T2
  ON T1.concert_id = T2.concert_id
GROUP BY
  T2.concert_id;
```

### Explanation

This query performs the following actions to produce the desired result:

1.  **`FROM singer_in_concert AS T1 JOIN concert AS T2 ON T1.concert_id = T2.concert_id`**: It starts by joining two tables:
    *   `singer_in_concert` (aliased as `T1`): This table links singers to the concerts they participate in via `concert_id` and `singer_id`.
    *   `concert` (aliased as `T2`): This table contains details about each concert, including `concert_name` and `theme`.
    The join condition `T1.concert_id = T2.concert_id` links records where a singer participated in a specific concert.

2.  **`GROUP BY T2.concert_id`**: The results are grouped by `concert_id` from the `concert` table. This ensures that the `COUNT(*)` function aggregates the number of singers for each unique concert.

3.  **`SELECT T2.concert_name, T2.theme, COUNT(*)`**: For each group (i.e., each unique concert), the query selects:
    *   `T2.concert_name`: The name of the concert.
    *   `T2.theme`: The theme of the concert.
    *   `COUNT(*)`: The total number of rows in the `singer_in_concert` table associated with that `concert_id`, effectively counting the number of singers (or singer participations) in that concert.