To find the last name of the student who owns a 3-year-old cat, you need to query the `student`, `has_pet`, and `pets` tables, joining them on their respective IDs and applying filters for `pettype` and `pet_age`.

```sql
SELECT
  T1.lname
FROM student AS T1
INNER JOIN has_pet AS T2
  ON T1.stuid = T2.stuid
INNER JOIN pets AS T3
  ON T2.petid = T3.petid
WHERE
  T3.pet_age = 3 AND T3.pettype = 'cat';
```