To find the name and country of origin of every singer who has a song with the word 'Hey' in its title, you can use the following SQL query.

### Query to Find Singers with 'Hey' in Song Title

The question asks for singers whose songs contain the word 'Hey' in their title, along with their name and country of origin. This requires querying the `singer` table and using a `LIKE` operator for pattern matching on the `song_name` column.

```sql
SELECT
  name,
  country
FROM singer
WHERE
  song_name LIKE '%Hey%';
```

#### Explanation:
*   **SELECT `name`, `country`**: This specifies that the query should return the `name` (singer's name) and `country` (country of origin) columns from the results.
*   **FROM `singer`**: This indicates that the data will be retrieved from the `singer` table.
*   **WHERE `song_name` LIKE `'\%Hey\%'`**: This is the filtering condition. It selects only those rows where the `song_name` column contains the substring 'Hey'. The `%` wildcard matches any sequence of zero or more characters.

#### Expected Output:

The query will return a list of singers' names and their respective countries, for all singers who have at least one song title containing the word "Hey".

| name  | country |
| :---- | :------ |
| ...   | ...     |
| ...   | ...     |