To find the weight of the youngest dog, you can use the following SQL query:

```sql
SELECT weight FROM pets ORDER BY pet_age LIMIT 1
```

### Explanation

This query works as follows:

1.  **`SELECT weight`**: This specifies that you want to retrieve the `weight` column from the table.
2.  **`FROM pets`**: This indicates that the data should be retrieved from the `pets` table.
3.  **`ORDER BY pet_age`**: This sorts the rows of the `pets` table based on the `pet_age` column in ascending order (default behavior for `ORDER BY`), meaning the youngest pets will appear first.
4.  **`LIMIT 1`**: This restricts the result set to only the first row after sorting, which corresponds to the youngest dog (or one of the youngest if there are multiple with the same minimum age).