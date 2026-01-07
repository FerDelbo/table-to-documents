To find the airport code and airport name corresponding to the city Anthony, you would query the `airports` table.

```sql
SELECT airportcode, airportname
FROM airports
WHERE city = 'Anthony';
```