To find the car model with the highest miles per gallon (MPG), you can execute a SQL query that joins the `car_names` and `cars_data` tables, orders the results by MPG in descending order, and then limits the output to the top entry.

### SQL Query

```sql
SELECT T1.Model
FROM car_names AS T1
INNER JOIN cars_data AS T2
  ON T1.MakeId = T2.Id
ORDER BY
  T2.Mpg DESC
LIMIT 1;
```

### Explanation

This query performs the following actions:

1.  **`SELECT T1.Model`**: It selects the `Model` column from the `car_names` table (aliased as `T1`). This is the desired output: the name of the car model.
2.  **`FROM car_names AS T1 JOIN cars_data AS T2 ON T1.MakeId = T2.Id`**: It joins two tables:
    *   `car_names` (aliased as `T1`): This table is expected to contain car model names and an identifier linking them to detailed car data.
    *   `cars_data` (aliased as `T2`): This table holds various car specifications, including `Mpg` (miles per gallon) and a unique `Id` for each car make.
    *   The `INNER JOIN` operation links rows from `car_names` to `cars_data` where `T1.MakeId` matches `T2.Id`, ensuring that only models with corresponding data are considered.
3.  **`ORDER BY T2.Mpg DESC`**: This clause sorts the results based on the `Mpg` value from the `cars_data` table in descending order. This places the car model with the highest MPG at the top of the result set.
4.  **`LIMIT 1`**: This clause restricts the output to only the first row after sorting, effectively giving you the single car model that has the highest MPG.

### Example Output

The query will return a single row with the name of the car model that achieves the highest miles per gallon.

| Model      |
| :--------- |
| `[CarModel]` |