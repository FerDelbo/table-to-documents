To find out which airlines have flights with a destination airport of 'AHD', you can use the following SQL query:

```sql
SELECT
  T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.destairport = 'AHD';
```

## Explanation of the SQL Query

This query retrieves the names of airlines by joining the `airlines` table with the `flights` table and filtering for flights that arrive at the specified airport.

### 1. SELECT Clause

*   `T1.airline`: This selects the `airline` name from the `airlines` table (aliased as `T1`).

### 2. FROM Clause

*   `airlines AS T1`: Specifies the `airlines` table and assigns it the alias `T1` for brevity.
*   `JOIN flights AS T2 ON T1.uid = T2.airline`: Performs an inner join with the `flights` table (aliased as `T2`). The join condition `T1.uid = T2.airline` links an airline in the `airlines` table to its corresponding flights in the `flights` table using their unique identifiers.

### 3. WHERE Clause

*   `T2.destairport = 'AHD'`: This clause filters the joined records to include only those flights where the `destairport` (destination airport code) in the `flights` table (`T2`) is 'AHD'.

## Conceptual Schema

To understand this query, consider the simplified structure of the tables involved:

### `airlines` Table

This table contains information about various airlines.
| Column Name | Description               | Data Type |
| :---------- | :------------------------ | :-------- |
| `uid`       | Unique ID for the airline | INTEGER   |
| `airline`   | Name of the airline       | TEXT      |
| `country`   | Country of origin         | TEXT      |
| `abbreviation` | Abbreviation for the airline | TEXT   |

### `flights` Table

This table contains details about individual flights.
| Column Name   | Description          | Data Type |
| :------------ | :------------------- | :-------- |
| `flightno`    | Flight number        | TEXT      |
| `airline`     | Foreign key to `airlines.uid` | INTEGER |
| `sourceairport` | Code of the departure airport | TEXT |
| `destairport` | Code of the destination airport | TEXT |

## How it Answers the Question

The query works by:
1.  Establishing a link between airlines and their flights.
2.  Filtering these flights to only include those that have 'AHD' as their destination.
3.  Finally, it extracts the name of the airline associated with these filtered flights.

This ensures that only the names of airlines operating flights arriving at "AHD" airport are returned.