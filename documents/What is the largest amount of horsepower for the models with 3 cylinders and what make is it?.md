The following Markdown document provides the SQL query to find the largest amount of horsepower for car models with 3 cylinders and the corresponding make.

```markdown
# Car Models with Maximum Horsepower for 3 Cylinders

This document details how to retrieve the car make and the largest horsepower value for car models that specifically have 3 cylinders.

## SQL Query

To identify the make and maximum horsepower for cars with 3 cylinders, you can use the following SQL query:

```sql
SELECT
  T2.horsepower,
  T1.make
FROM car_names AS T1
JOIN cars_data AS T2
  ON T1.makeid = T2.id
WHERE
  T2.cylinders = 3
ORDER BY
  T2.horsepower DESC
LIMIT 1;
```

### Query Explanation

*   **`SELECT T2.horsepower, T1.make`**: This selects the `horsepower` from the `cars_data` table (aliased as `T2`) and the `make` from the `car_names` table (aliased as `T1`).
*   **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id`**: This performs an inner join between the `car_names` table and the `cars_data` table. The join condition `T1.makeid = T2.id` links car names to their corresponding data entries.
*   **`WHERE T2.cylinders = 3`**: This filters the results to include only cars that have exactly 3 cylinders.
*   **`ORDER BY T2.horsepower DESC`**: This sorts the filtered results in descending order based on the `horsepower` value, placing the highest horsepower first.
*   **`LIMIT 1`**: This restricts the output to only the first row, which will be the car model with the maximum horsepower among those with 3 cylinders.

This query effectively isolates the car model with 3 cylinders that possesses the highest horsepower, providing both the horsepower value and the car's make.
```