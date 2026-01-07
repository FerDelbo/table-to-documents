To identify the airlines that have departing flights from both 'APG' and 'CVO' airports, you would perform a SQL query that uses an `INTERSECT` operator to find common airlines from two separate selections based on the `sourceairport`.

Here's the detailed technical documentation in Markdown format:

# Airlines with Departing Flights from Both APG and CVO Airports

This document explains how to query a database to find airlines that operate departing flights from two specified airports, 'APG' and 'CVO'. This requires joining the `airlines` and `flights` tables and utilizing the `INTERSECT` set operator.

## Database Schema

The relevant tables for this query are:

*   **`airlines`**: Contains information about various airlines.
    *   `uid`: Unique identifier for the airline (Primary Key).
    *   `airline`: Name of the airline.
    *   `abbreviation`: Abbreviation of the airline name.
    *   `country`: Country of origin for the airline.
    *   *(other columns may exist)*

*   **`flights`**: Contains details about individual flights.
    *   `flightid`: Unique identifier for the flight (Primary Key).
    *   `airline`: Foreign key referencing `airlines.uid`.
    *   `sourceairport`: The airport code where the flight departs from.
    *   `destairport`: The airport code where the flight arrives.
    *   *(other columns may exist)*

## Query Objective

The goal is to retrieve the names of airlines that have at least one departing flight from 'APG' airport AND at least one departing flight from 'CVO' airport.

## SQL Query

The following SQL query achieves this objective:

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

### Explanation

1.  **First `SELECT` statement (before `INTERSECT`)**:
    *   `SELECT T1.airline`: Selects the name of the airline.
    *   `FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.airline`: Joins the `airlines` table (aliased as `T1`) with the `flights` table (aliased as `T2`) based on their common `airline` identifier (`T1.uid` and `T2.airline`). This links airline names to their flights.
    *   `WHERE T2.sourceairport = 'APG'`: Filters these joined records to include only flights departing from the 'APG' airport. This subquery effectively lists all airlines that fly from 'APG'.

2.  **Second `SELECT` statement (after `INTERSECT`)**:
    *   This part of the query is structurally identical to the first, but with a different filter: `WHERE T2.sourceairport = 'CVO'`. This subquery lists all airlines that fly from 'CVO'.

3.  **`INTERSECT` Operator**:
    *   The `INTERSECT` operator combines the results of the two `SELECT` statements. It returns only the distinct `airline` names that are present in *both* sets of results. This means an airline must have had at least one flight from 'APG' *and* at least one flight from 'CVO' to be included in the final output.

## Example Usage (Conceptual)

If your database contained the following data:

**`airlines` table:**

| uid | airline           | abbreviation | country |
| :-- | :---------------- | :----------- | :------ |
| 1   | Airline A         | AA           | USA     |
| 2   | Airline B         | BB           | USA     |
| 3   | Airline C         | CC           | CAN     |

**`flights` table:**

| flightid | airline | sourceairport | destairport |
| :------- | :------ | :------------ | :---------- |
| 101      | 1       | APG           | JFK         |
| 102      | 1       | CVO           | LAX         |
| 103      | 2       | APG           | ORD         |
| 104      | 3       | CVO           | YYZ         |
| 105      | 1       | APG           | DFW         |
| 106      | 2       | MCO           | SFO         |

The query would produce:

| airline   |
| :-------- |
| Airline A |

*Airline A* is the only airline that has departing flights from both APG (flight 101, 105) and CVO (flight 102). *Airline B* only flies from APG (flight 103), and *Airline C* only flies from CVO (flight 104).