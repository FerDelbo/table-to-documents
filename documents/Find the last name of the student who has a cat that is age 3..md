To find the last name of the student who owns a 3-year-old cat, we need to query a database that contains information about students, their pets, and the details of those pets.

## SQL Query

The SQL query to achieve this is as follows:

```sql
SELECT
  T1.lname
FROM student AS T1
INNER JOIN has_pet AS T2
  ON T1.stuid = T2.stuid
INNER JOIN pets AS T3
  ON T3.petid = T2.petid
WHERE
  T3.pet_age = 3 AND T3.pettype = 'cat';
```

## Explanation

This query performs the following steps:

1.  **`SELECT T1.lname`**: It selects the `lname` (last name) column from the `student` table.
2.  **`FROM student AS T1`**: It starts by selecting from the `student` table, aliased as `T1`.
3.  **`INNER JOIN has_pet AS T2 ON T1.stuid = T2.stuid`**: It joins the `student` table (`T1`) with the `has_pet` table (`T2`). This join links students to the pets they own using their respective `stuid` (student ID).
4.  **`INNER JOIN pets AS T3 ON T3.petid = T2.petid`**: It then joins the result with the `pets` table (`T3`). This links the `has_pet` records to the actual pet details using their `petid` (pet ID).
5.  **`WHERE T3.pet_age = 3 AND T3.pettype = 'cat'`**: This is the filtering condition. It narrows down the results to only include pets that are exactly 3 years old (`pet_age = 3`) AND are of the type 'cat' (`pettype = 'cat'`).

By combining these steps, the query efficiently identifies and returns the last names of all students who own a cat that is 3 years old.