The following document provides the SQL query to list the maximum weight and type for each type of pet, along with an explanation of the query.

```markdown
# List Maximum Weight and Type for Each Pet Type

This document provides the SQL query to retrieve the maximum weight for each distinct pet type from the `pets` table.

## SQL Query

To achieve this, you need to select the maximum `weight` and the `pettype` from the `pets` table, grouping the results by `pettype`.

```sql
SELECT MAX(weight), pettype
FROM pets
GROUP BY pettype;
```

## Explanation

*   **`SELECT MAX(weight), pettype`**: This specifies the columns to be retrieved.
    *   `MAX(weight)`: This aggregate function calculates the highest weight for each group.
    *   `pettype`: This column indicates the type of pet.
*   **`FROM pets`**: This indicates that the data will be retrieved from the `pets` table.
*   **`GROUP BY pettype`**: This clause groups rows that have the same `pettype` together. The `MAX(weight)` function then operates on each of these groups independently, returning the maximum weight for each unique pet type.

## Example Usage

If your `pets` table contained data like this:

| petid | pet_age | pettype | weight |
| :---- | :------ | :------ | :----- |
| 1     | 2       | Dog     | 15     |
| 2     | 3       | Cat     | 5      |
| 3     | 1       | Dog     | 10     |
| 4     | 4       | Bird    | 0.5    |
| 5     | 2       | Cat     | 7      |
| 6     | 5       | Dog     | 20     |

Executing the query would yield a result similar to:

| MAX(weight) | pettype |
| :---------- | :------ |
| 20          | Dog     |
| 7           | Cat     |
| 0.5         | Bird    |
```