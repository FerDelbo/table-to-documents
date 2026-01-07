```markdown
# Count of Distinct Document Templates

To determine the number of unique templates utilized across all documents, a SQL query can be executed to count the distinct `template_id` values in the `documents` table.

## SQL Query

The following SQL query achieves this by using the `COUNT` aggregate function with the `DISTINCT` keyword on the `template_id` column of the `documents` table:

```sql
SELECT COUNT(DISTINCT template_id) FROM documents;
```

## Explanation

*   **`SELECT COUNT(DISTINCT template_id)`**: This part of the query counts the number of unique values present in the `template_id` column. The `DISTINCT` keyword ensures that each unique template ID is counted only once, even if it appears multiple times in the `documents` table (meaning it's used by multiple documents).
*   **`FROM documents`**: This specifies that the data for the count should be retrieved from the `documents` table.

This query will return a single numerical value representing the total count of different templates that have been assigned to documents.
```