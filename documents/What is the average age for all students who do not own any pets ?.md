The average age for all students who do not own any pets can be found by querying the `student` and `has_pet` tables.

```sql
SELECT avg(age)
FROM student
WHERE stuid NOT IN (
    SELECT stuid
    FROM has_pet
)
```

### Explanation:

1.  **`SELECT avg(age)`**: This part specifies that we want to calculate the average of the `age` column.
2.  **`FROM student`**: This indicates that the `age` data will be retrieved from the `student` table.
3.  **`WHERE stuid NOT IN (...)`**: This is a filtering condition. It includes only those students whose `stuid` (student ID) is *not* present in the subquery's result.
4.  **`SELECT stuid FROM has_pet`**: This subquery retrieves all `stuid` values from the `has_pet` table. These are the IDs of students who *do* own pets.

By combining these, the query effectively calculates the average age of students whose IDs are not found in the list of students who own pets, thus answering the question "What is the average age for all students who do not own any pets?".