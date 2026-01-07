The following document provides the SQL query to determine the maximum miles per gallon (MPG) for cars with 8 cylinders or those produced before 1980.

## Query for Maximum MPG of Cars with Specific Criteria

To find the maximum miles per gallon (MPG) among cars that either have 8 cylinders or were produced before the year 1980, you can use the SQL query provided below. This query targets the `cars_data` table and applies a conditional filter before calculating the maximum MPG.

### SQL Query

```sql
SELECT MAX(mpg)
FROM cars_data
WHERE cylinders = 8 OR year < 1980;
```

### Explanation

*   **`SELECT MAX(mpg)`**: This clause specifies that the query should return the highest value found in the `mpg` column.
*   **`FROM cars_data`**: This indicates that the data will be retrieved from the `cars_data` table.
*   **`WHERE cylinders = 8 OR year < 1980`**: This is the filtering condition. It includes rows where:
    *   The `cylinders` column has a value of `8`.
    *   **OR**
    *   The `year` column has a value less than `1980`.
    The `OR` operator ensures that a car's MPG is considered if it meets *at least one* of these two conditions.

### Database Table

The query primarily interacts with the `cars_data` table.

#### `cars_data` Table

This table is expected to contain information about various car models, including:

*   `mpg`: Miles per gallon (fuel efficiency).
*   `cylinders`: The number of cylinders in the car's engine.
*   `year`: The production year of the car.
*   Other relevant car specifications.