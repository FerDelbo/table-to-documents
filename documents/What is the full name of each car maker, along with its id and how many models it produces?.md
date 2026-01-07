This document provides the SQL query and an explanation for retrieving the full name of each car maker, their ID, and the number of models each produces.

## Question

What is the full name of each car maker, along with its id and how many models it produces?

## SQL Query

```sql
SELECT
  T1.fullname,
  T1.id,
  COUNT(*)
FROM car_makers AS T1
JOIN model_list AS T2
  ON T1.id = T2.maker
GROUP BY
  T1.id;
```

## Explanation

This query is designed to retrieve information about car makers and the number of models they produce by joining the `car_makers` and `model_list` tables.

### Tables Involved

*   **`car_makers` (aliased as `T1`)**: This table presumably stores information about the car manufacturers.
    *   `id`: A unique identifier for each car maker.
    *   `fullname`: The full name of the car maker.
*   **`model_list` (aliased as `T2`)**: This table likely contains a list of car models, with a reference to the maker.
    *   `maker`: A foreign key linking to the `id` in the `car_makers` table.

### Query Breakdown

1.  **`SELECT T1.fullname, T1.id, COUNT(*)`**:
    *   `T1.fullname`: Selects the full name of the car maker from the `car_makers` table.
    *   `T1.id`: Selects the unique ID of the car maker from the `car_makers` table.
    *   `COUNT(*)`: This aggregate function counts the total number of rows (models) associated with each car maker after the join and grouping.

2.  **`FROM car_makers AS T1`**:
    *   Specifies that the primary data source for the query is the `car_makers` table, which is given the alias `T1` for brevity.

3.  **`JOIN model_list AS T2 ON T1.id = T2.maker`**:
    *   Performs an `INNER JOIN` between `car_makers` (`T1`) and `model_list` (`T2`).
    *   The `ON T1.id = T2.maker` clause specifies the join condition, linking car makers to their respective models using their unique IDs. This ensures that only models with an associated car maker are considered.

4.  **`GROUP BY T1.id`**:
    *   This clause groups the rows based on the `id` of the car maker.
    *   The `COUNT(*)` function then counts the number of models for each distinct `car_makers.id` within these groups. Since `T1.id` is unique for each car maker, grouping by it effectively counts models per car maker.

This query will return a result set with three columns: the full name of the car maker, their ID, and the total count of models they produce.