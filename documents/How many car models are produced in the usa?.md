To determine the number of car models produced in the USA, you can use the following SQL query:

```sql
SELECT
  COUNT(*)
FROM model_list AS T1
INNER JOIN car_makers AS T2
  ON T1.maker = T2.id
INNER JOIN countries AS T3
  ON T2.country = T3.countryid
WHERE
  T3.countryname = 'USA';
```

### Explanation:

This query joins three tables: `model_list`, `car_makers`, and `countries` to link car models to their respective manufacturing countries.

1.  **`FROM model_list AS T1`**: Starts by selecting from the `model_list` table, aliased as `T1`, which contains information about car models.
2.  **`INNER JOIN car_makers AS T2 ON T1.maker = T2.id`**: Joins `model_list` (T1) with the `car_makers` table (aliased as `T2`) on the `maker` ID to link models to their manufacturers.
3.  **`INNER JOIN countries AS T3 ON T2.country = T3.countryid`**: Further joins `car_makers` (T2) with the `countries` table (aliased as `T3`) on the `country` ID to associate car makers with their country of origin.
4.  **`WHERE T3.countryname = 'USA'`**: Filters the results to include only those records where the `countryname` in the `countries` table is 'USA'.
5.  **`SELECT COUNT(*)`**: Counts the total number of car models that satisfy the filtering condition, effectively giving the number of car models produced in the USA.

This query will return a single numerical value representing the count of car models associated with manufacturers located in the USA.