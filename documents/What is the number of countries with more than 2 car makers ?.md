To determine the number of countries with more than 2 car makers, you can use the following SQL query.

---

# Number of Countries with More Than 2 Car Makers

To find the number of countries that host more than two car manufacturers, you would count distinct countries where the number of car makers associated with that country exceeds 2.

## SQL Query

```sql
SELECT count(*) FROM countries AS t1 JOIN car_makers AS t2 ON t1.countryid = t2.country GROUP BY t1.countryid HAVING count(*) > 2
```

### Explanation

This query works by:
1.  **Joining `countries` and `car_makers` tables**: It links countries (`t1`) with car makers (`t2`) based on their respective country IDs.
2.  **Grouping by `countryid`**: This groups all car makers belonging to the same country together.
3.  **Counting car makers per country**: `count(*)` tallies the number of car makers within each country group.
4.  **Filtering with `HAVING`**: `HAVING count(*) > 2` then filters these groups, keeping only those countries that have more than two car makers.
5.  **Final Count**: The outer `SELECT count(*)` then counts how many such distinct countries meet this criterion.