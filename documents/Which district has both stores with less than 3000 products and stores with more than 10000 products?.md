The following document provides the SQL query to identify districts that have both stores with less than 3000 products and stores with more than 10000 products.

```markdown
# Find Districts with Stores Having Both Low and High Product Counts

This document provides the SQL query to find the districts that contain at least one store with fewer than 3000 products and at least one store with more than 10000 products.

## SQL Query

To retrieve the districts that satisfy both conditions, an `INTERSECT` operator is used to combine the results of two separate `SELECT` statements.

```sql
SELECT district
FROM shop
WHERE number_products < 3000
INTERSECT
SELECT district
FROM shop
WHERE number_products > 10000;
```

### Query Explanation

1.  **`SELECT district FROM shop WHERE number_products < 3000`**:
    *   This subquery selects all `district` values from the `shop` table where the `number_products` is less than 3000. This identifies districts that have at least one store with a low product count.

2.  **`SELECT district FROM shop WHERE number_products > 10000`**:
    *   This subquery selects all `district` values from the `shop` table where the `number_products` is greater than 10000. This identifies districts that have at least one store with a high product count.

3.  **`INTERSECT`**:
    *   The `INTERSECT` operator returns only the distinct rows that are returned by both `SELECT` statements. In this context, it ensures that only districts appearing in *both* sets of results (i.e., having both low-product-count stores and high-product-count stores) are included in the final output.

## Example

Suppose the `shop` table contains the following data:

| shop_id | name        | district | number_products |
| :------ | :---------- | :------- | :-------------- |
| 1       | Gadget Hub  | Central  | 2500            |
| 2       | Tech Zone   | Central  | 12000           |
| 3       | Book Nook   | West     | 1500            |
| 4       | Toy World   | East     | 7000            |
| 5       | Game Haven  | Central  | 5000            |
| 6       | Art Supply  | West     | 11000           |

Applying the query would yield:

*   **First `SELECT` (products < 3000):** `Central`, `West`
*   **Second `SELECT` (products > 10000):** `Central`, `West`
*   **`INTERSECT` result:** `Central`, `West`

In this example, both 'Central' and 'West' districts would be returned because they each contain at least one store with fewer than 3000 products and at least one store with more than 10000 products.
```