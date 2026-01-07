To determine the number of car models produced by the "American Motor Company", you can use a SQL query that joins the `car_makers` and `model_list` tables and filters by the maker's full name.

```markdown
# Number of Car Models Produced by American Motor Company

To find out how many car models were produced by the car maker with the full name "American Motor Company", you can execute the following SQL query:

## SQL Query

```sql
SELECT
  COUNT(*)
FROM car_makers AS T1
JOIN model_list AS T2
  ON T1.id = T2.maker
WHERE
  T1.fullname = 'American Motor Company';
```

## Explanation

1.  **`SELECT COUNT(*)`**: This counts the total number of rows that satisfy the conditions. In this context, each row represents a distinct car model associated with a maker.
2.  **`FROM car_makers AS T1 JOIN model_list AS T2 ON T1.id = T2.maker`**: This performs an inner join between the `car_makers` table (aliased as `T1`) and the `model_list` table (aliased as `T2`). The join condition `T1.id = T2.maker` links car makers to the models they produce using their respective IDs.
3.  **`WHERE T1.fullname = 'American Motor Company'`**: This clause filters the results to include only those records where the `fullname` column in the `car_makers` table is 'American Motor Company'.

This query will return a single number representing the total count of models manufactured by "American Motor Company".
```