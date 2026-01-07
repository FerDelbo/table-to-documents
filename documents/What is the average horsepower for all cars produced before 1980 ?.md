To find the average horsepower for all cars produced before 1980, you would use the following SQL query:

```sql
SELECT AVG(horsepower)
FROM cars_data
WHERE year < 1980;
```