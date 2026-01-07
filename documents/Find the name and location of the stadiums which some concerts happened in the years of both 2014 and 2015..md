To find the name and location of stadiums that hosted concerts in both 2014 and 2015, you can use a SQL query that leverages the `INTERSECT` operator to combine results from two separate selections based on the concert year.

---

# Find Stadiums with Concerts in Both 2014 and 2015

This document outlines how to retrieve the names and locations of stadiums that have hosted concerts in both the years 2014 and 2015, using a SQL query.

## Question

The specific question is: "Find the name and location of the stadiums which some concerts happened in the years of both 2014 and 2015."

## SQL Query

The following SQL query identifies stadiums that had concerts in both specified years:

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

## Explanation of the Query

1.  **`SELECT T2.name, T2.location`**: This part specifies the columns to be retrieved from the `stadium` table (aliased as `T2`), which are the `name` and `location` of the stadiums.
2.  **`FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id`**: This performs an `INNER JOIN` between the `concert` table (aliased as `T1`) and the `stadium` table (aliased as `T2`). The join condition `T1.stadium_id = T2.stadium_id` links concerts to their respective stadiums based on the `stadium_id`.
3.  **`WHERE T1.year = 2014`**: The first `SELECT` statement filters the concerts to include only those that occurred in the year 2014.
4.  **`INTERSECT`**: This operator is used to combine the result sets of two or more `SELECT` statements. It returns only the distinct rows that are present in all result sets. In this case, it finds the stadiums (by name and location) that appear in both the 2014 concert list and the 2015 concert list.
5.  **`SELECT T2.name, T2.location FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id WHERE T1.year = 2015`**: This is the second `SELECT` statement, identical in structure to the first, but it filters for concerts that occurred in the year 2015.

By using `INTERSECT`, the query ensures that only stadiums that hosted at least one concert in 2014 AND at least one concert in 2015 are returned.

## Expected Output

The query will return a list of distinct stadium names and their corresponding locations, where each listed stadium hosted at least one concert in both 2014 and 2015.

| name | location |
| :--- | :------- |
| Stadium A | City X   |
| Stadium B | City Y   |
| ... | ... |