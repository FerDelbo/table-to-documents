To retrieve the name, country, and age of all singers, ordered from the oldest to the youngest, you can use the following SQL query.

## SQL Query for Singers Ordered by Age

### Purpose
This query is designed to list all singers, displaying their name, country of origin, and age. The results are presented in descending order of age, meaning the oldest singers will appear first.

### SQL Query
```sql
SELECT name, country, age
FROM singer
ORDER BY age DESC;
```

### Explanation
*   `SELECT name, country, age`: This clause specifies the columns to be retrieved from the database. It selects the singer's name, their country, and their age.
*   `FROM singer`: This indicates that the data will be retrieved from the `singer` table.
*   `ORDER BY age DESC`: This clause sorts the result set. `age` is the column used for sorting, and `DESC` (descending) ensures that the oldest singers (those with the highest age values) are listed first.

### Tables Involved
*   `singer`: This table is assumed to contain information about individual singers, including their `name`, `country`, and `age`.