```markdown
# Number of Flights

To determine the total number of flights, you would query the `flights` table to count all entries.

## SQL Query

```sql
SELECT count(*) FROM flights;
```

## Explanation

*   **`SELECT count(*)`**: This part of the query counts all rows in the table. The `*` indicates that all columns are considered for the count, effectively counting all records.
*   **`FROM flights`**: This specifies that the operation should be performed on the `flights` table.

This query will return a single numerical value representing the total count of flights recorded in the database.
```