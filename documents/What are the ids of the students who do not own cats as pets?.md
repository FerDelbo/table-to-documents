To retrieve the IDs of students who do not own cats as pets, you can use a SQL query that identifies all student IDs and then subtracts the IDs of students who are identified as owning a cat.

## SQL Query for Students Without Cat Pets

The following SQL query selects all student IDs from the `student` table and then uses the `EXCEPT` operator to remove the IDs of students who own a pet of type 'cat'.

```sql
SELECT StID
FROM student
EXCEPT
SELECT T1.StID
FROM student AS T1
JOIN has_pet AS T2
  ON T1.StID = T2.StID
JOIN pets AS T3
  ON T3.petid = T2.petid
WHERE
  T3.pettype = 'cat';
```

### Explanation

1.  **`SELECT StID FROM student`**: This part of the query retrieves the student IDs of all students registered in the `student` table.
2.  **`EXCEPT`**: This set operator returns all unique rows from the first `SELECT` statement that are not found in the second `SELECT` statement.
3.  **`SELECT T1.StID FROM student AS T1 JOIN has_pet AS T2 ON T1.StID = T2.StID JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'cat'`**: This subquery identifies the student IDs (`StID`) of all students who own a pet. It joins the `student`, `has_pet`, and `pets` tables to link students to their pets and then filters for pets where `pettype` is 'cat'.

By combining these two parts with `EXCEPT`, the query effectively lists the student IDs of those students who do not own any cats as pets.