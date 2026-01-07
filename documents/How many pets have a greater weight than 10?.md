To determine the number of pets with a weight greater than 10, you can use the following SQL query.

# Querying Pet Data: Pets with Weight Greater Than 10

This document provides the SQL query to count the total number of pets whose weight exceeds 10 units.

## 1. The Question

How many pets have a greater weight than 10?

## 2. SQL Query

```sql
SELECT count(*)
FROM pets
WHERE weight > 10;
```

## 3. Explanation

This SQL query performs the following actions:
*   **`SELECT count(*)`**: This counts all rows that satisfy the `WHERE` condition. The `count(*)` aggregate function returns the total number of records.
*   **`FROM pets`**: This specifies that the query will retrieve data from the `pets` table.
*   **`WHERE weight > 10`**: This clause filters the results, including only those records where the value in the `weight` column is strictly greater than 10.

## 4. Table Involved

The query operates on the `pets` table.