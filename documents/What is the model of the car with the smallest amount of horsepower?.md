To find the model of the car with the smallest amount of horsepower, you can use the following SQL query:

```sql
SELECT T1.model FROM car_names AS T1 JOIN cars_data AS T2 ON T1.makeid = T2.id ORDER BY T2.horsepower ASC LIMIT 1
```

### Explanation

This query works by:
1.  **Joining** the `car_names` table (aliased as `T1`) with the `cars_data` table (aliased as `T2`) on their respective ID columns (`T1.makeid = T2.id`). This links car models to their performance data, including horsepower.
2.  **Ordering** the results by the `horsepower` column from the `cars_data` table in `ASC`ending order. This puts the cars with the lowest horsepower at the top of the result set.
3.  **Limiting** the result to `1` row, which retrieves only the top entry after sorting, effectively giving you the car model with the smallest horsepower.
4.  **Selecting** the `model` column from the `car_names` table (`T1.model`) to display the name of the car model.