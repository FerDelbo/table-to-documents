To find the name and country (nation) of singers who have a song with 'Hey' in its title, you would query the `singer` table.

### SQL Query

```sql
SELECT
  name,
  country
FROM singer
WHERE
  song_name LIKE '%Hey%';
```

### Explanation

*   **`SELECT name, country`**: This specifies that you want to retrieve the `name` and `country` (referred to as 'nation' in your question) columns from the `singer` table.
*   **`FROM singer`**: This indicates that the data should be fetched from the `singer` table.
*   **`WHERE song_name LIKE '%Hey%'`**: This is the filtering condition.
    *   `song_name` refers to the column containing the song titles.
    *   `LIKE` is used for pattern matching.
    *   `'%Hey%'` is the pattern:
        *   The `%` wildcard matches any sequence of zero or more characters.
        *   `'Hey'` is the literal string to match.
        *   Putting `%` before and after 'Hey' means it will match any `song_name` that contains 'Hey' anywhere within its text (e.g., 'Hey Jude', 'The Hey Song', 'Say Hey').

This query will return a list of singers' names and their respective countries for all songs that contain 'Hey' in their title.