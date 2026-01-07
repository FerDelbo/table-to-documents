This document provides the SQL query to determine the number of pets owned by students older than 20 years of age.

## Query to Find Number of Pets Owned by Students Older Than 20

To find the number of pets owned by students whose age is greater than 20, you can use the following SQL query:

```sql
SELECT
  COUNT(*)
FROM student AS t1
JOIN has_pet AS t2
  ON t1.stuid = t2.stuid
WHERE
  t1.age > 20;
```

## Explanation

This query combines information from two tables, `student` and `has_pet`, to achieve the desired result.

1.  **`FROM student AS t1`**:
    *   Starts by selecting data from the `student` table, aliased as `t1`. This table presumably contains information about students, including their unique student ID (`stuid`) and age.

2.  **`JOIN has_pet AS t2 ON t1.stuid = t2.stuid`**:
    *   Performs an `INNER JOIN` with the `has_pet` table, aliased as `t2`.
    *   The `ON` clause `t1.stuid = t2.stuid` links students to their pets based on their common `stuid` (student ID). The `has_pet` table is expected to record which student owns which pet.

3.  **`WHERE t1.age > 20`**:
    *   Filters the joined results to include only those records where the student's age (from the `student` table, `t1.age`) is strictly greater than 20.

4.  **`SELECT COUNT(*)`**:
    *   Counts all rows that satisfy the `JOIN` and `WHERE` conditions. Each row in the `has_pet` table represents a single pet ownership, so counting these rows after filtering by student age gives the total number of pets owned by eligible students.

This query efficiently identifies and counts all pets associated with students who meet the specified age criterion.