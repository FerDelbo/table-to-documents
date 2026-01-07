To determine the number of flights departing from 'APG', you can execute a SQL query that counts the entries in the `flights` table where the `sourceairport` column matches 'APG'.

```sql
SELECT count(*) FROM flights WHERE sourceairport = 'APG';
```

This query will return a single numerical value representing the total count of flights that have 'APG' as their departure airport.

### Tables Used

*   `flights`