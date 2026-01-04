To find the average and maximum capacities for all stadiums, you can use a SQL query that calculates these aggregate functions on the `capacity` column of the `stadium` table.

---

# Stadium Capacity Analysis: Average and Maximum

This document provides the SQL query to retrieve the average and maximum capacities across all stadiums in the database.

## SQL Query

The following SQL query is used to calculate the average and maximum capacities:

```sql
SELECT
  AVG(capacity),
  MAX(capacity)
FROM stadium;
```

## Query Explanation

*   `SELECT AVG(capacity), MAX(capacity)`: This part of the query specifies that we want to retrieve two aggregate values:
    *   `AVG(capacity)`: Calculates the average value of the `capacity` column.
    *   `MAX(capacity)`: Determines the highest value in the `capacity` column.
*   `FROM stadium`: This indicates that the data for these calculations should be sourced from the `stadium` table.

## Relevant Table

The query interacts with the following table:

*   **`stadium`**: This table is expected to contain information about various stadiums, including a `capacity` column that stores the seating capacity for each stadium.

## Expected Output

Executing this query will return a single row with two columns:

| AVG(capacity) | MAX(capacity) |
| :------------ | :------------ |
| [Average_Value] | [Maximum_Value] |

Where:
*   `[Average_Value]` will be the calculated average capacity of all stadiums.
*   `[Maximum_Value]` will be the single highest capacity found among all stadiums.