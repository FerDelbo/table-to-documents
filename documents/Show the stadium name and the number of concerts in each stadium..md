The following document provides a SQL query and an explanation to retrieve the stadium name and the corresponding number of concerts held in each stadium.

## SQL Query for Stadium Concert Counts

### 1. Question

Show the stadium name and the number of concerts in each stadium.

### 2. SQL Query

```sql
SELECT T2.name, COUNT(*)
FROM concert AS T1
JOIN stadium AS T2
  ON T1.stadium_id = T2.stadium_id
GROUP BY T1.stadium_id;
```

### 3. Explanation

This SQL query is designed to count the number of concerts hosted by each stadium and display the stadium's name alongside this count.

#### 3.1. Query Purpose

The primary goal of this query is to provide an aggregated view of concert activity per stadium. It identifies each unique stadium that has hosted at least one concert and reports how many concerts each of them hosted.

#### 3.2. Tables Involved

*   **`concert` (aliased as `T1`)**: This table likely contains information about individual concerts, including a `stadium_id` to link to the stadium where the concert took place.
*   **`stadium` (aliased as `T2`)**: This table holds details about the stadiums, including their `stadium_id` and `name`.

#### 3.3. Join Operation

*   `JOIN stadium AS T2 ON T1.stadium_id = T2.stadium_id`: This clause connects the `concert` table (`T1`) with the `stadium` table (`T2`). The join condition `T1.stadium_id = T2.stadium_id` ensures that concerts are matched with their respective stadiums based on a common stadium identifier. This linkage is crucial to associate concert events with stadium names.

#### 3.4. Aggregation and Grouping

*   `COUNT(*)`: This aggregate function counts all rows within each group. In this context, it counts the number of concerts.
*   `GROUP BY T1.stadium_id`: This clause groups the rows from the joined tables based on the `stadium_id` from the `concert` table. This means that the `COUNT(*)` function will calculate the number of concerts for each unique `stadium_id`. Since `T1.stadium_id` is joined with `T2.stadium_id`, grouping by `T1.stadium_id` effectively groups by each unique stadium.

#### 3.5. Selection

*   `SELECT T2.name, COUNT(*)`: This selects two pieces of information for the final output:
    *   `T2.name`: The name of the stadium, retrieved from the `stadium` table (`T2`).
    *   `COUNT(*)`: The total count of concerts associated with that particular stadium, as calculated by the aggregation.

#### 3.6. Output

The query will return a result set with two columns:
*   **`name`**: The name of a stadium.
*   **`COUNT(*)`**: The total number of concerts held at that specific stadium.

Each row in the result will represent a unique stadium that has hosted concerts, along with its corresponding concert count.