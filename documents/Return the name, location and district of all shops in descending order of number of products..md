To retrieve the name, location, and district of all shops, ordered by the number of products in descending order, you would use the following SQL query.

## Query to List Shop Details by Product Count

### SQL Query
```sql
SELECT name, location, district
FROM shop
ORDER BY number_products DESC;
```

### Explanation

This query performs the following actions:

*   **`SELECT name, location, district`**: Specifies that the output should include the `name`, `location`, and `district` columns from the `shop` table.
*   **`FROM shop`**: Indicates that the data will be retrieved from the `shop` table.
*   **`ORDER BY number_products DESC`**: Sorts the results based on the `number_products` column in descending order (from the highest number of products to the lowest). This ensures that shops with more products appear first in the list.