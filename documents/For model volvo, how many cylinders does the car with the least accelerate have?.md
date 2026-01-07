To determine the number of cylinders for the 'volvo' car model with the least acceleration, you can use the following SQL query:

```sql
SELECT T1.Cylinders
FROM Cars_Data AS T1
INNER JOIN Car_Names AS T2
  ON T1.Id = T2.MakeId
WHERE
  T2.Model = 'volvo'
ORDER BY
  T1.Accelerate ASC
LIMIT 1;
```

### Explanation

This query performs the following steps:

1.  **`SELECT T1.Cylinders`**: It selects the `Cylinders` column from the `Cars_Data` table (aliased as `T1`), which represents the number of cylinders in the car.
2.  **`FROM Cars_Data AS T1 INNER JOIN Car_Names AS T2 ON T1.Id = T2.MakeId`**: It joins the `Cars_Data` table with the `Car_Names` table (aliased as `T2`) using their respective `Id` and `MakeId` columns. This join is necessary to link car data (like acceleration and cylinders) with car names and models.
3.  **`WHERE T2.Model = 'volvo'`**: This clause filters the results to only include entries where the car's model name is 'volvo'.
4.  **`ORDER BY T1.Accelerate ASC`**: It sorts the filtered results in ascending order based on the `Accelerate` column from the `Cars_Data` table. This ensures that the car with the *least* acceleration appears first.
5.  **`LIMIT 1`**: This restricts the output to only the top row, effectively giving you the number of cylinders for the 'volvo' model with the lowest acceleration.