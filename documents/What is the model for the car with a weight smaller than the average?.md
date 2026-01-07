To find the model of cars with a weight smaller than the average weight, you can use the following SQL query. This query involves joining the `car_names` and `cars_data` tables and utilizing a subquery to calculate the average weight for comparison.

## SQL Query to Find Car Models with Below-Average Weight

```sql
SELECT
  T1.model
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

### Explanation

This query works as follows:

1.  **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id`**:
    *   It starts by joining two tables: `car_names` (aliased as `T1`) and `cars_data` (aliased as `T2`).
    *   The join condition `T1.makeid = T2.id` links car names to their detailed data based on a common identifier.

2.  **`WHERE T2.weight < (...)`**:
    *   This clause filters the results based on the `weight` column from the `cars_data` table (`T2`).
    *   It selects only those cars whose weight is less than a specific value.

3.  **`(SELECT AVG(weight) FROM cars_data)`**:
    *   This is a subquery that calculates the average `weight` of all cars present in the `cars_data` table.
    *   The result of this subquery is a single value representing the overall average car weight.

4.  **`SELECT T1.model`**:
    *   Finally, from the filtered set of cars, the query selects the `model` from the `car_names` table (`T1`).

In essence, the query first determines the average weight of all cars and then retrieves the models of those cars whose individual weight falls below this calculated average.