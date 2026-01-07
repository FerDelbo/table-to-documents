This document provides a SQL query to identify car models that are lighter than 3500 units and are not manufactured by 'Ford Motor Company'.

## Car Models: Lighter than 3500 and Not by 'Ford Motor Company'

To find car models that meet the criteria of having a weight less than 3500 and not being produced by 'Ford Motor Company', we need to query multiple tables: `model_list`, `car_names`, `cars_data`, and `car_makers`.

### SQL Query

```sql
SELECT DISTINCT T1.model
FROM model_list AS T1
JOIN car_names AS T2
  ON T1.model = T2.model
JOIN cars_data AS T3
  ON T2.makeid = T3.id
JOIN car_makers AS T4
  ON T1.maker = T4.id
WHERE
  T3.weight < 3500 AND T4.fullname != 'Ford Motor Company';
```

### Query Explanation

1.  **`SELECT DISTINCT T1.model`**: This clause selects the `model` column from the `model_list` table (aliased as `T1`). The `DISTINCT` keyword ensures that only unique model names are returned, avoiding duplicates if a model has multiple entries or variations that fit the criteria.

2.  **`FROM model_list AS T1`**: The query starts by selecting from the `model_list` table, which likely contains information about car models and their associated makers. It's aliased as `T1` for brevity.

3.  **`JOIN car_names AS T2 ON T1.model = T2.model`**: This joins `model_list` (T1) with `car_names` (T2). This join is necessary to link the generic model name from `model_list` to specific car entries that include a `makeid`, which can then be used to access performance data.

4.  **`JOIN cars_data AS T3 ON T2.makeid = T3.id`**: This further joins the result with `cars_data` (T3). The `makeid` from `car_names` (T2) is matched with the `id` from `cars_data` (T3) to retrieve detailed specifications such as weight.

5.  **`JOIN car_makers AS T4 ON T1.maker = T4.id`**: This final join connects the `model_list` (T1) to the `car_makers` (T4) table using the `maker` ID. This allows us to access the full name of the car manufacturer.

6.  **`WHERE T3.weight < 3500 AND T4.fullname != 'Ford Motor Company'`**: This is the filtering condition:
    *   `T3.weight < 3500`: Filters for cars whose `weight` (from `cars_data`) is less than 3500.
    *   `AND T4.fullname != 'Ford Motor Company'`: Further filters the results to exclude any models where the manufacturer's `fullname` (from `car_makers`) is 'Ford Motor Company'.

### Expected Output

The query will return a list of car model names, ensuring that each model listed is lighter than 3500 units and was not built by 'Ford Motor Company'. Each model name will appear only once due to the `DISTINCT` keyword.