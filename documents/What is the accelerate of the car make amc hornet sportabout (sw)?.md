The acceleration of the car model "amc hornet sportabout (sw)" can be retrieved using a SQL query that joins the `cars_data` and `car_names` tables.

```markdown
# Car Acceleration: AMC Hornet Sportabout (SW)

This document details how to retrieve the acceleration value for the specific car model "amc hornet sportabout (sw)" from a relational database.

## Query Description

To obtain the `accelerate` value for a car given its `make` name, we need to perform a join operation between the `cars_data` table (which stores acceleration information) and the `car_names` table (which contains car make names and their corresponding IDs). The result is then filtered to target the specific car make.

## SQL Query

The following SQL query selects the `accelerate` column from the `cars_data` table, joining it with the `car_names` table on their respective ID columns, and then filtering for the `make` named 'amc hornet sportabout (sw)'.

```sql
SELECT
  T1.accelerate
FROM cars_data AS T1
INNER JOIN car_names AS T2
  ON T1.id = T2.makeid
WHERE
  T2.make = 'amc hornet sportabout (sw)';
```