To find the average weight of cars for each year, you can use the following SQL query:

```sql
SELECT year, AVG(weight) AS average_weight
FROM cars_data
GROUP BY year;
```

This query will return the average weight of cars, grouped by the `year` they were produced.

## Technical Documentation: Average Car Weight by Year

This document explains how to retrieve the average weight of cars for each production year from a relational database.

### 1. Objective

The primary goal is to calculate and display the average weight of cars, categorized by their manufacturing year. This allows for an analysis of how car weights have changed over different production years.

### 2. Database Schema (Assumed relevant table)

The operation relies on a table named `cars_data` with at least the following columns:

*   `year`: Represents the manufacturing year of the car.
*   `weight`: Represents the weight of the car.

### 3. SQL Query

To achieve the objective, the following SQL query is used:

```sql
SELECT
  year,
  AVG(weight)
FROM
  cars_data
GROUP BY
  year;
```

### 4. Query Breakdown

*   **`SELECT year, AVG(weight)`**: This clause specifies the columns to be retrieved.
    *   `year`: The production year of the car. This column will be used for grouping the results.
    *   `AVG(weight)`: An aggregate function that calculates the average value of the `weight` column for each group. The alias `average_weight` could optionally be added for better readability in the output.
*   **`FROM cars_data`**: This indicates that the data will be pulled from the `cars_data` table.
*   **`GROUP BY year`**: This clause groups rows that have the same `year` value into summary rows. The `AVG(weight)` function will then operate on each of these groups independently.

### 5. Expected Output

The query will return a result set with two columns:
*   `year`: The specific year of car production.
*   `average_weight`: The calculated average weight for all cars produced in that `year`.

The results will show a distinct average weight for each unique year present in the `cars_data` table.

**Example Output (Illustrative):**

| year | AVG(weight) |
| :--- | :---------- |
| 1970 | 3000.5      |
| 1971 | 2950.2      |
| 1972 | 3100.0      |
| ...  | ...         |
| 1982 | 2600.8      |