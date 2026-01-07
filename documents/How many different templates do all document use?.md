To determine the number of distinct templates used by all documents, you can query the `documents` table to count the unique `template_id` values.

### SQL Query

```sql
SELECT count(DISTINCT template_id)
FROM documents;
```

### Explanation

This query performs the following actions:
*   `SELECT count(DISTINCT template_id)`: This counts the number of unique `template_id` values. The `DISTINCT` keyword ensures that each unique template is counted only once, even if it is used by multiple documents.
*   `FROM documents`: This specifies that the query should retrieve data from the `documents` table.

Executing this query will return a single numerical value representing the total number of different templates utilized across all documents.