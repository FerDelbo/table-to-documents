To determine which year had the most concerts, you can query the `concert` table and group the results by year, counting the number of concerts in each year, and then ordering by the count in descending order.

```markdown
# Year with the Most Concerts

To identify the year with the highest number of concerts, the following SQL query can be used:

## SQL Query

```sql
SELECT
  year
FROM concert
GROUP BY
  year
ORDER BY
  count(*) DESC
LIMIT 1;
```

## Explanation

1.  **`SELECT year`**: This specifies that we want to retrieve the `year` column from the `concert` table.
2.  **`FROM concert`**: This indicates that the data will be pulled from the `concert` table.
3.  **`GROUP BY year`**: This clause groups rows that have the same `year` value. This is crucial for counting concerts per year.
4.  **`ORDER BY count(*) DESC`**: After grouping, `count(*)` calculates the number of concerts for each year. The results are then ordered in descending order based on this count, placing the year with the most concerts at the top.
5.  **`LIMIT 1`**: This restricts the output to only the first row, which corresponds to the year with the highest number of concerts due to the `ORDER BY` clause.

This query will return a single year, which is the year that hosted the greatest number of concerts.