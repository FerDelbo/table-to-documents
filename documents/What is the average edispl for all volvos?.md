```markdown
# Average Edispl for Volvo Cars

This document provides the SQL query to calculate the average engine displacement (edispl) for all cars of the 'Volvo' model.

## SQL Query

To find the average engine displacement for all Volvo cars, you would execute the following SQL query:

```sql
SELECT
  AVG(T2.edispl)
FROM car_names AS T1
JOIN cars_data AS T2
  ON T1.makeid = T2.id
WHERE
  T1.model = 'volvo';
```

## Explanation

The query performs the following steps to arrive at the desired result:

1.  **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id`**: This part of the query joins two tables: `car_names` (aliased as `T1`) and `cars_data` (aliased as `T2`). The join is performed on the `makeid` column from the `car_names` table and the `id` column from the `cars_data` table. This linkage is crucial because `car_names` likely contains the `model` information, while `cars_data` contains the `edispl` (engine displacement) attribute and links to the car make.

2.  **`WHERE T1.model = 'volvo'`**: This `WHERE` clause filters the joined results to include only those records where the car's model, found in the `car_names` table (`T1.model`), is 'volvo'. This ensures that only Volvo cars are considered for the calculation.

3.  **`SELECT AVG(T2.edispl)`**: Finally, the `SELECT` statement calculates the average of the `edispl` column (engine displacement) from the `cars_data` table (`T2.edispl`) for all the filtered 'Volvo' cars.

This query effectively retrieves the average engine displacement specifically for cars identified as 'Volvo' models by joining the relevant car information tables.
```