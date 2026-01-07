To find the average horsepower of cars produced before 1980, you can use the following SQL query:

```sql
SELECT avg(horsepower) FROM cars_data WHERE year < 1980
```

### Explanation

This query performs the following actions:

*   **`SELECT avg(horsepower)`**: This clause specifies that we want to calculate the average value of the `horsepower` column.
*   **`FROM cars_data`**: This indicates that the data for the calculation should be retrieved from the `cars_data` table.
*   **`WHERE year < 1980`**: This is a filtering condition that restricts the rows considered for the average calculation to only those cars whose `year` of production is earlier than 1980.