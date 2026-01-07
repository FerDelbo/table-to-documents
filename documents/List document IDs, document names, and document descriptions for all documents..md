Here's the Markdown document detailing how to list document IDs, names, and descriptions for all documents:

# Listing Document Details

This document outlines how to retrieve the document ID, document name, and document description for all entries in the `documents` table.

## 1. Objective

The main objective is to query the database to fetch comprehensive details about every document stored, including its unique identifier, its assigned name, and a descriptive text.

## 2. SQL Query

To achieve this, a simple `SELECT` statement targeting the `documents` table is used. This query will retrieve the specified columns for all rows in the table.

```sql
SELECT document_id, document_name, document_description FROM documents;
```

## 3. Explanation of the Query

*   **`SELECT document_id, document_name, document_description`**: This clause specifies the columns you want to retrieve from the table.
    *   `document_id`: The unique identifier for each document.
    *   `document_name`: The name given to the document.
    *   `document_description`: A brief description of the document's content or purpose.
*   **`FROM documents`**: This indicates that the data should be retrieved from the `documents` table.

## 4. Expected Output

The query will return a result set with three columns: `document_id`, `document_name`, and `document_description`. Each row in the result set will correspond to a single document in the `documents` table, providing its identifier, name, and description.

For example:

| document_id | document_name   | document_description           |
| :---------- | :-------------- | :----------------------------- |
| 1           | Robbin CV       | Curriculum Vitae for Robbin    |
| 2           | Project Proposal| Proposal for new software      |
| 3           | Summer Show     | Details about the summer event |
| ...         | ...             | ...                            |