To retrieve the first name and gender of all students who own more than one pet, you can use the following SQL query.

## Query to Find Students with Multiple Pets

This document provides a SQL query to identify students who own more than one pet, listing their first names and genders.

### SQL Query

```sql
SELECT
  T1.fname,
  T1.sex
FROM student AS T1
JOIN has_pet AS T2
  ON T1.stuid = T2.stuid
GROUP BY
  T1.stuid
HAVING
  COUNT(*) > 1;
```

### Explanation

This query involves two tables: `student` and `has_pet`.

1.  **`FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid`**:
    *   This part joins the `student` table (aliased as `T1`) with the `has_pet` table (aliased as `T2`).
    *   The join condition `T1.stuid = T2.stuid` links students to their pets based on their unique student ID.

2.  **`GROUP BY T1.stuid`**:
    *   After joining, the results are grouped by `stuid` (student ID) from the `student` table. This is crucial because we want to count the number of pets for each individual student.

3.  **`HAVING COUNT(*) > 1`**:
    *   The `HAVING` clause filters these grouped results. It retains only those groups (students) for which the count of associated records in the `has_pet` table (i.e., the number of pets) is greater than 1.

4.  **`SELECT T1.fname, T1.sex`**:
    *   Finally, for each student who meets the criteria (owning more than one pet), the query selects their `fname` (first name) and `sex` (gender) from the `student` table.

This query efficiently identifies and presents the requested information by combining student details with their pet ownership records and applying an aggregation filter.