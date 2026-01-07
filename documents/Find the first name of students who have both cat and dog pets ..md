To find the first name of students who own both a cat and a dog, you can use the following SQL query. This query leverages `JOIN` operations to link students to their pets and the `INTERSECT` operator to find students who satisfy both conditions (owning a cat AND owning a dog).

## Query: Students Owning Both Cat and Dog Pets

This document provides the SQL query and an explanation for identifying the first names of students who own both a cat and a dog.

### SQL Query

```sql
SELECT T1.fname
FROM student AS T1
JOIN has_pet AS T2
  ON T1.stuid = T2.stuid
JOIN pets AS T3
  ON T3.petid = T2.petid
WHERE
  T3.pettype = 'cat'
INTERSECT
SELECT T1.fname
FROM student AS T1
JOIN has_pet AS T2
  ON T1.stuid = T2.stuid
JOIN pets AS T3
  ON T3.petid = T2.petid
WHERE
  T3.pettype = 'dog';
```

### Explanation

1.  **`SELECT T1.fname FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'cat'`**:
    *   This first part of the query selects the `fname` (first name) from the `student` table.
    *   It joins `student` (aliased as `T1`) with `has_pet` (aliased as `T2`) on `stuid` to link students to their pets.
    *   It then joins with the `pets` table (aliased as `T3`) on `petid` to access pet type information.
    *   The `WHERE T3.pettype = 'cat'` clause filters these results to include only students who own a 'cat'.

2.  **`INTERSECT`**:
    *   The `INTERSECT` operator combines the results of two `SELECT` statements and returns only the rows that are present in *both* result sets. This is crucial for finding students who satisfy *both* criteria.

3.  **`SELECT T1.fname FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'dog'`**:
    *   This second part of the query is identical in structure to the first, but its `WHERE` clause filters for students who own a 'dog' (`T3.pettype = 'dog'`).

By using `INTERSECT`, the combined query effectively returns the `fname` of students who appear in both the list of cat owners and the list of dog owners, thus identifying students who own both types of pets.

### Tables Involved

*   `student`: Contains student information, including `stuid` (student ID) and `fname` (first name).
*   `has_pet`: A linking table that associates `stuid` (student ID) with `petid` (pet ID), indicating which student owns which pet.
*   `pets`: Contains pet information, including `petid` (pet ID) and `pettype` (type of pet).