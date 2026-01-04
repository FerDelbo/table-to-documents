```markdown
# Stadiums with Capacity Between 5000 and 10000

This document outlines how to retrieve the location and name of stadiums that have a seating capacity between 5000 and 10000 (inclusive).

## SQL Query

To obtain the desired information, you can use the following SQL query:

```sql
SELECT location, name
FROM stadium
WHERE capacity BETWEEN 5000 AND 10000;
```

### Explanation

*   **SELECT location, name**: This specifies that the query should return the `location` and `name` columns from the `stadium` table.
*   **FROM stadium**: This indicates that the data will be retrieved from the `stadium` table.
*   **WHERE capacity BETWEEN 5000 AND 10000**: This is the filtering condition. It restricts the results to only include stadiums where the `capacity` column's value is greater than or equal to 5000 and less than or equal to 10000.

## Example

Assuming a `stadium` table with the following structure and data:

| stadium_id | name        | capacity | location       | average |
| :--------- | :---------- | :------- | :------------- | :------ |
| 1          | Grand Arena | 12000    | City A         | 10000   |
| 2          | Town Field  | 7500     | City B         | 6000    |
| 3          | Sports Dome | 4000     | City C         | 3500    |
| 4          | River Park  | 9800     | City D         | 9000    |
| 5          | Small Venue | 2500     | City E         | 2000    |

Executing the query would yield the following results:

| location | name       |
| :------- | :--------- |
| City B   | Town Field |
| City D   | River Park |
```