The following document provides the SQL query to find the number of employees hired in each shop, along with the shop name.

## SQL Query to Count Employees Per Shop

To determine the number of employees hired in each shop and display their respective shop names, you can use a SQL query that joins the `hiring` and `shop` tables.

### Query

```sql
SELECT
  COUNT(*),
  T2.Name
FROM hiring AS T1
JOIN shop AS T2
  ON T1.shop_id = T2.shop_id
GROUP BY
  T2.Name;
```

### Explanation

This query operates by:

1.  **Joining Tables**: It links the `hiring` table (aliased as `T1`) with the `shop` table (aliased as `T2`) using the common column `shop_id`. This allows us to connect specific hiring records to their respective shop details.
2.  **Counting Employees**: The `COUNT(*)` aggregate function counts all the rows within each group. In this context, it counts the number of hiring records associated with each shop.
3.  **Grouping by Shop Name**: The `GROUP BY T2.Name` clause groups the results by the `Name` column from the `shop` table. This ensures that the `COUNT(*)` is applied separately for each unique shop, giving the total number of employees for that particular shop.
4.  **Selecting Output**: The query selects the `COUNT(*)` (number of employees) and the `T2.Name` (shop name) for clarity.

This structured query efficiently retrieves the desired information, presenting each shop's name alongside the total count of employees hired within it.