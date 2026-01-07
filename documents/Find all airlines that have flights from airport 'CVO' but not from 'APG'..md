To find all airlines that have flights departing from airport 'CVO' but not from 'APG', you can use the following SQL query:

```sql
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.sourceairport = 'CVO'
EXCEPT
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.sourceairport = 'APG';
```

### Explanation:

This query works by performing two main selections and then using the `EXCEPT` operator to find the difference between them.

1.  **First `SELECT` statement**:
    *   `SELECT T1.airline FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.airline`: This part joins the `airlines` table (aliased as `T1`) with the `flights` table (aliased as `T2`) on their respective unique identifiers (`uid` from `airlines` and `airline` from `flights`). It then selects the `airline` name.
    *   `WHERE T2.sourceairport = 'CVO'`: This filters the joined results to include only those flights whose `sourceairport` is 'CVO'.
    *   The result of this subquery is a list of all airlines that have *any* flights departing from 'CVO'.

2.  **Second `SELECT` statement (after `EXCEPT`)**:
    *   `SELECT T1.airline FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.airline WHERE T2.sourceairport = 'APG'`: This part is structured similarly to the first. It identifies all airlines that have *any* flights departing from 'APG'.

3.  **`EXCEPT` Operator**:
    *   The `EXCEPT` operator takes the distinct rows from the first `SELECT` query and removes all rows that are also present in the second `SELECT` query.
    *   Therefore, the final result set contains only the airlines that fly from 'CVO' but do *not* fly from 'APG'.