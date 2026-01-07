This document provides a comprehensive guide to retrieving distinct car models produced after the year 1980, formatted in Markdown.

## Retrieving Distinct Car Models Produced After 1980

This section details the SQL query required to find all unique car models that were manufactured after the year 1980, along with an explanation of its components and how to use it.

### SQL Query

To obtain the distinct car models produced after 1980, execute the following SQL query:

```sql
SELECT DISTINCT T1.model
FROM model_list AS T1
JOIN car_names AS T2
  ON T1.model = T2.model
JOIN cars_data AS T3
  ON T2.makeid = T3.id
WHERE
  T3.year > 1980;
```

### Query Explanation

Let's break down the SQL query to understand how it achieves the desired result:

*   **`SELECT DISTINCT T1.model`**:
    *   `SELECT model`: This clause specifies that we want to retrieve the `model` column.
    *   `DISTINCT`: This keyword ensures that only unique model names are returned. If a model was produced multiple times after 1980, it will only appear once in the result set.
    *   `T1`: This is an alias for the `model_list` table, used to make the query more concise and readable.

*   **`FROM model_list AS T1`**:
    *   This indicates that we are starting our query from the `model_list` table, aliased as `T1`. This table is assumed to contain information about various car models.

*   **`JOIN car_names AS T2 ON T1.model = T2.model`**:
    *   This performs an `INNER JOIN` with the `car_names` table (aliased as `T2`).
    *   The `ON T1.model = T2.model` condition links records in `model_list` to `car_names` based on matching `model` values. This step is crucial for connecting a `model` from `model_list` to its specific `makeid` in `car_names`, which then links to the `cars_data` table.

*   **`JOIN cars_data AS T3 ON T2.makeid = T3.id`**:
    *   This performs another `INNER JOIN` with the `cars_data` table (aliased as `T3`).
    *   The `ON T2.makeid = T3.id` condition links records from `car_names` to `cars_data` using the `makeid` from `car_names` and the `id` from `cars_data`. This connection allows us to access the production `year` for each car.

*   **`WHERE T3.year > 1980`**:
    *   This `WHERE` clause filters the results. It includes only those car records where the `year` column from the `cars_data` table (`T3.year`) is strictly greater than `1980`. This effectively selects all cars produced starting from 1981 onwards.

### Assumptions

*   **Database Schema:** The query assumes the existence of three tables:
    *   `model_list`: Contains `model` information.
    *   `car_names`: Links `model` to `makeid`.
    *   `cars_data`: Contains `id` and `year` of car production.
*   **Data Types:** The `year` column in `cars_data` is assumed to be a numeric type allowing for direct comparison with `1980`.
*   **Relationship:** A clear relationship exists between `model_list` and `car_names` via the `model` column, and between `car_names` and `cars_data` via `makeid` and `id` respectively.

### Usage

To use this query:

1.  Connect to your SQL database.
2.  Execute the provided SQL statement.
3.  The result will be a list of distinct car model names that were produced after the year 1980.

This document provides a clear, structured, and accurate method for obtaining the requested information from a relational database using SQL.