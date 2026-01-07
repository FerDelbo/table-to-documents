To determine the number of cars produced in 1980, you can execute a SQL query on the `cars_data` table.

## SQL Query

```sql
SELECT count(*)
FROM cars_data
WHERE year = 1980;
```

## Explanation

This query performs the following actions:

*   **`SELECT count(*)`**: This clause counts all rows that match the specified criteria. In this context, it will count each car entry.
*   **`FROM cars_data`**: This specifies that the data will be retrieved from the `cars_data` table.
*   **`WHERE year = 1980`**: This is a filtering condition that restricts the count to only include cars where the `year` column has a value of `1980`.

## Assumed Table Schema

The query assumes the existence of a table named `cars_data` with at least the following column:

### `cars_data` Table

| Column Name | Data Type | Description                              |
| :---------- | :-------- | :--------------------------------------- |
| `year`      | INTEGER   | The year in which the car was produced.  |
| (other columns) | (various) | Other relevant data about the cars.      |

This query will return a single numerical value representing the total count of cars manufactured in the year 1980.