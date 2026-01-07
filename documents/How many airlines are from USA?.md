To find out how many airlines are from the USA, you would query the `airlines` table, filtering by the `country` column.

## SQL Query

```sql
SELECT count(*)
FROM airlines
WHERE country = 'USA';
```

## Explanation

*   `SELECT count(*)`: This part of the query counts the total number of rows that match the specified criteria. In this context, it counts the number of airlines.
*   `FROM airlines`: This specifies that the query will retrieve data from the `airlines` table.
*   `WHERE country = 'USA'`: This is the filtering condition. It restricts the count to only include airlines where the `country` column's value is 'USA'.