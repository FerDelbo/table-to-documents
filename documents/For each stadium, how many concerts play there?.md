To determine the number of concerts held at each stadium, you can execute a SQL query that joins the `concert` and `stadium` tables and then groups the results by stadium.

## Query to Count Concerts per Stadium

This query will list each stadium's name along with the total count of concerts that have taken place there.

### SQL Query

```sql
SELECT
  T2.name AS StadiumName,
  COUNT(*) AS NumberOfConcerts
FROM concert AS T1
JOIN stadium AS T2
  ON T1.stadium_id = T2.stadium_id
GROUP BY
  T2.stadium_id;
```

### Explanation

1.  **`SELECT T2.name AS StadiumName, COUNT(*) AS NumberOfConcerts`**:
    *   `T2.name`: Selects the `name` column from the `stadium` table (aliased as `T2`). This will be the name of each stadium.
    *   `COUNT(*)`: Counts all rows for each group. In this context, it counts the number of concerts.
    *   `AS StadiumName`, `AS NumberOfConcerts`: These are aliases given to the selected columns to make the output more readable.

2.  **`FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id`**:
    *   `FROM concert AS T1`: Specifies the `concert` table as the primary table, aliased as `T1`.
    *   `JOIN stadium AS T2`: Joins the `concert` table with the `stadium` table, aliased as `T2`.
    *   `ON T1.stadium_id = T2.stadium_id`: This is the join condition. It links rows from `concert` to `stadium` where the `stadium_id` matches, ensuring that concerts are associated with their respective stadiums.

3.  **`GROUP BY T2.stadium_id`**:
    *   This clause groups the rows based on the `stadium_id` from the `stadium` table. `COUNT(*)` will then operate on each of these groups, counting all concerts associated with a unique `stadium_id`. Grouping by `T2.name` would also work if `stadium.name` is guaranteed to be unique for each `stadium_id`.

### Expected Output

The query will return a result set with two columns: `StadiumName` and `NumberOfConcerts`. Each row will represent a unique stadium that has hosted at least one concert, showing its name and the total count of concerts held there.

For example:

| StadiumName     | NumberOfConcerts |
| :-------------- | :--------------- |
| Wembley Stadium | 5                |
| Madison Square  | 3                |
| Staples Center  | 2                |
| ...             | ...              |