This document provides the SQL query to retrieve the names of singers and the number of concerts each person has participated in, based on the provided database schema context.

## Singer Concert Counts

This section details how to query the database to find out how many concerts each singer has been involved in.

### SQL Query

To get the name of each singer and the total number of concerts they participated in, you can use the following SQL query:

```sql
SELECT
  T2.name,
  COUNT(*)
FROM singer_in_concert AS T1
JOIN singer AS T2
  ON T1.singer_id = T2.singer_id
GROUP BY
  T2.singer_id;
```

### Query Explanation

Let's break down the components of this SQL query:

*   **`SELECT T2.name, COUNT(*)`**:
    *   `T2.name`: This selects the `name` column from the `singer` table (aliased as `T2`). This will be the name of each singer.
    *   `COUNT(*)`: This aggregate function counts the total number of rows for each group. In this context, it will count the number of concerts associated with each singer.

*   **`FROM singer_in_concert AS T1 JOIN singer AS T2 ON T1.singer_id = T2.singer_id`**:
    *   `FROM singer_in_concert AS T1`: Specifies that we are starting our query from the `singer_in_concert` table, which links singers to concerts. It's aliased as `T1` for brevity.
    *   `JOIN singer AS T2 ON T1.singer_id = T2.singer_id`: Performs an `INNER JOIN` with the `singer` table (aliased as `T2`). The join condition `T1.singer_id = T2.singer_id` links rows from `singer_in_concert` to their corresponding singer in the `singer` table using their shared `singer_id`.

*   **`GROUP BY T2.singer_id`**:
    *   This clause groups the rows based on the `singer_id` from the `singer` table. This is crucial because `COUNT(*)` will then count all concert entries for each unique `singer_id`, effectively giving the total number of concerts per singer. Grouping by `T2.singer_id` implicitly groups by `T2.name` as `singer_id` is typically the primary key for the `singer` table, ensuring uniqueness for each singer's name.

### Result

Executing this query will return a list where each row contains a singer's name and the count of concerts they have performed in. For example:

| name      | COUNT(*) |
| :-------- | :------- |
| Singer A  | 5        |
| Singer B  | 3        |
| Singer C  | 1        |
| ...       | ...      |