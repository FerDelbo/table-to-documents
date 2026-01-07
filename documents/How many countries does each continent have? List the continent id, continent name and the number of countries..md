This document provides the SQL query to determine the number of countries within each continent, along with an explanation of how the query works.

## How Many Countries Does Each Continent Have?

This query retrieves the continent ID, continent name, and the total count of countries associated with each continent.

### SQL Query

```sql
SELECT T1.ContId, T1.Continent, COUNT(*)
FROM continents AS T1
JOIN countries AS T2
  ON T1.ContId = T2.Continent
GROUP BY
  T1.ContId;
```

### Explanation

The query uses a `JOIN` operation between the `continents` table (aliased as `T1`) and the `countries` table (aliased as `T2`) to link countries to their respective continents.

1.  **`SELECT T1.ContId, T1.Continent, COUNT(*)`**:
    *   `T1.ContId`: Selects the unique identifier for each continent from the `continents` table.
    *   `T1.Continent`: Selects the name of each continent from the `continents` table.
    *   `COUNT(*)`: Counts the total number of rows (countries) for each group defined by the `GROUP BY` clause.

2.  **`FROM continents AS T1 JOIN countries AS T2 ON T1.ContId = T2.Continent`**:
    *   This clause specifies the tables involved: `continents` (as `T1`) and `countries` (as `T2`).
    *   The `JOIN` condition `T1.ContId = T2.Continent` links records from `continents` to `countries` where the continent ID matches.

3.  **`GROUP BY T1.ContId`**:
    *   This clause groups the results by `ContId`. This ensures that the `COUNT(*)` function aggregates the number of countries for each unique continent ID.

### Tables Involved

*   **`continents`**: This table likely contains information about continents, including `ContId` (Continent ID) and `Continent` (Continent Name).
*   **`countries`**: This table likely contains information about countries, including a `Continent` foreign key that links to `ContId` in the `continents` table.