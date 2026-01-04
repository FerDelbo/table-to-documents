To retrieve the locations and names of all stadiums with a capacity between 5000 and 10000, you can use the following SQL query.

## Query to Find Stadiums by Capacity Range

This query selects the `location` and `name` from the `stadium` table, filtering for records where the `capacity` column falls inclusively between 5000 and 10000.

```sql
SELECT
  location,
  name
FROM stadium
WHERE
  capacity BETWEEN 5000 AND 10000;
```

### Explanation

*   **`SELECT location, name`**: This specifies the columns you want to retrieve from the database. In this case, `location` (representing where the stadium is situated) and `name` (the name of the stadium).
*   **`FROM stadium`**: This indicates that the data should be retrieved from the `stadium` table.
*   **`WHERE capacity BETWEEN 5000 AND 10000`**: This is the filtering condition.
    *   `capacity`: Refers to the column holding the stadium's capacity.
    *   `BETWEEN 5000 AND 10000`: This clause is used to filter records where the `capacity` value is greater than or equal to 5000 AND less than or equal to 10000.