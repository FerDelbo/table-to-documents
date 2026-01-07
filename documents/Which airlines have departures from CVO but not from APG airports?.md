The following Markdown document provides a comprehensive answer to your question regarding airlines with departures from CVO but not from APG airports.

---

# Airlines with Departures from CVO but Not APG Airports

To identify airlines that have departures from CVO airport but do not have departures from APG airport, we can construct a SQL query that leverages the `EXCEPT` set operator. This operator returns all distinct rows that are returned by the first `SELECT` statement but not by the second.

## SQL Query

The SQL query to find such airlines involves joining the `airlines` table with the `flights` table twice. The first part of the query selects airlines that depart from 'CVO', and the second part selects airlines that depart from 'APG'. The `EXCEPT` clause then filters out any airlines that appear in the second result set.

```sql
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.sourceairport = 'CVO'
EXCEPT
SELECT T1.airline
FROM airlines AS T1
JOIN flights AS T2
  ON T1.uid = T2.airline
WHERE
  T2.sourceairport = 'APG';
```

## Explanation

Let's break down the components of this query:

1.  **`SELECT T1.airline FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.airline WHERE T2.sourceairport = 'CVO'`**:
    *   This subquery identifies all distinct airline names (`T1.airline`) that have at least one flight (`T2`) originating from the 'CVO' airport (`T2.sourceairport = 'CVO'`).
    *   It joins the `airlines` table (aliased as `T1`) with the `flights` table (aliased as `T2`) using their respective unique identifiers (`uid` for airlines and `airline` for flights, assuming `flights.airline` is a foreign key referencing `airlines.uid`).

2.  **`EXCEPT`**:
    *   This set operator is crucial. It takes the result set of the first `SELECT` statement and removes any rows that are also present in the result set of the second `SELECT` statement.

3.  **`SELECT T1.airline FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.airline WHERE T2.sourceairport = 'APG'`**:
    *   This second subquery, similar to the first, identifies all distinct airline names (`T1.airline`) that have at least one flight (`T2`) originating from the 'APG' airport (`T2.sourceairport = 'APG'`).

## Conclusion

By executing this SQL query, you will obtain a list of airline names that operate flights *from* CVO airport but *do not* operate any flights from APG airport. This effectively answers the question by filtering for airlines based on their departure airport presence and absence.