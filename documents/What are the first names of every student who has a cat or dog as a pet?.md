To retrieve the first names of every student who owns a cat or dog as a pet, you would execute a SQL query that joins the `student`, `has_pet`, and `pets` tables, and then filters the results based on the `pettype` column.

## Query to Find First Names of Students with Cat or Dog Pets

The following SQL query will provide the first names of students who have either a cat or a dog as a pet:

```sql
SELECT DISTINCT
  T1.fname
FROM student AS T1
JOIN has_pet AS T2
  ON T1.stuid = T2.stuid
JOIN pets AS T3
  ON T3.petid = T2.petid
WHERE
  T3.pettype = 'cat' OR T3.pettype = 'dog';
```

### Explanation

1.  **`SELECT DISTINCT T1.fname`**: This clause selects the `fname` (first name) column from the `student` table (`T1`). The `DISTINCT` keyword ensures that each student's first name appears only once in the result, even if a student owns multiple cats or dogs.

2.  **`FROM student AS T1`**: This specifies that we are starting our query from the `student` table, which is aliased as `T1` for brevity.

3.  **`JOIN has_pet AS T2 ON T1.stuid = T2.stuid`**: This performs an inner join with the `has_pet` table (aliased as `T2`). The join condition `T1.stuid = T2.stuid` links students to their pets via their respective student IDs.

4.  **`JOIN pets AS T3 ON T3.petid = T2.petid`**: This further joins the result with the `pets` table (aliased as `T3`). The join condition `T3.petid = T2.petid` connects the `has_pet` records to the actual pet details, including their type.

5.  **`WHERE T3.pettype = 'cat' OR T3.pettype = 'dog'`**: This `WHERE` clause filters the joined results to include only those records where the `pettype` in the `pets` table (`T3`) is either 'cat' or 'dog'.

This query efficiently identifies and lists the unique first names of all students who satisfy the condition of owning a cat or a dog.