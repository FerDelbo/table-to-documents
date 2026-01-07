This document provides a SQL query to determine the number of distinct pet types, along with an explanation of the query.

## How many different types of pet are there?

To find out the total number of unique pet types, you can query the `pets` table and count the distinct values in the `pettype` column.

### SQL Query

```sql
SELECT COUNT(DISTINCT pettype) FROM pets;
```

### Explanation

*   **`SELECT COUNT(DISTINCT pettype)`**: This clause is used to count the number of unique entries in the `pettype` column.
    *   `COUNT(*)` counts all rows.
    *   `DISTINCT pettype` ensures that only unique `pettype` values are considered before counting, effectively eliminating duplicate pet types.
*   **`FROM pets`**: This specifies that the query should retrieve data from the `pets` table.

This query will return a single numerical value representing the total count of different pet types recorded in the database.