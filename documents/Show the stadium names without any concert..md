To retrieve the names of stadiums that have not hosted any concerts, you can use a SQL query that identifies `stadium_id` values present in the `stadium` table but not in the `concert` table.

## Query to Find Stadiums Without Concerts

The following SQL query selects the `name` from the `stadium` table where the `stadium_id` is not present in the list of `stadium_id`s found in the `concert` table.

```sql
SELECT name
FROM stadium
WHERE stadium_id NOT IN (
    SELECT stadium_id
    FROM concert
);
```

### Explanation

1.  **`SELECT name FROM stadium`**: This part of the query initiates the selection process, targeting the `name` column from the `stadium` table. This is the primary information we want to retrieve.
2.  **`WHERE stadium_id NOT IN (...)`**: This is a filtering clause that restricts the results. It specifies that only those stadium records whose `stadium_id` is *not* found within the subquery's result set should be included.
3.  **`SELECT stadium_id FROM concert`**: This is a subquery that identifies all `stadium_id`s that *do* have at least one concert associated with them in the `concert` table.

By combining these parts, the query effectively isolates and returns the names of stadiums that exist in your database but have never been recorded as hosting a concert.

### Expected Output

The query will return a list of stadium names. Each name in the output corresponds to a stadium that currently has no concerts associated with it in the database.

For example:

```
Stadium A
Grand Arena
Riverside Field
```