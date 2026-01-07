To determine the number of countries listed, you can execute a SQL query that counts all entries in the `countries` table.

```sql
SELECT count(*) FROM countries;
```

### Explanation

*   **SELECT count(\*)**: This clause counts the total number of rows in the table. Each row represents a distinct country.
*   **FROM countries**: This specifies that the count operation should be performed on the `countries` table.

This query will return a single numerical value representing the total count of countries recorded in the database.