The number of flights arriving at 'ATO' can be determined by querying the `flights` table and filtering by the `destairport` column.

```sql
SELECT count(*)
FROM flights
WHERE destairport = 'ATO';
```