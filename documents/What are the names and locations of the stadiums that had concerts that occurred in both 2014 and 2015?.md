To find the names and locations of stadiums that hosted concerts in both 2014 and 2015, you would use a SQL query that leverages the `INTERSECT` operator to combine results from two separate queries, each filtering for a specific year.

The following Markdown document details this process.

```markdown
# Stadiums Hosting Concerts in Both 2014 and 2015

This document outlines how to retrieve the names and locations of stadiums that hosted concerts in both the years 2014 and 2015 using SQL.

## 1. Understanding the Requirement

The core requirement is to identify stadiums that satisfy two conditions simultaneously:
1. Hosted at least one concert in the year 2014.
2. Hosted at least one concert in the year 2015.

To achieve this, we will perform two separate selections (one for each year) and then find the intersection of their results.

## 2. SQL Query

The SQL query to achieve this is structured as follows:

```sql
SELECT T2.name, T2.location
FROM concert AS T1
JOIN stadium AS T2
  ON T1.stadium_id = T2.stadium_id
WHERE
  T1.year = 2014
INTERSECT
SELECT T2.name, T2.location
FROM concert AS T1
JOIN stadium AS T2
  ON T1.stadium_id = T2.stadium_id
WHERE
  T1.year = 2015;
```

### Explanation of the Query:

*   **`SELECT T2.name, T2.location`**: This specifies that we want to retrieve the `name` and `location` columns from the `stadium` table (aliased as `T2`).
*   **`FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id`**: This part performs an `INNER JOIN` between the `concert` table (aliased as `T1`) and the `stadium` table (aliased as `T2`). The join condition `T1.stadium_id = T2.stadium_id` links concerts to their respective stadiums using the `stadium_id` foreign key.
*   **`WHERE T1.year = 2014`**: The first `WHERE` clause filters the concerts to only include those that occurred in the year `2014`.
*   **`INTERSECT`**: This set operator returns only the distinct rows that are returned by both the query on its left and the query on its right. In this case, it ensures that a stadium is only included in the final result if it appeared in *both* the 2014 results and the 2015 results.
*   **`SELECT T2.name, T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2015`**: This is the second query, identical in structure to the first, but it filters for concerts that occurred in the year `2015`.

## 3. How it Works

1.  The first `SELECT` statement identifies all stadiums that hosted a concert in 2014, returning their names and locations.
2.  The second `SELECT` statement identifies all stadiums that hosted a concert in 2015, returning their names and locations.
3.  The `INTERSECT` operator then compares the results of these two queries. Only the `name` and `location` pairs that are present in *both* result sets will be included in the final output. This effectively filters for stadiums that had at least one concert in 2014 AND at least one concert in 2015.

This method guarantees that only stadiums fulfilling both year-specific concert criteria are listed.
```