```markdown
# Pet Information by Age

This document provides a SQL query to retrieve the ID and weight of all pets that are older than 1 year.

## SQL Query

To find the `petid` and `weight` of pets whose age is greater than 1, execute the following SQL query:

```sql
SELECT petid, weight FROM pets WHERE pet_age > 1
```

### Explanation

*   `SELECT petid, weight`: This specifies the columns you want to retrieve from the database. In this case, `petid` (pet's identification number) and `weight` (pet's weight).
*   `FROM pets`: This indicates that the data should be retrieved from the `pets` table.
*   `WHERE pet_age > 1`: This is the filtering condition. It ensures that only rows where the `pet_age` column has a value strictly greater than 1 are included in the result set.

## Example

Assuming a `pets` table with the following structure and data:

| petid | pet_age | weight | pettype |
| :---- | :------ | :----- | :------ |
| 101   | 2       | 15     | Dog     |
| 102   | 0       | 2      | Cat     |
| 103   | 5       | 30     | Dog     |
| 104   | 1       | 8      | Bird    |
| 105   | 3       | 10     | Cat     |

Running the query would yield:

| petid | weight |
| :---- | :----- |
| 101   | 15     |
| 103   | 30     |
| 105   | 10     |
```