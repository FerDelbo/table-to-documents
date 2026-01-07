This document provides the SQL query to find the average 'edispl' of cars for the model 'volvo'.

## Query for Average Edispl of Volvo Cars

To determine the average 'edispl' (engine displacement) for cars of the 'volvo' model, you can use the following SQL query. This query joins the `car_names` table with the `cars_data` table to link car models with their performance data and then calculates the average 'edispl' for the specified model.

### SQL Query

```sql
SELECT
  avg(T2.edispl)
FROM car_names AS T1
JOIN cars_data AS T2
  ON T1.makeid = T2.id
WHERE
  T1.model = 'volvo';
```

### Explanation

*   **`SELECT avg(T2.edispl)`**: This clause specifies that we want to calculate the average value of the `edispl` column. `T2` is an alias for the `cars_data` table.
*   **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id`**: This part of the query performs an inner join between two tables:
    *   `car_names` (aliased as `T1`), which likely contains information about car models and their `makeid`.
    *   `cars_data` (aliased as `T2`), which contains detailed car data including `edispl` and `id` (which corresponds to `makeid`).
    *   The join condition `T1.makeid = T2.id` links records from both tables based on their respective identification columns.
*   **`WHERE T1.model = 'volvo'`**: This `WHERE` clause filters the results to only include records where the `model` column in the `car_names` table (aliased as `T1`) is exactly 'volvo'. This ensures that the average 'edispl' is calculated specifically for Volvo cars.