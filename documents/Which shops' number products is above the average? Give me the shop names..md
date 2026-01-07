To find the names of shops where the number of products is above the average, you can use the following SQL query:

```sql
SELECT
  name
FROM shop
WHERE
  number_products > (
    SELECT
      AVG(number_products)
    FROM shop
  );
```