To find the count of car models produced in the United States, you would use a SQL query that joins the `model_list`, `car_makers`, and `countries` tables. This allows you to link car models to their manufacturers and then to the country where the manufacturer is located.

Here's the breakdown of the SQL query:

### SQL Query

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

### Explanation

1.  **`SELECT COUNT(*)`**: This part of the query counts the total number of rows that satisfy the specified conditions. Each row represents a car model.
2.  **`FROM model_list AS T1`**: We start by selecting from the `model_list` table, aliased as `T1`, which contains information about different car models.
3.  **`INNER JOIN car_makers AS T2 ON T1.maker = T2.id`**: This joins `model_list` (`T1`) with the `car_makers` table (`T2`). The join condition `T1.maker = T2.id` links a car model to its manufacturer using the `maker` ID.
4.  **`INNER JOIN countries AS T3 ON T2.country = T3.countryid`**: This further joins the result with the `countries` table (`T3`). The join condition `T2.country = T3.countryid` connects the car manufacturer to its country of origin.
5.  **`WHERE T3.countryname = 'USA'`**: This is the filtering condition. It ensures that only car models from manufacturers located in the country named 'USA' are included in the count.

This query effectively isolates and counts all car models associated with manufacturers based in the United States.