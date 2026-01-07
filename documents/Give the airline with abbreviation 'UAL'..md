Here's the technical documentation in Markdown format answering your question:

# Find Airline by Abbreviation

This document provides the SQL query to retrieve the full name of an airline given its abbreviation.

## Question

Give the airline with abbreviation 'UAL'.

## SQL Query

To find the airline with the abbreviation 'UAL', you can use the following SQL query:

```sql
SELECT airline
FROM airlines
WHERE abbreviation = 'UAL';
```

## Explanation

This query performs a selection from the `airlines` table based on a specific condition:

*   **`SELECT airline`**: This specifies that the `airline` column (which presumably contains the full name of the airline) should be returned in the result set.
*   **`FROM airlines`**: This indicates that the data should be retrieved from the `airlines` table.
*   **`WHERE abbreviation = 'UAL'`**: This is the filtering condition. It restricts the results to only those rows where the `abbreviation` column matches the string 'UAL'.