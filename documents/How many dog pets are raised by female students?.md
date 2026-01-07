To determine the number of dog pets raised by female students, you can execute the following SQL query:

```sql
SELECT count(*) FROM student AS t1 JOIN has_pet AS t2 ON t1.stuid = t2.stuid JOIN pets AS t3 ON t2.petid = t3.petid WHERE t1.sex = 'F' AND t3.pettype = 'dog'
```

### Explanation

This query performs the following actions:

1.  **`SELECT count(*)`**: This counts the total number of rows that satisfy the conditions specified later in the query. Each row represents a connection between a female student and her dog pet.
2.  **`FROM student AS t1 JOIN has_pet AS t2 ON t1.stuid = t2.stuid JOIN pets AS t3 ON t2.petid = t3.petid`**: This section joins three tables:
    *   `student` (aliased as `t1`) contains information about students.
    *   `has_pet` (aliased as `t2`) links students to their pets.
    *   `pets` (aliased as `t3`) contains details about the pets themselves.
    The joins are established based on matching student IDs (`stuid`) between `student` and `has_pet`, and matching pet IDs (`petid`) between `has_pet` and `pets`.
3.  **`WHERE t1.sex = 'F' AND t3.pettype = 'dog'`**: This filters the joined results to include only:
    *   Students whose `sex` (from the `student` table) is 'F' (female).
    *   Pets whose `pettype` (from the `pets` table) is 'dog'.

The combination of these conditions ensures that the count returned is precisely the number of dog pets that are owned by female students.

### Tables Involved

*   `student`
*   `has_pet`
*   `pets`