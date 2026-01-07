The following document provides the SQL query to find the model of cars whose weight is below the average weight.

***

# Find Car Models Below Average Weight

## Question

Find the model of the car whose weight is below the average weight.

## SQL Query

To retrieve the models of cars that have a weight less than the average weight of all cars, you can use the following SQL query:

```sql
SELECT T1.model
FROM car_names AS T1
JOIN cars_data AS T2
  ON T1.makeid = T2.id
WHERE
  T2.weight < (
    SELECT
      AVG(weight)
    FROM cars_data
  );
```

## Explanation

The query involves a join between the `car_names` and `cars_data` tables and a subquery to calculate the average weight.

1.  **`SELECT T1.model FROM car_names AS T1`**:
    *   This specifies that we want to retrieve the `model` column from the `car_names` table.
    *   `T1` is an alias given to the `car_names` table for brevity.

2.  **`JOIN cars_data AS T2 ON T1.makeid = T2.id`**:
    *   This joins the `car_names` table (aliased as `T1`) with the `cars_data` table (aliased as `T2`).
    *   The join condition `T1.makeid = T2.id` links car models to their corresponding car data based on their unique identifiers.

3.  **`WHERE T2.weight < (SELECT AVG(weight) FROM cars_data)`**:
    *   This is the filtering condition.
    *   A subquery `(SELECT AVG(weight) FROM cars_data)` calculates the average `weight` from the `cars_data` table.
    *   The outer query then selects only those car models where the `weight` (from `cars_data`, aliased as `T2`) is strictly less than this calculated average weight.

This query effectively identifies all car models that are lighter than the overall average weight of cars in the dataset.