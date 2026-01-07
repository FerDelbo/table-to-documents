To find the average weight of cars for each year, along with the corresponding year, you can use the following SQL query:

```sql
SELECT avg(weight), year FROM cars_data GROUP BY year
```

This query will group the car data by the `year` column and then calculate the average `weight` for all cars within each of those years.

### Explanation:

*   **`SELECT avg(weight), year`**: This specifies the columns you want to retrieve. `avg(weight)` calculates the average value of the `weight` column, and `year` is the year for which this average is computed.
*   **`FROM cars_data`**: This indicates that the data should be retrieved from the `cars_data` table.
*   **`GROUP BY year`**: This clause groups rows that have the same `year` value together. The `AVG()` aggregate function then operates on each of these groups independently.