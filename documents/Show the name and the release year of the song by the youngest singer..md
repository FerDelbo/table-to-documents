To find the name and release year of the song by the youngest singer, you would query the `singer` table. This involves ordering the singers by their age in ascending order and then selecting the song details for the first entry.

```markdown
# Song by the Youngest Singer

To retrieve the name and release year of the song performed by the youngest singer, you need to query the `singer` table, order the results by the singer's age in ascending order, and then limit the output to the top result.

## SQL Query

```sql
SELECT
  song_name,
  song_release_year
FROM singer
ORDER BY
  age ASC
LIMIT 1;
```

## Explanation

*   **`SELECT song_name, song_release_year`**: This specifies that you want to retrieve the `song_name` and `song_release_year` columns from the table.
*   **`FROM singer`**: This indicates that the data should be retrieved from the `singer` table.
*   **`ORDER BY age ASC`**: This clause sorts all rows in the `singer` table based on the `age` column in ascending order, meaning the youngest singer(s) will appear first.
*   **`LIMIT 1`**: This clause restricts the output to only the first row after sorting, effectively giving you the song details associated with the youngest singer.

This query will return the song name and its release year belonging to the singer with the lowest age recorded in the database. If there are multiple singers with the same minimum age, it will return one of their songs.