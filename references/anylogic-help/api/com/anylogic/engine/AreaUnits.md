*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AreaUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class AreaUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[AreaUnits](AreaUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.AreaUnits

All Implemented Interfaces:
:   `IUnits<AreaUnits>`, `Serializable`, `Comparable<AreaUnits>`, `Constable`

---

```
public enum AreaUnits
extends Enum<AreaUnits>
implements IUnits<AreaUnits>
```

Standard AnyLogic area units, should be used in specific functions and parameters which work with units.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, AreaUnits units)` | Converts the given value from **this** units to the given `units` |
| `LengthUnits` | `getLengthUnits()` |  |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `double` | `modifier(AreaUnits units)` |  |
| `static AreaUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static AreaUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
