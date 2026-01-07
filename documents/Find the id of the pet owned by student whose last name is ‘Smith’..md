To find the ID of the pet owned by a student whose last name is 'Smith', you would typically query a database that contains information about students and their pets. The following document outlines the SQL query required to achieve this, along with an explanation of its components.

***

# Find Pet ID by Student Last Name

This document provides the SQL query to retrieve the pet ID associated with a student whose last name is 'Smith'. This operation involves joining two tables: `student` and `has_pet`.

## SQL Query

```sql
SELECT
  T2.petid
FROM student AS T1
JOIN has_pet AS T2
  ON T1.stuid = T2.stuid
WHERE
  T1.lname = 'Smith';
```

## Query Explanation

The query is structured to efficiently link students to their pets and then filter the results based on the student's last name.

1.  **`SELECT T2.petid`**: This specifies that the query should return the `petid` column from the `has_pet` table (aliased as `T2`). This is the unique identifier for the pet we are looking for.

2.  **`FROM student AS T1`**: The query starts by selecting data from the `student` table, which is aliased as `T1` for brevity. This table is presumed to contain student information, including their ID and last name.

3.  **`JOIN has_pet AS T2 ON T1.stuid = T2.stuid`**: An `INNER JOIN` is performed between the `student` table (`T1`) and the `has_pet` table (`T2`).
    *   The `has_pet` table acts as a linking table, associating students (`stuid`) with their pets (`petid`).
    *   The join condition `T1.stuid = T2.stuid` ensures that only records where a student from the `student` table is linked to a pet in the `has_pet` table are considered.

4.  **`WHERE T1.lname = 'Smith'`**: This clause filters the joined results. It specifies that we are only interested in records where the `lname` (last name) column in the `student` table (`T1`) is exactly 'Smith'.

## Expected Output

The query will return a list of `petid` values. Each `petid` in the result set will correspond to a pet owned by a student whose last name is 'Smith'. If multiple students named 'Smith' own pets, or if a single 'Smith' student owns multiple pets, all relevant `petid`s will be listed. If no student with the last name 'Smith' is found to own a pet, the query will return an empty result set.