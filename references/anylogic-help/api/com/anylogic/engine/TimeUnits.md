*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/TimeUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class TimeUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[TimeUnits](TimeUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.TimeUnits

All Implemented Interfaces:
:   `IUnits<TimeUnits>`, `Serializable`, `Comparable<TimeUnits>`, `Constable`

---

```
public enum TimeUnits
extends Enum<TimeUnits>
implements IUnits<TimeUnits>
```

Standard AnyLogic time units, should be used in specific functions and parameters which work with units.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, TimeUnits units)` | Converts the given value from **this** units to the given `units` |
| `static TimeUnits` | `fromCalendarConstant(int timeUnit)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `getCalendarConstant()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `boolean` | `isFixedLength()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `modifier(TimeUnits units)` |  |
| `long` | `toMilliseconds()` |  |
| `static TimeUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static TimeUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
