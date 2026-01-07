To find the districts that contain both shops selling less than 3000 products and shops selling more than 10000 products, you can use the following SQL query and explanation.

## Query for Districts with Varied Product Offerings

This document outlines how to retrieve the names of districts that host shops with both low and high product counts, specifically those with less than 3000 products and those with more than 10000 products.

### SQL Query

```sql
SELECT district
FROM shop
WHERE number_products < 3000
INTERSECT
SELECT district
FROM shop
WHERE number_products > 10000;
```

### Explanation

The query uses the `INTERSECT` operator to find districts that satisfy two distinct conditions:

1.  **`SELECT district FROM shop WHERE number_products < 3000`**: This subquery identifies all districts where at least one shop sells fewer than 3000 products.
2.  **`SELECT district FROM shop WHERE number_products > 10000`**: This subquery identifies all districts where at least one shop sells more than 10000 products.

The `INTERSECT` operator then returns only the `district` values that are present in **both** result sets. This ensures that only districts containing both types of shops (low product count and high product count) are included in the final output.

### Assumptions

*   A table named `shop` exists.
*   The `shop` table contains columns named `district` (for the district where the shop is located) and `number_products` (representing the number of products sold by the shop).
*   `number_products` is a numerical column.

### Example Output

Given a `shop` table with data similar to this:

| shop_id | name        | district     | number_products |
| :------ | :---------- | :----------- | :-------------- |
| 1       | Shop A      | Downtown     | 1500            |
| 2       | Shop B      | Downtown     | 12000           |
| 3       | Shop C      | Uptown       | 2500            |
| 4       | Shop D      | Midtown      | 8000            |
| 5       | Shop E      | Downtown     | 500             |
| 6       | Shop F      | Uptown       | 15000           |
| 7       | Shop G      | Suburb       | 2000            |

The query would produce an output similar to:

```
district
----------
Downtown
Uptown
```

This output indicates that 'Downtown' and 'Uptown' are the districts where you can find both shops with less than 3000 products and shops with more than 10000 products.