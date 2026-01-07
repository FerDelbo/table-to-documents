To retrieve the city and country for the Alton airport, you can use the following SQL query.

## SQL Query

```sql
SELECT city, country
FROM airports
WHERE airportname = 'Alton';
```

### Explanation

This query selects the `city` and `country` columns from the `airports` table. The `WHERE` clause filters the results to only include rows where the `airportname` is 'Alton'. This will return the city and country associated with the Alton airport.