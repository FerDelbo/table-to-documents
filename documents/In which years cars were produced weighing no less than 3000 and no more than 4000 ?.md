To determine the years in which cars were produced weighing no less than 3000 and no more than 4000 units, you can execute a SQL query against the `cars_data` table.

## SQL Query to Find Production Years for Cars Within a Specific Weight Range

The following SQL query identifies the distinct production years for cars that have a weight between 3000 and 4000 (inclusive).

```sql
SELECT DISTINCT year
FROM cars_data
WHERE weight BETWEEN 3000 AND 4000;
```

### Explanation

*   **`SELECT DISTINCT year`**: This clause specifies that we want to retrieve the unique values from the `year` column. Using `DISTINCT` ensures that each year is listed only once, even if multiple cars from that year fall within the specified weight range.
*   **`FROM cars_data`**: This indicates that the data will be retrieved from the `cars_data` table, which presumably contains information about various cars, including their production year and weight.
*   **`WHERE weight BETWEEN 3000 AND 4000`**: This is the filtering condition. It restricts the results to only include rows where the `weight` column's value is greater than or equal to 3000 and less than or equal to 4000. This directly addresses the requirement of "weighing no less than 3000 and no more than 4000".

## How to Use

To get the desired information, simply run this SQL query against your database containing the `cars_data` table. The output will be a list of years where cars meeting the weight criteria were manufactured.