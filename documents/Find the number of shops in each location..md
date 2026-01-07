To find the number of shops in each location, you can use the following SQL query:

```sql
SELECT count(*), location
FROM shop
GROUP BY location;
```

### Explanation

*   **`SELECT count(*), location`**: This part of the query specifies what data you want to retrieve.
    *   `count(*)`: This aggregate function counts the total number of rows (shops in this case) for each group.
    *   `location`: This is the column that holds the location information for each shop.
*   **`FROM shop`**: This indicates that the data is being retrieved from the `shop` table.
*   **`GROUP BY location`**: This clause groups the rows that have the same `location` value. The `count(*)` function then operates on these groups, providing a count for each distinct location.

This query will return a result set with two columns: the count of shops and the respective location.