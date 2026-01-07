```markdown
# Car Models Produced by Each Maker

This document provides the SQL query to determine the number of car models produced by each car maker, along with the maker's ID and full name.

## SQL Query

To retrieve the requested information, you can use the following SQL query:

```sql
SELECT
  COUNT(*),
  T2.FullName,
  T2.Id
FROM Model_List AS T1
JOIN Car_Makers AS T2
  ON T1.Maker = T2.Id
GROUP BY
  T2.Id;
```

## Explanation

1.  **`FROM Model_List AS T1 JOIN Car_Makers AS T2 ON T1.Maker = T2.Id`**:
    *   This part of the query joins two tables: `Model_List` (aliased as `T1`) and `Car_Makers` (aliased as `T2`).
    *   The join condition `T1.Maker = T2.Id` links models to their respective car makers using the `Maker` ID from `Model_List` and the `Id` from `Car_Makers`.

2.  **`GROUP BY T2.Id`**:
    *   This clause groups the results by the `Id` of each car maker. This ensures that the aggregate function (`COUNT(*)`) is applied separately for each unique car maker.

3.  **`SELECT COUNT(*), T2.FullName, T2.Id`**:
    *   `COUNT(*)`: This aggregate function counts the total number of rows (models) for each group (car maker).
    *   `T2.FullName`: This selects the full name of the car maker from the `Car_Makers` table.
    *   `T2.Id`: This selects the ID of the car maker from the `Car_Makers` table.

## Example Result

The query will return a result set similar to this (actual data may vary):

| COUNT(*) | FullName               | Id  |
| :------- | :--------------------- | :-- |
| 5        | American Motor Company | 1   |
| 3        | General Motors         | 2   |
| 7        | Ford Motor Company     | 3   |
| ...      | ...                    | ... |
```