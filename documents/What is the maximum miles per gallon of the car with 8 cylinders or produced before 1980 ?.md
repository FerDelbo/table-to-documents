```markdown
# Maximum Miles Per Gallon for Cars with 8 Cylinders or Produced Before 1980

To find the maximum miles per gallon (MPG) for cars that either have 8 cylinders or were produced before 1980, you can use a SQL query that leverages the `MAX()` aggregate function and a `WHERE` clause with an `OR` condition.

## SQL Query

```sql
SELECT
  MAX(mpg)
FROM cars_data
WHERE
  cylinders = 8 OR year < 1980;
```

### Explanation

*   **`SELECT MAX(mpg)`**: This part of the query specifies that we want to retrieve the highest value from the `mpg` (miles per gallon) column.
*   **`FROM cars_data`**: This indicates that the data will be retrieved from the `cars_data` table.
*   **`WHERE cylinders = 8 OR year < 1980`**: This is the filtering condition.
    *   `cylinders = 8`: This condition selects cars that have exactly 8 cylinders.
    *   `OR`: This logical operator combines the two conditions. If a car satisfies *either* the 8-cylinder condition *or* the year before 1980 condition, it will be included in the dataset for which the maximum MPG is calculated.
    *   `year < 1980`: This condition selects cars that were produced in any year prior to 1980.

This query will return a single value representing the highest MPG found among all cars that meet at least one of the specified criteria.
```