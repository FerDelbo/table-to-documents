To retrieve the document ID, template ID, and description for the document named "Robbin CV", you can use the following SQL query.

```sql
SELECT document_id, template_id, document_description
FROM documents
WHERE document_name = 'Robbin CV';
```

### Explanation

This query performs the following actions:

1.  **`SELECT document_id, template_id, document_description`**: This specifies the columns you want to retrieve from the `documents` table. These columns directly correspond to the requested information: the unique identifier for the document, the ID of the template it uses, and its textual description.
2.  **`FROM documents`**: This indicates that the data should be retrieved from the `documents` table.
3.  **`WHERE document_name = 'Robbin CV'`**: This is the filtering condition. It ensures that only the row(s) where the `document_name` column exactly matches 'Robbin CV' are selected. This will pinpoint the specific document you are interested in.