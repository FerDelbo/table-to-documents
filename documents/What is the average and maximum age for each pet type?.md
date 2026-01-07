The average and maximum age for each pet type can be retrieved using the following SQL query:

```sql
SELECT
  avg(pet_age),
  max(pet_age),
  pettype
FROM pets
GROUP BY
  pettype;
```