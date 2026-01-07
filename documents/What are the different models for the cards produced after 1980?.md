To retrieve the different car models produced after 1980, you can use the following SQL query:

```sql
SELECT DISTINCT T1.model
FROM model_list AS T1
INNER JOIN car_names AS T2
  ON T1.model = T2.model
INNER JOIN cars_data AS T3
  ON T2.makeid = T3.id
WHERE
  T3.year > 1980;
```

### Explanation of the Query:

1.  **`SELECT DISTINCT T1.model`**: This selects the unique `model` names. The `DISTINCT` keyword ensures that only one instance of each model name is returned, even if it appears multiple times in the results.
2.  **`FROM model_list AS T1`**: The query starts by selecting from the `model_list` table, aliased as `T1`. This table likely contains a list of car models.
3.  **`INNER JOIN car_names AS T2 ON T1.model = T2.model`**: An `INNER JOIN` is performed with the `car_names` table (aliased as `T2`) on the `model` column. This links models from the `model_list` to their specific car names, which also contain a `makeid` to link to car data.
4.  **`INNER JOIN cars_data AS T3 ON T2.makeid = T3.id`**: Another `INNER JOIN` connects to the `cars_data` table (aliased as `T3`) using `T2.makeid` and `T3.id`. The `cars_data` table is crucial as it contains the production year information.
5.  **`WHERE T3.year > 1980`**: This clause filters the results to include only those car entries where the `year` of production (from the `cars_data` table) is greater than 1980.

This query effectively joins the necessary tables to filter by the production year and extract the unique car models that meet the specified criteria.