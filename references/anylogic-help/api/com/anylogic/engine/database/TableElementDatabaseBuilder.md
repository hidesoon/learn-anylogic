*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/TableElementDatabaseBuilder.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class TableElementDatabaseBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.TableElementDatabaseBuilder

---

```
@AnyLogicInternalAPI
public class TableElementDatabaseBuilder
extends Object
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TableElementDatabaseBuilder(Utilities utils)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `CustomDistributionAbstract` | `buildCustomDistribution(String type, String definitionType)` |  |
| `<T extends Enum> CustomDistributionOptions<T>` | `buildCustomDistributionOfOptions(Class<T> enumClass)` |  |
| `TableFunction` | `buildTableFunction(TableFunction.InterpolationType interpolationType, int approximationOrder, TableFunction.OutOfRangeAction outOfRangeAction, double outOfRangeValue)` |  |
| `void` | `fillSchedule(Schedule s, Class<?> valueType, boolean isSundayFirst, boolean isByDays, long repeatTime, boolean isRange, boolean isCustom, long atomicDuration)` |  |
| `TableElementDatabaseBuilder` | `setColumns(com.querydsl.core.types.Expression<?>... columns)` |  |
| `TableElementDatabaseBuilder` | `setOwner(Utilities owner)` |  |
| `TableElementDatabaseBuilder` | `setSqlQuery(String sql, Object... params)` |  |
