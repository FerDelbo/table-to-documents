To determine the number of shops in each location, you can execute a SQL query that counts the occurrences of shops grouped by their location. This provides a summary of shop distribution across different geographical areas.

### SQL Query for Counting Shops per Location

To get the count of shops for each location, use the following SQL query:

```sql
SELECT
  location,
  COUNT(*) AS number_of_shops
FROM shop
GROUP BY
  location;
```

### Explanation

1.  **`SELECT location, COUNT(*) AS number_of_shops`**:
    *   `location`: This selects the location column, which is the attribute by which we want to group the shops.
    *   `COUNT(*)`: This aggregate function counts all rows within each group.
    *   `AS number_of_shops`: This assigns an alias `number_of_shops` to the count column, making the output more readable.

2.  **`FROM shop`**:
    *   This specifies that the query will retrieve data from the `shop` table.

3.  **`GROUP BY location`**:
    *   This clause groups the rows that have the same `location` value into summary rows. The `COUNT(*)` function then operates on these groups, giving a separate count for each unique location.

### Example Output

Executing this query would yield a result set similar to this:

| location         | number_of_shops |
| :--------------- | :-------------- |
| Downtown         | 5               |
| City Center      | 3               |
| West Side        | 2               |
| East End         | 4               |
| Financial District | 1               |

This table clearly shows each distinct location and the total number of shops associated with that location.