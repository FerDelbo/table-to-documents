To determine which car model saves the most gasoline, meaning it has the maximum miles per gallon (MPG), we need to query the car data, specifically looking for the model with the highest `mpg` value.

The following SQL query achieves this by joining the `car_names` and `cars_data` tables and ordering the results by `mpg` in descending order, then taking the top result.

### SQL Query

```sql
SELECT
  T1.model
FROM car_names AS T1
JOIN cars_data AS T2
  ON T1.makeid = T2.id
ORDER BY
  T2.mpg DESC
LIMIT 1;
```

### Explanation

1.  **`SELECT T1.model`**: This selects the `model` column from the `car_names` table (aliased as `T1`). This is the desired output, representing the name of the car model.
2.  **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id`**:
    *   We start by selecting from the `car_names` table (aliased as `T1`) which contains car models and their `makeid`.
    *   We then perform an `INNER JOIN` with the `cars_data` table (aliased as `T2`). The `cars_data` table contains performance metrics like `mpg` (miles per gallon) and is linked to `car_names` via `makeid` in `car_names` and `id` in `cars_data`.
    *   The `ON T1.makeid = T2.id` clause specifies the join condition, linking car names to their respective data entries.
3.  **`ORDER BY T2.mpg DESC`**: This clause sorts the results based on the `mpg` column from the `cars_data` table in descending order. This ensures that the car model with the highest MPG appears at the top of the result set.
4.  **`LIMIT 1`**: This clause restricts the output to only the first row after sorting, which will be the car model with the maximum miles per gallon.

This query effectively identifies the single car model that offers the best fuel efficiency, thus "saving the most gasoline."