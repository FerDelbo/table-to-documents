# Stadiums Without Concerts in 2014

To identify the names of all stadiums that did not host a concert in the year 2014, we can construct an SQL query that leverages the `EXCEPT` operator to find the difference between all stadium names and those stadiums that had a concert in 2014.

## SQL Query

```sql
SELECT name
FROM stadium
EXCEPT
SELECT T2.name
FROM concert AS T1
JOIN stadium AS T2
  ON T1.stadium_id = T2.stadium_id
WHERE
  T1.year = 2014;
```

## Query Explanation

This query is composed of two main parts connected by the `EXCEPT` operator:

1.  **First `SELECT` statement**:
    *   `SELECT name FROM stadium`: This retrieves the names of all stadiums from the `stadium` table.

2.  **Second `SELECT` statement (subquery)**:
    *   `SELECT T2.name FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id`: This part joins the `concert` table (aliased as `T1`) with the `stadium` table (aliased as `T2`) on their common `stadium_id`. It then selects the names of the stadiums.
    *   `WHERE T1.year = 2014`: This clause filters the joined results to include only those concerts that occurred in the year 2014.

3.  **`EXCEPT` operator**:
    *   The `EXCEPT` operator takes the results of the first query and removes any rows that are also present in the results of the second query. In this case, it will return the names of stadiums that appear in the list of all stadiums but **do not** appear in the list of stadiums that had a concert in 2014.

Therefore, the combined query effectively lists all stadiums that did not host any concert in the year 2014.