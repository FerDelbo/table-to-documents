This document outlines the process to retrieve information about students who own a dog but do not own a cat, using a SQL query.

## Find Students with Dogs but No Cats

To identify students who possess a dog but do not have a cat as a pet, a SQL query involving joins and a subquery is required. This approach ensures that only students meeting both conditions are returned.

### SQL Query

```sql
SELECT
  T1.fname,
  T1.age
FROM student AS T1
JOIN has_pet AS T2
  ON T1.stuid = T2.stuid
JOIN pets AS T3
  ON T3.petid = T2.petid
WHERE
  T3.pettype = 'dog' AND T1.stuid NOT IN (
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

This query performs the following steps:

1.  **Select Student Information**: The outer `SELECT` statement aims to retrieve the `fname` (first name) and `age` from the `student` table.

2.  **Join Tables for Dog Owners**:
    *   The `student` table (aliased as `T1`) is joined with the `has_pet` table (aliased as `T2`) using `T1.stuid = T2.stuid`. This links students to the pets they own.
    *   The `has_pet` table (`T2`) is then joined with the `pets` table (aliased as `T3`) using `T3.petid = T2.petid`. This brings in the details about the pets, specifically their `pettype`.
    *   The `WHERE T3.pettype = 'dog'` condition filters this joined dataset to include only students who own at least one 'dog'.

3.  **Identify Cat Owners (Subquery)**:
    *   A subquery is used to identify all students who own a 'cat'. This subquery has a similar structure, joining `student`, `has_pet`, and `pets` tables.
    *   The condition `T3.pettype = 'cat'` specifically targets cat owners.
    *   The `SELECT T1.stuid` in the subquery returns the unique student IDs of all students who own a cat.

4.  **Exclude Cat Owners**:
    *   The `AND T1.stuid NOT IN (...)` clause in the outer query filters out any student whose `stuid` appears in the result set of the subquery (i.e., students who own a cat).

By combining these steps, the query effectively returns the first name and age of students who own at least one dog, but do not own any cats.

### Expected Output

The query will return a list of student records. Each record will contain:

*   **fname**: The first name of the student.
*   **age**: The age of the student.

This list will exclusively include students who satisfy the condition of owning a dog while not owning a cat.