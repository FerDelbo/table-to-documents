To find the model of the car with the minimum horsepower, you can use the following SQL query:

```sql
SELECT T1.model
FROM car_names AS T1
JOIN cars_data AS T2
  ON T1.makeid = T2.id
ORDER BY
  T2.horsepower ASC
LIMIT 1;
```

### Explanation

1.  **`SELECT T1.model`**: This specifies that we want to retrieve the `model` column from the `car_names` table (aliased as `T1`).
2.  **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id`**: This performs an inner join between the `car_names` table and the `cars_data` table.
    *   `car_names` (aliased as `T1`) likely contains car models and their `makeid`.
    *   `cars_data` (aliased as `T2`) likely contains car data including `horsepower` and `id` (which corresponds to `makeid` in `car_names`).
    *   The `JOIN` condition `T1.makeid = T2.id` links cars to their specific data.
3.  **`ORDER BY T2.horsepower ASC`**: This clause sorts the results in ascending order based on the `horsepower` column from the `cars_data` table (`T2`). This places the car with the lowest horsepower at the top.
4.  **`LIMIT 1`**: This restricts the output to only the first row, which, after sorting, will be the car model with the minimum horsepower.