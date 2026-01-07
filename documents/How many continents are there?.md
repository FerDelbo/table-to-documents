## How many continents are there?

To determine the total number of continents, you can query the `continents` table to count all entries.

### SQL Query

```sql
SELECT COUNT(*)
FROM continents;
```

### Explanation

This SQL query performs the following actions:
*   `SELECT COUNT(*)`: This aggregate function counts the total number of rows in the `continents` table. Each row is assumed to represent a distinct continent.
*   `FROM continents`: This specifies that the query should retrieve data from the `continents` table.

### Example Output

The query will return a single numerical value representing the total count of continents.

```
+----------+
| COUNT(*) |
+----------+
| 7        |
+----------+
```