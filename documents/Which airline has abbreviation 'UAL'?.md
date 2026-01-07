To find out which airline has the abbreviation 'UAL', you can query the `airlines` table.

```sql
SELECT airline
FROM airlines
WHERE abbreviation = 'UAL';
```

### Explanation

This SQL query performs the following actions:

*   **`SELECT airline`**: This specifies that you want to retrieve the `airline` name.
*   **`FROM airlines`**: This indicates that the data should be fetched from the `airlines` table.
*   **`WHERE abbreviation = 'UAL'`**: This is the filtering condition. It ensures that only rows where the `abbreviation` column has a value of 'UAL' are considered.