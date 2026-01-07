```markdown
# Car Maker and Production Year of the Earliest Produced Car

This document provides the SQL query to identify the maker and production year of the car that was produced in the earliest recorded year.

## SQL Query

To find the maker and the production year of the car produced in the earliest year, you can use the following SQL query:

```sql
SELECT T2.Make ,  T1.Year
FROM cars_data AS T1
JOIN car_names AS T2
  ON T1.Id  =  T2.MakeId
WHERE T1.Year  =  (
  SELECT min(Year)
  FROM cars_data
);
```

### Explanation

1.  **`SELECT T2.Make , T1.Year`**: This specifies the columns we want to retrieve: the `Make` (maker) from the `car_names` table and the `Year` from the `cars_data` table.
2.  **`FROM cars_data AS T1 JOIN car_names AS T2 ON T1.Id = T2.MakeId`**: This performs an `INNER JOIN` between the `cars_data` table (aliased as `T1`) and the `car_names` table (aliased as `T2`). The join condition `T1.Id = T2.MakeId` links car data records to their corresponding car names/makers.
3.  **`WHERE T1.Year = (SELECT min(Year) FROM cars_data)`**: This is the crucial filtering condition.
    *   The subquery `SELECT min(Year) FROM cars_data` finds the absolute earliest `Year` present in the `cars_data` table.
    *   The outer query then filters the joined results to include only those cars whose `Year` matches this minimum year.

This query effectively retrieves the manufacturer and year for all cars associated with the earliest production year available in the dataset.
```