```markdown
# Battle Information

This document provides details about battles, including their names, dates, and results.

## Query

To retrieve the name, date, and result of each battle, the following SQL query can be used:

```sql
SELECT name, date, result FROM battle
```

## Explanation

*   **`SELECT name, date, result`**: This clause specifies the columns to be retrieved from the database. It selects the `name`, `date`, and `result` columns.
*   **`FROM battle`**: This clause indicates that the data should be fetched from the `battle` table.

This query will return a list containing the name, date, and result for every battle entry in the `battle` table.
```