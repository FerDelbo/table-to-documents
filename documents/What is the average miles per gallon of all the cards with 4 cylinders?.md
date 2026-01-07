```markdown
# Average Miles Per Gallon for Cars with 4 Cylinders

To determine the average miles per gallon (MPG) for all cars equipped with 4 cylinders, you would query the `cars_data` table, filtering for records where the `cylinders` column equals 4 and then calculating the average of the `mpg` column.

## SQL Query

```sql
SELECT avg (mpg) FROM cars_data WHERE cylinders = 4
```

### Explanation

*   **`SELECT avg (mpg)`**: This part of the query calculates the average value of the `mpg` (miles per gallon) column.
*   **`FROM cars_data`**: This specifies that the data should be retrieved from the `cars_data` table.
*   **`WHERE cylinders = 4`**: This is a filtering condition that restricts the calculation to only include cars that have exactly 4 cylinders.

This query will return a single numerical value representing the average miles per gallon for all 4-cylinder cars in the dataset.
```