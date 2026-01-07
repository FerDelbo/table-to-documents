This document provides the SQL query to retrieve the airline names and their abbreviations for airlines based in the USA.

## Querying Airline Information for USA-based Airlines

To find the names and abbreviations of airlines located in the United States, you can perform a selection from the `airlines` table, filtering by the `country` column.

### SQL Query

The following SQL query selects the `airline` name and its `abbreviation` from the `airlines` table where the `country` is 'USA'.

```sql
SELECT
  airline,
  abbreviation
FROM airlines
WHERE
  country = 'USA';
```

### Explanation

*   **`SELECT airline, abbreviation`**: This clause specifies the columns you want to retrieve. In this case, `airline` for the full name of the airline and `abbreviation` for its short code.
*   **`FROM airlines`**: This indicates that the data will be fetched from the `airlines` table.
*   **`WHERE country = 'USA'`**: This is the filtering condition. It ensures that only rows where the `country` column has a value of 'USA' are included in the result set, thereby showing only USA-based airlines.