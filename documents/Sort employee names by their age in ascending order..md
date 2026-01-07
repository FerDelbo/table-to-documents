To sort employee names by their age in ascending order, you would use the following SQL query:

```sql
SELECT name FROM employee ORDER BY age ASC;
```

## Explanation

This query is structured to retrieve specific information (`name`) from the `employee` table and arrange the results based on the `age` column.

*   **`SELECT name`**: This clause specifies that you want to retrieve the `name` column from the table.
*   **`FROM employee`**: This indicates that the data should be fetched from the `employee` table.
*   **`ORDER BY age ASC`**: This is the crucial part for sorting.
    *   `ORDER BY age`: This command tells the database to sort the results based on the values in the `age` column.
    *   `ASC`: This keyword (short for "ascending") ensures that the sorting is done from the youngest age to the oldest. If `ASC` is omitted, `ORDER BY` defaults to ascending order in many SQL databases, but it's good practice to include it for clarity.

This query will return a list of all employee names, with the employee with the lowest age appearing first, and the employee with the highest age appearing last.