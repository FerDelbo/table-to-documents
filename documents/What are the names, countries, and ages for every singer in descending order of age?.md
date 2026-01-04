To retrieve the names, countries, and ages for every singer, ordered by age from the oldest to the youngest, you can use the following SQL query:

```sql
SELECT name, country, age
FROM singer
ORDER BY age DESC;
```

### Explanation

*   **`SELECT name, country, age`**: This specifies the columns you want to retrieve from the `singer` table.
    *   `name`: The name of the singer.
    *   `country`: The country of origin for the singer.
    *   `age`: The age of the singer.
*   **`FROM singer`**: This indicates that the data should be fetched from the `singer` table.
*   **`ORDER BY age DESC`**: This clause sorts the results based on the `age` column in descending order (`DESC`), meaning the oldest singers will appear first in the list.