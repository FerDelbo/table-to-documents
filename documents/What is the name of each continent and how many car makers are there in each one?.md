This document provides the SQL query to determine the name of each continent and the corresponding number of car makers located in each.

## Number of Car Makers per Continent

To find out how many car makers are in each continent, we need to join information from the `continents`, `countries`, and `car_makers` tables.

The following SQL query achieves this by:
1.  Joining `continents` with `countries` on their respective ID and continent columns.
2.  Joining the result with `car_makers` on the country ID.
3.  Grouping the results by continent name to count the car makers for each continent.

```sql
SELECT
  T1.continent,
  COUNT(*)
FROM continents AS T1
JOIN countries AS T2
  ON T1.contid = T2.continent
JOIN car_makers AS T3
  ON T2.countryid = T3.country
GROUP BY
  T1.continent;
```

### Explanation:

*   **`SELECT T1.continent, COUNT(*)`**: This selects the name of the continent (aliased as `T1`) and counts all rows for each group, effectively counting the number of car makers.
*   **`FROM continents AS T1`**: Specifies the `continents` table as the primary table, aliased as `T1`.
*   **`JOIN countries AS T2 ON T1.contid = T2.continent`**: This joins the `continents` table (`T1`) with the `countries` table (`T2`) using `contid` from `continents` and `continent` from `countries` to link countries to their respective continents.
*   **`JOIN car_makers AS T3 ON T2.countryid = T3.country`**: This further joins the result with the `car_makers` table (`T3`) using `countryid` from `countries` and `country` from `car_makers` to link car makers to their countries.
*   **`GROUP BY T1.continent`**: This clause groups the rows by the continent name, so the `COUNT(*)` function can calculate the number of car makers for each unique continent.