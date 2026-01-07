To find the model of the car with the most horsepower among all 4-cylinder cars, you would use a SQL query that joins the `car_names` and `cars_data` tables, filters for cars with 4 cylinders, orders the results by horsepower in descending order, and limits the output to the top result.

## SQL Query for Car Model with Most Horsepower (4 Cylinders)

```sql
SELECT
  T1.model
FROM car_names AS T1
INNER JOIN cars_data AS T2
  ON T1.makeid = T2.id
WHERE
  T2.cylinders = 4
ORDER BY
  T2.horsepower DESC
LIMIT 1;
```

### Explanation of the Query

1.  **`SELECT T1.model`**: This specifies that the query should return the `model` column from the `car_names` table (aliased as `T1`).
2.  **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id`**: This performs an `INNER JOIN` between the `car_names` table (aliased as `T1`) and the `cars_data` table (aliased as `T2`). The join condition `T1.makeid = T2.id` links car models to their corresponding data based on their `makeid`/`id`.
3.  **`WHERE T2.cylinders = 4`**: This clause filters the results to include only cars that have `4` cylinders.
4.  **`ORDER BY T2.horsepower DESC`**: This sorts the filtered cars in descending order based on their `horsepower` from the `cars_data` table. This puts the car with the most horsepower at the top.
5.  **`LIMIT 1`**: This restricts the output to only the first row, which will be the car model with the highest horsepower among the 4-cylinder cars.

This query will efficiently retrieve the desired car model from the database.