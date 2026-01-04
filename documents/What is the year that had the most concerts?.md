To determine the year with the most concerts, you would execute an SQL query that counts the number of concerts for each year and then orders the results to find the year with the highest count.

```markdown
# Year with the Most Concerts

To find the year that hosted the highest number of concerts, you can use the following SQL query. This query groups the concerts by year, counts the occurrences for each year, and then orders them in descending order to identify the year with the maximum number of concerts.

## SQL Query

```sql
SELECT year
FROM concert
GROUP BY year
ORDER BY count(*) DESC
LIMIT 1;
```

## Explanation

*   **`SELECT year`**: This specifies that the `year` column should be returned in the result.
*   **`FROM concert`**: This indicates that the data should be retrieved from the `concert` table.
*   **`GROUP BY year`**: This clause groups rows that have the same `year` value into summary rows. Aggregate functions (like `count(*)`) are performed on these groups.
*   **`ORDER BY count(*) DESC`**: This sorts the grouped results in descending order based on the count of concerts for each year, placing the year with the most concerts at the top.
*   **`LIMIT 1`**: This restricts the output to only the first row, which, after sorting, will be the year with the highest number of concerts.

This query effectively isolates and presents the single year that recorded the highest volume of concerts.