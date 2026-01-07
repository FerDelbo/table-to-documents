To retrieve the major and age of every student who does not own a cat as a pet, you can use the following SQL query.

## Query to Find Major and Age of Students Without Cat Pets

This query identifies students who do not possess a cat pet by first selecting all student IDs associated with 'cat' type pets, and then excluding these students from the main selection of student majors and ages.

### SQL Query

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

1.  **Outer Query**:
    *   `SELECT major, age FROM student`: This part selects the `major` and `age` columns from the `student` table.
    *   `WHERE stuid NOT IN (...)`: This clause filters the students. It includes only those students whose `stuid` (student ID) is *not* present in the results of the subquery.

2.  **Inner Query (Subquery)**:
    *   `SELECT T1.stuid FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid`: This joins the `student`, `has_pet`, and `pets` tables.
        *   `student AS T1`: Aliases the `student` table as `T1`.
        *   `has_pet AS T2`: Aliases the `has_pet` table as `T2`.
        *   `pets AS T3`: Aliases the `pets` table as `T3`.
        *   The joins link students to their pets via the `has_pet` intermediary table.
    *   `WHERE T3.pettype = 'cat'`: This filters the joined results to only include records where the `pettype` in the `pets` table is 'cat'.
    *   The subquery effectively returns a list of `stuid`s for all students who own at least one cat.

By combining the outer and inner queries, the final result set will contain the `major` and `age` of all students who do not own any cats.