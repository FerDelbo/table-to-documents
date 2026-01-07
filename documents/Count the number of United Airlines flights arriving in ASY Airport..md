To count the number of United Airlines flights arriving in ASY Airport, you would use an SQL query that joins the `airlines` and `flights` tables, filters by the airline name 'United Airlines' and the destination airport 'ASY', and then counts the resulting flights.

Here's the technical documentation in Markdown format:

# Counting United Airlines Flights Arriving at ASY Airport

This document explains how to construct an SQL query to determine the number of flights operated by "United Airlines" that arrive at "ASY Airport".

## Database Schema Overview

For this query, we will primarily interact with two tables:
- **`airlines`**: Contains information about different airlines.
- **`flights`**: Contains details about individual flights, including the operating airline and departure/destination airports.

The relevant columns for this query are:
- `airlines.uid`: Unique identifier for an airline (used to join with `flights`).
- `airlines.airline`: The name of the airline (e.g., 'United Airlines').
- `flights.airline`: Foreign key linking to `airlines.uid`.
- `flights.destairport`: The destination airport code (e.g., 'ASY').

## SQL Query

To achieve the desired count, the following SQL query can be used:

```sql
SELECT
  COUNT(*)
FROM airlines AS T1
JOIN flights AS T2
  ON T2.airline = T1.uid
WHERE
  T1.airline = 'United Airlines' AND T2.destairport = 'ASY';
```

## Explanation

1.  **`SELECT COUNT(*)`**: This part of the query specifies that we want to count the total number of rows that satisfy the conditions. Each row in the result set will represent a flight matching the criteria.
2.  **`FROM airlines AS T1 JOIN flights AS T2 ON T2.airline = T1.uid`**:
    *   We start by selecting from the `airlines` table, aliased as `T1`.
    *   We then perform an `INNER JOIN` with the `flights` table, aliased as `T2`.
    *   The `ON T2.airline = T1.uid` clause establishes the join condition, linking flights to their respective airlines using their unique identifiers.
3.  **`WHERE T1.airline = 'United Airlines' AND T2.destairport = 'ASY'`**:
    *   This is the filtering clause that applies two conditions:
        *   `T1.airline = 'United Airlines'`: Filters the joined results to include only flights operated by "United Airlines".
        *   `T2.destairport = 'ASY'`: Further filters these flights to include only those whose destination airport code is 'ASY'.

This query will return a single numerical value representing the total count of "United Airlines" flights that arrive at "ASY Airport".