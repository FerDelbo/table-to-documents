To find the airport name for a given airport code, you can query the `airports` table.

### Query to Find Airport Name by Airport Code

To retrieve the name of the airport associated with the code 'AKO', you would use the following SQL query:

```sql
SELECT airportname FROM airports WHERE airportcode = 'AKO'
```

This query selects the `airportname` column from the `airports` table, specifically for rows where the `airportcode` matches 'AKO'.