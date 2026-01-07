```markdown
# Querying Continent Information: ID, Name, and Country Count

This document provides a SQL query to retrieve the ID, name, and the total number of countries associated with each continent.

## SQL Query

To obtain the continent ID, continent name, and the count of countries within each continent, execute the following SQL query:

```sql
SELECT
  T1.contid,
  T1.continent,
  COUNT(*)
FROM continents AS T1
JOIN countries AS T2
  ON T1.contid = T2.continent
GROUP BY
  T1.contid;
```

## Explanation

The query performs the following actions:

1.  **`SELECT T1.contid, T1.continent, COUNT(*)`**: It selects the `contid` (continent ID) and `continent` (continent name) from the `continents` table (aliased as `T1`), along with a count of all records (`COUNT(*)`) for each group.
2.  **`FROM continents AS T1 JOIN countries AS T2 ON T1.contid = T2.continent`**: It joins the `continents` table (`T1`) with the `countries` table (`T2`). The join condition `T1.contid = T2.continent` links continents to their respective countries using their ID.
3.  **`GROUP BY T1.contid`**: This clause groups the results by `contid`, ensuring that the `COUNT(*)` aggregate function tallies countries for each unique continent ID.

This query effectively lists each continent, its unique identifier, and the total number of countries that are linked to it in the database.
```