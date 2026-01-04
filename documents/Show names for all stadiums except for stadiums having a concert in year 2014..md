This document provides a solution in SQL (Structured Query Language) to identify the names of all stadiums that did not host any concerts in the year 2014.

## Querying Stadiums Without 2014 Concerts

To achieve this, we will use a set operation to subtract the stadiums that had concerts in 2014 from the complete list of all stadiums.

### SQL Query

```sql
SELECT name
FROM stadium
EXCEPT
SELECT T2.name
FROM concert AS T1
JOIN stadium AS T2
  ON T1.stadium_id = T2.stadium_id
WHERE
  T1.year = 2014;
```

### Query Explanation

This SQL query is structured into two main parts connected by the `EXCEPT` operator:

1.  **First `SELECT` statement (`SELECT name FROM stadium`)**: This part retrieves the `name` of every stadium from the `stadium` table. This forms our initial set of all stadiums.

2.  **Second `SELECT` statement (subquery)**: This subquery identifies all stadiums that *did* host a concert in the year 2014.
    *   `FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id`: This joins the `concert` table (aliased as `T1`) with the `stadium` table (aliased as `T2`) on their common `stadium_id` to link concerts to their respective stadiums.
    *   `WHERE T1.year = 2014`: This clause filters the results to include only concerts that took place in the year 2014.
    *   `SELECT T2.name`: This selects the names of the stadiums where these 2014 concerts occurred.

3.  **`EXCEPT` Operator**: The `EXCEPT` operator takes the result set of the first `SELECT` statement and removes any rows that are also present in the result set of the second `SELECT` statement. In essence, it gives us the names of stadiums from the full list that are *not* found in the list of stadiums that hosted concerts in 2014.

### Involved Tables

The query utilizes the following tables:

*   **`stadium`**: Contains information about various stadiums, including their `name` and `stadium_id`.
*   **`concert`**: Contains details about concerts, including the `stadium_id` where the concert took place and the `year` of the concert.

### Example Schema (Illustrative)

To better understand the query, consider a simplified schema for the involved tables:

#### `stadium` Table

| Column       | Type    | Description             |
| :----------- | :------ | :---------------------- |
| `stadium_id` | INTEGER | Unique ID for the stadium |
| `name`       | TEXT    | Name of the stadium     |
| `location`   | TEXT    | Location of the stadium |
| `capacity`   | INTEGER | Seating capacity        |

#### `concert` Table

| Column         | Type    | Description                |
| :------------- | :------ | :------------------------- |
| `concert_id`   | INTEGER | Unique ID for the concert  |
| `stadium_id`   | INTEGER | ID of the stadium hosting the concert |
| `concert_name` | TEXT    | Name of the concert        |
| `year`         | INTEGER | Year the concert took place |
| `theme`        | TEXT    | Theme of the concert       |

This query effectively isolates and presents the names of stadiums that remained concert-free during the specified year, 2014.