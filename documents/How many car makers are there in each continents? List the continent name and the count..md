To determine the number of car makers in each continent and list their names along with the respective counts, you can use the following SQL query.

## SQL Query

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

## Explanation

This query retrieves the count of car makers for each continent by joining three tables: `continents`, `countries`, and `car_makers`.

1.  **`FROM continents AS T1`**:
    *   Starts by selecting data from the `continents` table, aliased as `T1`. This table presumably contains information about continents, including their names (`continent`) and unique identifiers (`contid`).

2.  **`JOIN countries AS T2 ON T1.contid = T2.continent`**:
    *   Connects the `continents` table (`T1`) with the `countries` table (`T2`). The join condition `T1.contid = T2.continent` links continents to the countries that belong to them, assuming `T2.continent` is a foreign key referencing `T1.contid`.

3.  **`JOIN car_makers AS T3 ON T2.countryid = T3.country`**:
    *   Further joins the result with the `car_makers` table (`T3`). The condition `T2.countryid = T3.country` links countries (`T2`) to the car makers (`T3`) located in those countries, assuming `T3.country` is a foreign key referencing `T2.countryid`.

4.  **`SELECT T1.continent, COUNT(*)`**:
    *   Selects the `continent` name from the `continents` table (`T1`).
    *   Uses the `COUNT(*)` aggregate function to count the total number of rows (representing car makers after the joins) for each group.

5.  **`GROUP BY T1.continent`**:
    *   Groups the results by `T1.continent`. This ensures that the `COUNT(*)` function calculates the number of car makers for each unique continent.

The query will return a result set with two columns: the name of the continent and the total number of car makers associated with that continent.