To determine the number of documents using the template with type code 'PPT', you would execute a SQL query that joins the `documents` and `templates` tables and filters by the `template_type_code`.

Here is the SQL query to answer the question:

```sql
SELECT
  COUNT(*)
FROM documents AS T1
INNER JOIN templates AS T2
  ON T1.template_id = T2.template_id
WHERE
  T2.template_type_code = 'PPT';
```

### Explanation:

*   **`SELECT COUNT(*)`**: This part of the query counts the total number of rows that satisfy the conditions. In this context, each row represents a document.
*   **`FROM documents AS T1 INNER JOIN templates AS T2 ON T1.template_id = T2.template_id`**: This specifies that we are querying data from two tables: `documents` (aliased as `T1`) and `templates` (aliased as `T2`). An `INNER JOIN` is used to combine rows from both tables where there is a match on the `template_id` column, which links a document to its specific template.
*   **`WHERE T2.template_type_code = 'PPT'`**: This clause filters the joined results to include only those records where the `template_type_code` in the `templates` table (T2) is exactly 'PPT'.

This query will return a single number representing the count of documents that are associated with a template having the type code 'PPT'.