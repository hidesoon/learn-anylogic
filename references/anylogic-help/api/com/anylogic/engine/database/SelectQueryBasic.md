*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/SelectQueryBasic.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class SelectQueryBasic<QUERY extends SelectQueryBasic<QUERY>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.SelectQueryBasic<QUERY>

Direct Known Subclasses:
:   `SelectQuery`

---

```
public class SelectQueryBasic<QUERY extends SelectQueryBasic<QUERY>>
extends Object
```

SelectQuery for building and execution of SELECT SQL statements

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `SelectQueryBasic(ModelDBConnectivity database, com.querydsl.sql.RelationalPathBase<?> table)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `long` | `count()` | This function caches its results, to speed up default behavior Use count(false) to get non cached result every time |
| `long` | `count(boolean cached)` |  |
| `QUERY` | `distinct()` | Set the SelectQuery to return distinct results |
| `com.querydsl.core.types.dsl.BooleanExpression` | `exists()` | Exists is used to test for the existence of any record in a subquery. |
| `com.querydsl.core.Tuple` | `firstResult(boolean cached, com.querydsl.core.types.Expression<?>... columns)` | Returns first result for the given SelectQuery or null if no result is found This function caches its results, to speed up default behavior Use firstResult(columns) to get non cached result every time |
| `<RT> RT` | `firstResult(boolean cached, com.querydsl.core.types.Expression<RT> column)` | Returns first result for the given SelectQuery or null if no result is found |
| `<RT, T> RT` | `firstResult(boolean cached, com.querydsl.core.types.Expression<T> column, Class<RT> returnType)` | Returns first result for the given SelectQuery or null if no result is found |
| `com.querydsl.core.Tuple` | `firstResult(com.querydsl.core.types.Expression<?>... columns)` | Returns first result for the given SelectQuery or null if no result is found This function caches its results, to speed up default behavior Use firstResult(columns) to get non cached result every time |
| `<RT> RT` | `firstResult(com.querydsl.core.types.Expression<RT> column)` | Returns first result for the given SelectQuery or null if no result is found This function caches its results, to speed up default behavior Use firstResult(false, column) to get non cached result every time |
| `<RT, T> RT` | `firstResult(com.querydsl.core.types.Expression<T> column, Class<RT> returnType)` | Returns first result for the given SelectQuery or null if no result is found This function caches its results, to speed up default behavior Use firstResult(false, column, returnType) to get non cached result every time |
| `QUERY` | `fullJoin(com.querydsl.core.types.EntityPath<?> table)` | Adds a full join to query |
| `<E> QUERY` | `fullJoin(com.querydsl.sql.ForeignKey<E> key, com.querydsl.sql.RelationalPath<E> table)` | Adds a full join to query |
| `com.querydsl.sql.SQLQuery<com.querydsl.core.Tuple>` | `getDSLQuery()` |  |
| `com.querydsl.sql.SQLBindings` | `getSQL(com.querydsl.core.types.Expression<?>... columns)` | Get the query as an SQL query string and parameters |
| `QUERY` | `groupBy(com.querydsl.core.types.Expression<?> column)` | Defines GROUP BY statement column |
| `QUERY` | `groupBy(com.querydsl.core.types.Expression<?>... columns)` | Defines GROUP BY statement columns |
| `boolean` | `hasResults()` | This function caches its results, to speed up default behavior Use exists(false) to get non cached result every time |
| `boolean` | `hasResults(boolean cached)` |  |
| `QUERY` | `innerJoin(com.querydsl.core.types.EntityPath<?> table)` | Adds an inner join to query |
| `<E> QUERY` | `innerJoin(com.querydsl.sql.ForeignKey<E> key, com.querydsl.sql.RelationalPath<E> table)` | Adds an inner join to query |
| `QUERY` | `join(com.querydsl.core.types.EntityPath<?> table)` | Adds a join to query |
| `<E> QUERY` | `join(com.querydsl.sql.ForeignKey<E> key, com.querydsl.sql.RelationalPath<E> table)` | Adds a join to query |
| `QUERY` | `leftJoin(com.querydsl.core.types.EntityPath<?> table)` | Adds a left join to query |
| `<E> QUERY` | `leftJoin(com.querydsl.sql.ForeignKey<E> key, com.querydsl.sql.RelationalPath<E> table)` | Adds a left join to query |
| `QUERY` | `limit(long limit)` | Defines the maximum number of rows for the selection results |
| `List<com.querydsl.core.Tuple>` | `list()` | List the results for columns of origin table we select from An empty list is returned for no results. |
| `List<com.querydsl.core.Tuple>` | `list(com.querydsl.core.types.Expression<?>... columns)` | List the results for given columns of SelectQuery An empty list is returned for no results. |
| `<RT> List<RT>` | `list(com.querydsl.core.types.Expression<RT> column)` | List the results for given column of SelectQuery An empty list is returned for no results. |
| `QUERY` | `offset(long offset)` | Defines the offset for the selection results |
| `QUERY` | `on(com.querydsl.core.types.Predicate condition)` | Defines a condition to the last added join |
| `QUERY` | `on(com.querydsl.core.types.Predicate... conditions)` | Defines a conditions to the last added join |
| `QUERY` | `orderBy(com.querydsl.core.types.OrderSpecifier<?> orderSpecifier)` | Defines ORDER BY specifier |
| `QUERY` | `orderBy(com.querydsl.core.types.OrderSpecifier<?>... orderSpecifiers)` | Defines ORDER BY specifiers |
| `QUERY` | `rightJoin(com.querydsl.core.types.EntityPath<?> table)` | Adds a right join to query |
| `<E> QUERY` | `rightJoin(com.querydsl.sql.ForeignKey<E> key, com.querydsl.sql.RelationalPath<E> table)` | Adds a right join to query |
| `com.querydsl.core.Tuple` | `uniqueResult(boolean cached, com.querydsl.core.types.Expression<?>... columns)` | Returns a unique result for the given SelectQuery This function caches its results, to speed up default behavior Use uniqueResult(columns) to get non cached result every time |
| `<RT> RT` | `uniqueResult(boolean cached, com.querydsl.core.types.Expression<RT> column)` | Returns an unique result for the given SelectQuery |
| `<RT, T> RT` | `uniqueResult(boolean cached, com.querydsl.core.types.Expression<T> column, Class<RT> returnType)` | Returns an unique result for the given SelectQuery |
| `com.querydsl.core.Tuple` | `uniqueResult(com.querydsl.core.types.Expression<?>... columns)` | Returns a unique result for the given SelectQuery This function caches its results, to speed up default behavior Use uniqueResult(columns) to get non cached result every time |
| `<RT> RT` | `uniqueResult(com.querydsl.core.types.Expression<RT> column)` | Returns an unique result for the given SelectQuery This function caches its results, to speed up default behavior Use uniqueResult(false, column) to get non cached result every time |
| `<RT, T> RT` | `uniqueResult(com.querydsl.core.types.Expression<T> column, Class<RT> returnType)` | Returns an unique result for the given SelectQuery This function caches its results, to speed up default behavior Use uniqueResult(false, column, returnType) to get non cached result every time |
| `QUERY` | `where(com.querydsl.core.types.Predicate condition)` | Add condition for selection results |
| `QUERY` | `where(com.querydsl.core.types.Predicate... conditions)` | Add conditions for selection results |
