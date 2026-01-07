To find the total number of employees, you can execute a SQL query that counts all records in the `employee` table.

```sql
SELECT count(*) FROM employee;
```

### Explanation

*   `SELECT count(*)`: This part of the query is an aggregate function that counts the total number of rows in the `employee` table. The `*` indicates that all rows should be counted, regardless of their column values.
*   `FROM employee`: This specifies that the query should retrieve data from the `employee` table.

This query will return a single value representing the total count of employees.