This document provides a detailed answer to the question "What is the name and capacity of the stadium with the most concerts after 2013?".

## Querying for Stadium with Most Concerts After 2013

To find the name and capacity of the stadium that hosted the most concerts after the year 2013, you would typically join information from a `concert` table (to check the year and count concerts) and a `stadium` table (to retrieve the stadium's name and capacity).

### SQL Query

The SQL query to achieve this result involves:
1.  **Joining** the `concert` table with the `stadium` table on their common `stadium_id`.
2.  **Filtering** the concerts to only include those that occurred after the year 2013.
3.  **Grouping** the results by `stadium_id` to count concerts per stadium.
4.  **Ordering** the grouped results in descending order of the concert count.
5.  **Limiting** the result to `1` to get only the stadium with the highest number of concerts.
6.  **Selecting** the stadium's name and capacity.

```sql
SELECT
  T2.name,
  T2.capacity
FROM
  concert AS T1
JOIN
  stadium AS T2
  ON T1.stadium_id = T2.stadium_id
WHERE
  T1.year > 2013
GROUP BY
  T2.stadium_id
ORDER BY
  COUNT(*) DESC
LIMIT 1;
```

### Explanation

*   **`SELECT T2.name, T2.capacity`**: This specifies that the output should include the `name` and `capacity` columns from the `stadium` table (aliased as `T2`).
*   **`FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id`**: This performs an inner join between the `concert` table (aliased as `T1`) and the `stadium` table (aliased as `T2`). The join condition `T1.stadium_id = T2.stadium_id` links concerts to their respective stadiums.
*   **`WHERE T1.year > 2013`**: This clause filters the `concert` records, ensuring that only concerts that took place after the year 2013 are considered.
*   **`GROUP BY T2.stadium_id`**: This groups the rows by each unique `stadium_id` from the `stadium` table. This is essential for counting the number of concerts per stadium.
*   **`ORDER BY COUNT(*) DESC`**: After grouping, this orders the stadiums based on the count of concerts (`COUNT(*)`) in descending order, placing the stadium with the most concerts at the top.
*   **`LIMIT 1`**: This restricts the output to only the first row, which corresponds to the stadium with the highest number of concerts after 2013.

This query will return the name and capacity of the single stadium that hosted the most concerts after 2013.