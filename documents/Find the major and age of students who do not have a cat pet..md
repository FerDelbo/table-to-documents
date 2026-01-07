```markdown
# Students Without Cat Pets: Major and Age

This document provides the SQL query to retrieve the major and age of students who do not own a cat as a pet.

## SQL Query

To identify the major and age of students who do not have a cat pet, you can use the following SQL query:

```sql
SELECT
  major,
  age
FROM student
WHERE
  stuid NOT IN (
    SELECT
      T1.stuid
    FROM student AS T1
    JOIN has_pet AS T2
      ON T1.stuid = T2.stuid
    JOIN pets AS T3
      ON T3.petid = T2.petid
    WHERE
      T3.pettype = 'cat'
  );
```

### Explanation

*   **`SELECT major, age FROM student`**: This part of the query selects the `major` and `age` columns from the `student` table. This is the primary information we want to retrieve.
*   **`WHERE stuid NOT IN (...)`**: This clause filters the results from the `student` table. It includes only those students whose `stuid` (student ID) is *not* present in the subquery's result set.
*   **Subquery `(SELECT T1.stuid FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'cat')`**:
    *   This subquery is responsible for finding the `stuid` of all students who *do* own a cat.
    *   `FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid`: It joins the `student` table (aliased as `T1`) with the `has_pet` table (aliased as `T2`) on the `stuid` column, linking students to their pets.
    *   `JOIN pets AS T3 ON T3.petid = T2.petid`: It then joins with the `pets` table (aliased as `T3`) on the `petid` column, to get details about the pets.
    *   `WHERE T3.pettype = 'cat'`: This condition filters the joined results to include only records where the `pettype` is 'cat'.
    *   `SELECT T1.stuid`: Finally, it selects the `stuid` of these students (who own a cat).

By combining these parts, the main query effectively selects the major and age of students who are not found in the list of students owning a cat, thus identifying students who do not have a cat pet.
```