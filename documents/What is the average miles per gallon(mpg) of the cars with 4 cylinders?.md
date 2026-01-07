The average miles per gallon (mpg) for cars with 4 cylinders can be retrieved using a SQL query on the `cars_data` table.

```sql
SELECT avg(mpg)
FROM cars_data
WHERE cylinders = 4;
```

This query will return a single value representing the average miles per gallon for all cars recorded in the `cars_data` table that have exactly 4 cylinders.