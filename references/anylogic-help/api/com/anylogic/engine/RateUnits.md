*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/RateUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class RateUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[RateUnits](RateUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.RateUnits

All Implemented Interfaces:
:   `IUnits<RateUnits>`, `Serializable`, `Comparable<RateUnits>`, `Constable`

---

```
public enum RateUnits
extends Enum<RateUnits>
implements IUnits<RateUnits>
```

Standard AnyLogic rate units, should be used in specific functions and parameters which work with units.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, RateUnits units)` | Converts the given value from **this** units to the given `units` |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `TimeUnits` | `getTimeUnits()` | Returns the base time unit of this rate unit |
| `double` | `modifier(RateUnits units)` |  |
| `static RateUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static RateUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
