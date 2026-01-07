```markdown
# Number of Airports

To determine the total number of airports, a simple count query on the `airports` table is performed.

## SQL Query

```sql
SELECT count(*) FROM airports;
```

## Explanation

This query uses the `COUNT(*)` aggregate function to count all rows in the `airports` table, effectively returning the total number of airports listed.
```