This document provides a comprehensive answer to the question regarding how to find the first name of every student who owns a dog but does not own a cat, formatted in Markdown.

## Find Students with Dogs but No Cats

This section details the SQL query required to identify the first names of students who own at least one dog, but do not own any cats, based on a hypothetical database schema.

### Database Schema

To understand the query, let's consider a simplified database schema with the following tables and relevant columns:

*   **`student` Table**: Stores information about students.
    *   `stuid` (Primary Key): Unique identifier for the student.
    *   `fname`: First name of the student.
    *   `age`: Age of the student.
    *   *(Other student details...)*
*   **`has_pet` Table**: Links students to their pets.
    *   `stuid` (Foreign Key): References `student.stuid`.
    *   `petid` (Foreign Key): References `pets.petid`.
*   **`pets` Table**: Stores information about pets.
    *   `petid` (Primary Key): Unique identifier for the pet.
    *   `pettype`: Type of the pet (e.g., 'dog', 'cat', 'bird').
    *   *(Other pet details...)*

### The Question

"What is the first name of every student who has a dog but does not have a cat?"

### SQL Query

To retrieve the first names of students who own dogs but do not own cats, you can use the following SQL query:

```sql
SELECT
  T1.fname
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

This query combines information from three tables (`student`, `has_pet`, and `pets`) to first identify students who own dogs, and then filters that list to exclude any students who also own cats.

1.  **`FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid`**:
    *   This part sets up the necessary joins between the `student`, `has_pet`, and `pets` tables.
    *   It links students (`T1`) to their pets through the `has_pet` table (`T2`), and then links those `has_pet` entries to the specific pet types in the `pets` table (`T3`). This allows us to access student details and pet types together.

2.  **`WHERE T3.pettype = 'dog'`**:
    *   This initial `WHERE` clause filters the joined records to include only those where the pet type is 'dog'. This ensures we are only considering students who own at least one dog.

3.  **`AND T1.stuid NOT IN (...)`**:
    *   This is the crucial part that excludes students who own cats. The `NOT IN` operator checks if a student's ID (`T1.stuid`) is *not* present in the results of the subquery.

4.  **Subquery: `(SELECT T1.stuid FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'cat')`**:
    *   This inner query functions similarly to the main query's joins, but its purpose is specifically to find the `stuid` (Student IDs) of *all* students who own at least one cat.
    *   It joins `student`, `has_pet`, and `pets` tables and filters for `pettype = 'cat'`.

5.  **`SELECT T1.fname`**:
    *   Finally, the query selects only the `fname` (first name) of the students who satisfy both conditions: owning a dog AND not owning a cat.

### Example Scenario

Let's imagine the following data:

**`student` table:**

| stuid | fname   | age |
| :---- | :------ | :-- |
| 101   | Alice   | 20  |
| 102   | Bob     | 22  |
| 103   | Carol   | 21  |
| 104   | David   | 23  |

**`pets` table:**

| petid | pettype |
| :---- | :------ |
| 1     | dog     |
| 2     | cat     |
| 3     | dog     |
| 4     | fish    |
| 5     | cat     |

**`has_pet` table:**

| stuid | petid |
| :---- | :---- |
| 101   | 1     |
| 101   | 2     |
| 102   | 3     |
| 103   | 5     |
| 104   | 1     |

Applying the query:

1.  **Students with dogs**: Alice (petid 1), Bob (petid 3), David (petid 1)
2.  **Students with cats (subquery result)**: Alice (petid 2), Carol (petid 5)
3.  **Exclude students with cats from students with dogs**:
    *   Alice is excluded because she has a dog (petid 1) AND a cat (petid 2).
    *   Bob has a dog (petid 3) but no cat.
    *   David has a dog (petid 1) but no cat.

**Expected Result:**

| fname |
| :---- |
| Bob   |
| David |