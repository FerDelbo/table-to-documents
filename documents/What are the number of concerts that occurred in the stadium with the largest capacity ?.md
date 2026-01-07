To find the number of concerts that occurred in the stadium with the largest capacity, you can use the following SQL query:

# Number of Concerts in the Largest Capacity Stadium

## Question
What are the number of concerts that occurred in the stadium with the largest capacity?

## SQL Query

```sql
SELECT count(*)
FROM concert
WHERE stadium_id = (
    SELECT stadium_id
    FROM stadium
    ORDER BY capacity DESC
    LIMIT 1
);
```

## Explanation

This query works in two main steps:

1.  **Find the `stadium_id` of the stadium with the largest capacity:**
    *   `SELECT stadium_id FROM stadium ORDER BY capacity DESC LIMIT 1`: This subquery selects the `stadium_id` from the `stadium` table, orders the stadiums by their `capacity` in descending order, and then limits the result to the top one, effectively giving the ID of the stadium with the maximum capacity.

2.  **Count concerts in that specific stadium:**
    *   `SELECT count(*) FROM concert WHERE stadium_id = (...)`: The outer query then counts all rows (`*`) from the `concert` table where the `stadium_id` matches the ID returned by the subquery (i.e., the stadium with the largest capacity).

This efficiently provides the total number of concerts held at the stadium capable of hosting the most attendees.

## Tables Involved

*   `concert`: Contains information about concerts, including the `stadium_id` where each concert took place.
*   `stadium`: Contains details about stadiums, including `stadium_id` and `capacity`.