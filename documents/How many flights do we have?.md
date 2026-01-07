To determine the total number of flights, you can execute a SQL query that counts all records within the `flights` table.

### SQL Query

```sql
SELECT count(*) FROM flights;
```

### Explanation

*   **`SELECT count(*)`**: This clause is used to count the total number of rows in the `flights` table. The `*` inside `count()` indicates that all rows should be counted, without any specific column filtering.
*   **`FROM flights`**: This specifies that the query should retrieve data from the `flights` table.

This query will return a single value representing the total count of flights recorded in the database.