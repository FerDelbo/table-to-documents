The question "How many cars have more than 4 cylinders?" can be answered by querying the `cars_data` table and filtering for records where the `cylinders` column has a value greater than 4, then counting the resulting rows.

The SQL query to achieve this is:

```sql
SELECT count(*) FROM cars_data WHERE cylinders > 4;
```

### Explanation:

*   **`SELECT count(*)`**: This part of the query counts the total number of rows that satisfy the conditions specified in the `WHERE` clause.
*   **`FROM cars_data`**: This indicates that the query will retrieve data from the `cars_data` table.
*   **`WHERE cylinders > 4`**: This is the filtering condition. It restricts the count to only include cars that have more than 4 cylinders.