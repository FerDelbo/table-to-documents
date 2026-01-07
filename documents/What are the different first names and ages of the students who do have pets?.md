This document provides the SQL query to retrieve the distinct first names and ages of students who own pets, based on the provided dataset.

## Query: Students with Pets

### Question
What are the different first names and ages of the students who do have pets?

### SQL Query
To find the distinct first names and ages of students who have pets, you would use the following SQL query:

```sql
SELECT DISTINCT T1.fname, T1.age
FROM student AS T1
JOIN has_pet AS T2
  ON T1.stuid = T2.stuid;
```

### Explanation of the Query

This query identifies students who have pets by joining two tables: `student` and `has_pet`.

*   **`SELECT DISTINCT T1.fname, T1.age`**: This clause specifies that the query should return the `fname` (first name) and `age` of the students. The `DISTINCT` keyword ensures that only unique combinations of first name and age are returned, preventing duplicate entries if a student has multiple pets or is listed multiple times in the `has_pet` table.
*   **`FROM student AS T1`**: This indicates that the primary table for the query is `student`, aliased as `T1` for brevity. The `student` table is expected to contain information about students, including their unique student ID (`stuid`), first name (`fname`), and age (`age`).
*   **`JOIN has_pet AS T2 ON T1.stuid = T2.stuid`**: This performs an `INNER JOIN` operation between the `student` table (`T1`) and the `has_pet` table (`T2`).
    *   The `has_pet` table is expected to link students to their pets, likely containing `stuid` (student ID) and `petid` (pet ID).
    *   The `ON T1.stuid = T2.stuid` condition matches rows from both tables where the `stuid` is the same. This effectively filters for only those students who have at least one entry in the `has_pet` table, meaning they own a pet. Students without any pet entries in `has_pet` would not be included in the result.

In essence, the query retrieves the first name and age of every student who is recorded as owning a pet, ensuring that each unique student's details are listed only once.