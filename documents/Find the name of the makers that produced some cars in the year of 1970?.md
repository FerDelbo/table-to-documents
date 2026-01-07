To find the names of car makers that produced cars in the year 1970, you can use the following SQL query:

```sql
SELECT DISTINCT T1.Maker
FROM car_makers AS T1
INNER JOIN model_list AS T2
  ON T1.Id = T2.Maker
INNER JOIN car_names AS T3
  ON T2.Model = T3.Model
INNER JOIN cars_data AS T4
  ON T3.MakeId = T4.Id
WHERE
  T4.Year = 1970;
```

### Explanation

This query retrieves the names of distinct car makers who produced cars in the year 1970 by joining several tables:

1.  **`car_makers AS T1`**: This table contains information about car manufacturers, including their names.
2.  **`model_list AS T2`**: This table links car makers to their models.
3.  **`car_names AS T3`**: This table provides details about car models, including a `MakeId` which can be linked to `cars_data`.
4.  **`cars_data AS T4`**: This table holds data about cars, including their production year.

The `INNER JOIN` clauses connect these tables based on their respective IDs:
*   `T1.Id = T2.Maker`: Links car makers to their models.
*   `T2.Model = T3.Model`: Links models from the `model_list` to the `car_names` table.
*   `T3.MakeId = T4.Id`: Links car names to the car data.

The `WHERE T4.Year = 1970` clause filters the results to include only cars produced in the year 1970.

Finally, `SELECT DISTINCT T1.Maker` ensures that each car maker's name is listed only once in the result.

### Tables Involved

*   `car_makers`
*   `model_list`
*   `car_names`
*   `cars_data`