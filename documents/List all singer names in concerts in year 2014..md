This document provides the SQL query to list the names of all singers who performed in concerts during the year 2014, based on the provided database schema and example questions.

## List all singer names in concerts in year 2014

To retrieve the names of all singers who participated in concerts held in the year 2014, you need to join information from the `singer` table (for singer names), the `concert` table (for concert year), and the `singer_in_concert` table (to link singers to concerts).

### SQL Query

```sql
SELECT T2.name
FROM singer_in_concert AS T1
JOIN singer AS T2
  ON T1.singer_id = T2.singer_id
JOIN concert AS T3
  ON T1.concert_id = T3.concert_id
WHERE
  T3.year = 2014;
```

### Explanation

1.  **`SELECT T2.name`**: This specifies that the query should return the `name` column from the `singer` table. We use `T2.name` because `singer` is aliased as `T2`.
2.  **`FROM singer_in_concert AS T1`**: The query starts by selecting from the `singer_in_concert` table, which links singers to concerts. It's aliased as `T1` for brevity.
3.  **`JOIN singer AS T2 ON T1.singer_id = T2.singer_id`**: This joins `singer_in_concert` (T1) with the `singer` table (aliased as `T2`) using the `singer_id` column. This step is necessary to get the actual names of the singers.
4.  **`JOIN concert AS T3 ON T1.concert_id = T3.concert_id`**: This further joins the result with the `concert` table (aliased as `T3`) using the `concert_id` column. This join brings in the `year` information of the concerts.
5.  **`WHERE T3.year = 2014`**: This clause filters the results, ensuring that only concerts that took place in the year `2014` are considered.

### How to use the query

You can execute this SQL query against your database to get a list of all singer names that performed in concerts during 2014. The result will be a list of names, potentially with duplicates if a singer performed in multiple concerts in 2014. If you need a list of unique singer names, you can add the `DISTINCT` keyword after `SELECT`.