To find the names of airlines that have flights departing from airport 'AHD', you can use the following SQL query:

```sql
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.sourceairport = 'AHD';
```

### Explanation:

This query retrieves the names of airlines by joining the `airlines` and `flights` tables and filtering the results based on the source airport.

*   **`SELECT T1.airline`**: This specifies that the output should include the `airline` name from the `airlines` table (aliased as `T1`).
*   **`FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.airline`**: This performs an inner join between the `airlines` table (aliased as `T1`) and the `flights` table (aliased as `T2`). The join condition `T1.uid = T2.airline` links airlines to their respective flights using their unique identifiers.
*   **`WHERE T2.sourceairport = 'AHD'`**: This filters the joined results to include only those flights where the `sourceairport` column in the `flights` table (T2) matches 'AHD'.

In summary, the query first connects airlines with their flights and then selects the names of those airlines that have at least one flight originating from the airport identified by the code 'AHD'.