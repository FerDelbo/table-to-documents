To find the names of the singers who performed in a concert in 2014, you would use a SQL query that joins the `singer_in_concert`, `singer`, and `concert` tables.

```markdown
# Singers Who Performed in Concerts in 2014

This document outlines the SQL query required to retrieve the names of singers who participated in concerts held in the year 2014.

## SQL Query

To identify the singers, we need to join information from three tables:
1.  `singer_in_concert`: This table links singers to concerts.
2.  `singer`: This table contains details about individual singers, including their names.
3.  `concert`: This table provides information about concerts, including the year they took place.

The query will select the `name` of the singer, joining these tables on their respective foreign keys, and then filter the results for concerts that occurred in the year 2014.

```sql
SELECT
  T2.name
FROM singer_in_concert AS T1
JOIN singer AS T2
  ON T1.singer_id = T2.singer_id
JOIN concert AS T3
  ON T1.concert_id = T3.concert_id
WHERE
  T3.year = 2014;
```

## Explanation

*   **`SELECT T2.name`**: This specifies that we want to retrieve the `name` column from the `singer` table (aliased as `T2`).
*   **`FROM singer_in_concert AS T1`**: We start by selecting from the `singer_in_concert` table, aliasing it as `T1` for brevity. This table acts as an intermediary, connecting singers to concerts.
*   **`JOIN singer AS T2 ON T1.singer_id = T2.singer_id`**: This performs an inner join with the `singer` table (aliased as `T2`). The join condition `T1.singer_id = T2.singer_id` links each entry in `singer_in_concert` to the corresponding singer's details in the `singer` table.
*   **`JOIN concert AS T3 ON T1.concert_id = T3.concert_id`**: Another inner join is performed with the `concert` table (aliased as `T3`). The condition `T1.concert_id = T3.concert_id` links `singer_in_concert` entries to the details of the specific concert.
*   **`WHERE T3.year = 2014`**: This clause filters the results, ensuring that only records related to concerts held in the year 2014 are included.

This query effectively retrieves the names of all singers who had a performance in any concert during the year 2014.
```