To find the number of car models produced by each maker, along with the maker's full name, you can use the following SQL query:

```sql
SELECT
  COUNT(*),
  T2.fullname
FROM model_list AS T1
INNER JOIN car_makers AS T2
  ON T1.maker = T2.id
GROUP BY
  T2.id;
```