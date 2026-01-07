To identify which airlines have flights departing from the airport with code 'AHD', we can construct a SQL query that joins the `airlines` and `flights` tables and filters for the specified source airport.

## SQL Query

```sql
SELECT
  T1.airline
FROM airlines AS T1
INNER JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.sourceairport = 'AHD';
```

## Explanation

This query performs the following actions:

1.  **`SELECT T1.airline`**: It selects the name of the airline from the `airlines` table.
2.  **`FROM airlines AS T1 INNER JOIN flights AS T2 ON T1.uid = T2.airline`**: It joins the `airlines` table (aliased as `T1`) with the `flights` table (aliased as `T2`). The join condition `T1.uid = T2.airline` links flights to their respective airlines using the unique identifier (`uid`) from the `airlines` table and the `airline` foreign key in the `flights` table.
3.  **`WHERE T2.sourceairport = 'AHD'`**: This clause filters the joined results to include only those flights where the `sourceairport` is 'AHD'.

The result will be a list of airline names that operate flights originating from the 'AHD' airport.

## Assumed Database Schema

To understand this query, the following simplified schema is assumed:

### `airlines` Table

| Column Name | Type    | Description                       |
| :---------- | :------ | :-------------------------------- |
| `uid`         | INTEGER | Unique identifier for the airline |
| `airline`     | TEXT    | The name of the airline           |
| `abbreviation`| TEXT    | Abbreviation of the airline       |
| `country`     | TEXT    | Country of the airline            |

### `flights` Table

| Column Name   | Type    | Description                               |
| :------------ | :------ | :---------------------------------------- |
| `flightno`      | TEXT    | Flight number                             |
| `airline`       | INTEGER | Foreign key linking to `airlines.uid`     |
| `sourceairport` | TEXT    | Code of the departure airport             |
| `destairport`   | TEXT    | Code of the destination airport           |

## Example Result

If executed against a database, the query would return a result set similar to this (actual results would depend on the data in your database):

| airline           |
| :---------------- |
| United Airlines   |
| Southwest Airlines|
| American Airlines |