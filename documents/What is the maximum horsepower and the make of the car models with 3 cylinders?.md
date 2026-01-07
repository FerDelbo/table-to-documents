```markdown
# Car Models with Maximum Horsepower and 3 Cylinders

This document provides the SQL query to retrieve the make and maximum horsepower of car models that have 3 cylinders.

## SQL Query

To find the maximum horsepower and the make of car models equipped with 3 cylinders, you can use the following SQL query:

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

### Explanation

*   **`SELECT T2.horsepower, T1.make`**: This selects the `horsepower` from the `cars_data` table (aliased as `T2`) and the `make` from the `car_names` table (aliased as `T1`).
*   **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id`**: This specifies that we are joining the `car_names` table with the `cars_data` table. The join condition `T1.makeid = T2.id` links car names to their corresponding data entries.
*   **`WHERE T2.cylinders = 3`**: This filters the results to include only cars that have `3` cylinders.
*   **`ORDER BY T2.horsepower DESC`**: This sorts the filtered results in descending order based on their `horsepower`, so the car with the highest horsepower appears first.
*   **`LIMIT 1`**: This restricts the output to only the top row, effectively giving us the car with the maximum horsepower among those with 3 cylinders.

This query will return a single row containing the make and the maximum horsepower for a 3-cylinder car model.
```