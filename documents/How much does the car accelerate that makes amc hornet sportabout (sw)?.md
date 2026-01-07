```markdown
# SQL Query for Car Acceleration by Make

This document provides the SQL query to determine the acceleration of a car given its make, along with an explanation of the query and the tables involved.

## The Question

How much does the car accelerate that makes amc hornet sportabout (sw)?

## SQL Query

```sql
SELECT T1.Accelerate
FROM Cars_Data AS T1
INNER JOIN Car_Names AS T2
  ON T1.Id = T2.MakeId
WHERE
  T2.Make = 'amc hornet sportabout (sw)';
```

## Explanation

This query retrieves the `Accelerate` value for a specific car model.

1.  **`SELECT T1.Accelerate`**: This selects the `Accelerate` column from the `Cars_Data` table (aliased as `T1`).
2.  **`FROM Cars_Data AS T1 INNER JOIN Car_Names AS T2 ON T1.Id = T2.MakeId`**: This performs an `INNER JOIN` between the `Cars_Data` table (`T1`) and the `Car_Names` table (`T2`). The join condition `T1.Id = T2.MakeId` links car data to its corresponding name and make information.
3.  **`WHERE T2.Make = 'amc hornet sportabout (sw)'`**: This filters the results to include only those records where the `Make` column in the `Car_Names` table (`T2`) matches 'amc hornet sportabout (sw)'.

## Involved Tables

The query interacts with two tables:

*   **`Cars_Data`**: Contains detailed specifications about cars, including their acceleration (`Accelerate`) and a unique identifier (`Id`).
*   **`Car_Names`**: Stores information about car models, including the car's make (`Make`) and a `MakeId` that links to the `Id` in the `Cars_Data` table.

### Relevant Columns

*   **`Cars_Data.Accelerate`**: The acceleration value of the car.
*   **`Cars_Data.Id`**: The primary key for the `Cars_Data` table, used to link with `Car_Names`.
*   **`Car_Names.Make`**: The specific make or model name of the car.
*   **`Car_Names.MakeId`**: A foreign key referencing `Cars_Data.Id`, establishing the relationship between car names and their data.
```