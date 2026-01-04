This document provides the SQL query to retrieve the names of stadiums that have not hosted any concerts.

## Query: Names of Stadiums Without Concerts

To find the names of stadiums that have not hosted any concerts, you can use a SQL query that leverages a subquery with a `NOT IN` clause. This approach identifies `stadium_id` values from the `stadium` table that do not exist in the `concert` table.

### SQL Query

```sql
SELECT name
FROM stadium
WHERE stadium_id NOT IN (
    SELECT stadium_id
    FROM concert
);
```

### Explanation

1.  **`SELECT name FROM stadium`**: This part of the query specifies that we want to retrieve the `name` column from the `stadium` table.
2.  **`WHERE stadium_id NOT IN (...)`**: This is the filtering condition. It ensures that only those `stadium_id` values are selected from the `stadium` table that *do not* appear in the results of the subquery.
3.  **`SELECT stadium_id FROM concert`**: This is the subquery. It returns a list of all `stadium_id` values that are present in the `concert` table, meaning these stadiums *have* hosted at least one concert.

By combining these, the main query effectively filters the `stadium` table to show only the names of stadiums whose `stadium_id` is not found in the list of stadiums that have hosted concerts, thus identifying stadiums without any concerts.