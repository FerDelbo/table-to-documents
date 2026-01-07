Here's how to count the number of documents, presented in Markdown format:

# Counting Documents

This document provides the SQL query to determine the total number of documents in the database.

## SQL Query

To count all entries in the `documents` table, use the following SQL query:

```sql
SELECT count(*) FROM documents
```

## Explanation

*   `SELECT count(*)`: This aggregate function is used to count the total number of rows in the table. The `*` indicates that all rows should be counted, regardless of their column values.
*   `FROM documents`: This specifies that the count operation should be performed on the `documents` table.

This query will return a single numerical value representing the total count of documents.