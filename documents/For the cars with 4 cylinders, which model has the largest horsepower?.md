```markdown
# Car Model with Largest Horsepower (4 Cylinders)

To find the car model with the largest horsepower among cars equipped with 4 cylinders, you can execute a SQL query that joins the `car_names` and `cars_data` tables, filters for 4-cylinder cars, and then orders the results by horsepower in descending order, taking only the top entry.

## SQL Query

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

### Explanation of the Query:

*   **`SELECT T1.model`**: This selects the `model` of the car from the `car_names` table (aliased as `T1`).
*   **`FROM car_names AS T1 INNER JOIN cars_data AS T2 ON T1.makeid = T2.id`**: This performs an inner join between the `car_names` table (`T1`) and the `cars_data` table (`T2`). The join condition `T1.makeid = T2.id` links car models to their corresponding car data based on their unique identifiers.
*   **`WHERE T2.cylinders = 4`**: This filters the results to include only cars that have 4 cylinders.
*   **`ORDER BY T2.horsepower DESC`**: This sorts the filtered cars in descending order based on their `horsepower` value, placing the car with the highest horsepower at the top.
*   **`LIMIT 1`**: This restricts the output to only the first row after sorting, effectively giving us the car model with the largest horsepower among the 4-cylinder vehicles.

## Example

Assuming you have a database with the specified tables and data, running this query will return the model name of the 4-cylinder car that boasts the highest horsepower.

For instance, if your data includes:

| makeid | model           |
| :----- | :-------------- |
| 1      | Toyota Corolla  |
| 2      | Honda Civic     |
| 3      | Ford Focus      |

And `cars_data` includes:

| id | cylinders | horsepower |
| :-- | :-------- | :--------- |
| 1  | 4         | 90         |
| 2  | 4         | 110        |
| 3  | 4         | 100        |

The query would identify the 'Honda Civic' as the model with the largest horsepower (110) among the 4-cylinder cars.
```