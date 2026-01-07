The number of cars with horsepower greater than 150 can be found by querying the `cars_data` table.

```sql
SELECT count(*)
FROM cars_data
WHERE horsepower > 150;
```