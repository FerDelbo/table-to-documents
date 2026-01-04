To find the total number of singers, you can query the `singer` table to count all records.

## Query to Count All Singers

The SQL query to determine the total number of singers is as follows:

```sql
SELECT count(*) FROM singer
```

### Explanation

*   `SELECT count(*)`: This clause is used to count the total number of rows in the table. The `*` indicates that all rows should be counted, regardless of their column values.
*   `FROM singer`: This specifies that the operation should be performed on the `singer` table.

This query will return a single numerical value representing the total count of singers stored in the `singer` table.