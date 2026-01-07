To find the type and weight of the youngest pet, you can use the following SQL query:

```sql
SELECT pettype, weight
FROM pets
ORDER BY pet_age
LIMIT 1;
```

### Explanation

This query works as follows:

1.  **`FROM pets`**: Specifies that we are querying the `pets` table.
2.  **`ORDER BY pet_age`**: Sorts the records in the `pets` table based on the `pet_age` column in ascending order. This places the youngest pet's record at the top.
3.  **`LIMIT 1`**: Restricts the output to only the first row after sorting, which corresponds to the youngest pet.
4.  **`SELECT pettype, weight`**: Selects the `pettype` and `weight` columns for that youngest pet.