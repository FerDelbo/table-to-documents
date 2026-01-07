To find out which city and country the Alton airport is located in, you can use the following SQL query. This query selects the `city` and `country` columns from the `airports` table, filtering for records where the `airportname` is 'Alton airport'.

```sql
SELECT city, country
FROM airports
WHERE airportname = 'Alton airport';
```

### Explanation

*   **`SELECT city, country`**: This specifies that you want to retrieve the values from the `city` and `country` columns.
*   **`FROM airports`**: This indicates that the data should be fetched from the `airports` table.
*   **`WHERE airportname = 'Alton airport'`**: This is the filtering condition. It ensures that only rows where the `airportname` column exactly matches 'Alton airport' are considered.

Executing this query against your database will return the city and country associated with the Alton airport.