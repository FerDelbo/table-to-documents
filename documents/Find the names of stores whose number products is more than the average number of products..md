This document provides the SQL query to find the names of stores that have a number of products greater than the average number of products across all stores.

## Query to Find Stores with Above-Average Products

To identify stores with a product count exceeding the overall average, you can use the following SQL query:

```sql
SELECT name
FROM shop
WHERE number_products > (SELECT AVG(number_products) FROM shop);
```

### Explanation of the SQL Query

This query uses a subquery to first calculate the average number of products. The outer query then filters the `shop` table to return only those stores whose `number_products` value is greater than this calculated average.

*   **`SELECT name`**: This specifies that the query will return the `name` column, which represents the name of each store.
*   **`FROM shop`**: This indicates that the data is being retrieved from the `shop` table.
*   **`WHERE number_products > (...)`**: This is the filtering condition. It ensures that only rows where the `number_products` column is greater than the result of the subquery are included in the final output.
*   **`(SELECT AVG(number_products) FROM shop)`**: This is a subquery.
    *   **`AVG(number_products)`**: This aggregate function calculates the average value of the `number_products` column from all records in the `shop` table.
    *   **`FROM shop`**: The subquery also operates on the `shop` table to determine the global average.

### How it Works

1.  The database first executes the **inner query**: `SELECT AVG(number_products) FROM shop`. This computes a single average value for `number_products` across all entries in the `shop` table.
2.  Then, the **outer query** takes this average value. It retrieves the `name` of every store from the `shop` table where its individual `number_products` count is strictly greater than the average calculated in the first step.

This ensures that you get a list of all stores that are performing above the average in terms of the number of products they offer.