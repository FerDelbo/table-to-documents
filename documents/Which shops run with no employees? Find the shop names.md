To find the names of shops that do not have any employees, you can use the following SQL query:

```sql
SELECT name
FROM shop
WHERE shop_id NOT IN (
    SELECT shop_id
    FROM hiring
);
```

### Explanation

This query works by:
1.  **`SELECT name FROM shop`**: This specifies that you want to retrieve the `name` column from the `shop` table.
2.  **`WHERE shop_id NOT IN (...)`**: This is a filtering condition. It means "select shops where the `shop_id` is NOT present in the results of the subquery."
3.  **`SELECT shop_id FROM hiring`**: This subquery retrieves all `shop_id` values from the `hiring` table, which represents shops that *do* have employees.

By combining these, the query effectively returns the names of all shops whose `shop_id` is not found in the `hiring` table, meaning those shops have no employees associated with them.