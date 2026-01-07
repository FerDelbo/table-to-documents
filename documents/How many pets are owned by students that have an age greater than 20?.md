To determine the number of pets owned by students older than 20, you would execute a SQL query that joins the `student` and `has_pet` tables and filters for students whose age is greater than 20.

## Query for Number of Pets Owned by Students Older Than 20

The following SQL query calculates the total count of pets associated with students who are older than 20 years of age.

```sql
SELECT
  COUNT(*)
FROM student AS t1
INNER JOIN has_pet AS t2
  ON t1.stuid = t2.stuid
WHERE
  t1.age > 20;
```

### Explanation

This query works by:
1.  **Joining Tables**: It performs an `INNER JOIN` between the `student` table (aliased as `t1`) and the `has_pet` table (aliased as `t2`). The join condition `t1.stuid = t2.stuid` links students to their respective pets using the student ID.
2.  **Filtering by Age**: The `WHERE t1.age > 20` clause filters the results to include only those records where the student's age is greater than 20.
3.  **Counting Results**: Finally, `COUNT(*)` counts all the rows that satisfy the join and filter conditions, effectively giving the total number of pets owned by students meeting the age criterion.

### Tables Involved

The primary tables used in this query are:
*   `student`: Contains information about students, including their `stuid` (student ID) and `age`.
*   `has_pet`: Links students (`stuid`) to their pets (`petid`), indicating ownership.