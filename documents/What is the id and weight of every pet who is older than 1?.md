To retrieve the ID and weight of every pet older than 1, you can use the following SQL query.

# Pet Information for Pets Older Than 1

## SQL Query

```sql
SELECT petid, weight
FROM pets
WHERE pet_age > 1;
```

## Explanation

This query is designed to select specific information about pets that meet a certain age criterion.

*   **`SELECT petid, weight`**: This clause specifies the columns you want to retrieve from the database.
    *   `petid`: Represents the unique identifier for each pet.
    *   `weight`: Represents the weight of each pet.
*   **`FROM pets`**: This indicates that the data will be retrieved from the `pets` table. This table is assumed to contain information about various pets, including their ID, weight, and age.
*   **`WHERE pet_age > 1`**: This is the filtering condition. It ensures that only rows (pets) where the value in the `pet_age` column is greater than 1 are included in the result set. This effectively filters for all pets who are older than one year.