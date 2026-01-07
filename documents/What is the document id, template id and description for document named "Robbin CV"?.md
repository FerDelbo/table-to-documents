To retrieve the document ID, template ID, and description for the document named "Robbin CV", you would use the following SQL query:

```sql
SELECT
  document_id,
  template_id,
  document_description
FROM documents
WHERE
  document_name = 'Robbin CV';
```

### Explanation:

This query is designed to fetch specific details about a document from a `documents` table.

*   **`SELECT document_id, template_id, document_description`**: This specifies the columns you want to retrieve from the table.
    *   `document_id`: The unique identifier for the document.
    *   `template_id`: The identifier for the template used by the document.
    *   `document_description`: The descriptive text associated with the document.
*   **`FROM documents`**: This indicates that the data should be fetched from the `documents` table.
*   **`WHERE document_name = 'Robbin CV'`**: This is the filtering condition. It ensures that only the row(s) where the `document_name` column exactly matches 'Robbin CV' are returned.