To find the weight of the youngest dog, you would query the `pets` table, ordering the results by `pet_age` in ascending order and limiting the result to one entry.

### SQL Query

```sql
SELECT weight
FROM pets
ORDER BY pet_age ASC
LIMIT 1;
```

### Explanation

*   **`SELECT weight`**: This specifies that you want to retrieve the `weight` column from the table.
*   **`FROM pets`**: This indicates that the data should be retrieved from the `pets` table.
*   **`ORDER BY pet_age ASC`**: This clause sorts the rows by the `pet_age` column in ascending order, meaning the youngest pet will appear first.
*   **`LIMIT 1`**: This restricts the output to only the first row after sorting, which corresponds to the youngest dog's weight.