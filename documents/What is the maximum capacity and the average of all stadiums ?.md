To find the maximum and average capacity of all stadiums, you can use the following SQL query:

# Stadium Capacity Analysis

## Question
What is the maximum capacity and the average of all stadiums?

## SQL Query
```sql
SELECT max(Capacity), avg(Capacity)
FROM stadium;
```

## Explanation
This query retrieves two aggregate values from the `stadium` table:
*   `max(Capacity)`: Calculates the highest seating capacity among all stadiums.
*   `avg(Capacity)`: Computes the average seating capacity across all stadiums.

The `SELECT` statement specifies the columns to be returned, in this case, the maximum and average of the `Capacity` column. The `FROM stadium` clause indicates that the data should be fetched from the `stadium` table.