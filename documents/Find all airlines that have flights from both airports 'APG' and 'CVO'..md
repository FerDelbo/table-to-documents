This document provides a SQL query to identify airlines that operate flights from two specific airports: 'APG' and 'CVO'.

## Question

Find all airlines that have flights from both airports 'APG' and 'CVO'.

## SQL Query

```sql
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.sourceairport = 'APG'
INTERSECT
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.sourceairport = 'CVO';
```

## Explanation

The query uses the `INTERSECT` operator to find airlines that satisfy two separate conditions: having flights departing from 'APG' and having flights departing from 'CVO'.

Here's a breakdown of the query components:

1.  **First `SELECT` Statement (Flights from 'APG'):**
    *   `SELECT T1.airline`: This selects the name of the airline. `T1` is an alias for the `airlines` table.
    *   `FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.airline`: This performs an `INNER JOIN` between the `airlines` table (aliased as `T1`) and the `flights` table (aliased as `T2`). The join condition `T1.uid = T2.airline` links flights to their respective airlines using the unique identifier (`uid`) from the `airlines` table and the `airline` foreign key in the `flights` table.
    *   `WHERE T2.sourceairport = 'APG'`: This filters the results to include only flights that originate from the airport with the code 'APG'.

2.  **Second `SELECT` Statement (Flights from 'CVO'):**
    *   This part is identical in structure to the first `SELECT` statement, but its `WHERE` clause is modified to filter for flights originating from the airport with the code 'CVO': `WHERE T2.sourceairport = 'CVO'`.

3.  **`INTERSECT` Operator:**
    *   The `INTERSECT` operator combines the results of the two `SELECT` statements. It returns only the distinct `airline` names that are present in *both* result sets. This ensures that only airlines that operate flights from *both* 'APG' and 'CVO' airports are included in the final output.

## Assumed Schema

To understand this query, we assume the following simplified schema for the `airlines` and `flights` tables:

*   **`airlines` Table:**
    *   `uid`: Unique identifier for the airline (Primary Key).
    *   `airline`: Name of the airline.
    *   `abbreviation`: Abbreviation of the airline.
    *   `country`: Country of origin for the airline.

*   **`flights` Table:**
    *   `flightno`: Flight number.
    *   `airline`: Foreign key referencing `airlines.uid`.
    *   `sourceairport`: Code of the departure airport.
    *   `destairport`: Code of the destination airport.

The query effectively identifies common airlines by first listing all airlines associated with departures from 'APG' and then listing all airlines associated with departures from 'CVO', finally finding the intersection of these two lists.