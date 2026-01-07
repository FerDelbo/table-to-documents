```markdown
# Count of Documents

To determine the total number of documents available, you can execute a SQL query that counts all rows in the `documents` table.

## SQL Query

```sql
SELECT count(*) FROM documents;
```

## Explanation

*   `SELECT count(*)`: This clause is used to count the total number of rows in the table. The `*` indicates that all rows should be counted, without any specific column filtering.
*   `FROM documents`: This specifies that the count operation should be performed on the `documents` table.

Executing this query will return a single numerical value representing the total number of documents in your database.
```