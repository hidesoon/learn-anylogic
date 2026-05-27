*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/SpeedUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class SpeedUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[SpeedUnits](SpeedUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.SpeedUnits

All Implemented Interfaces:
:   `IUnits<SpeedUnits>`, `Serializable`, `Comparable<SpeedUnits>`, `Constable`

---

```
public enum SpeedUnits
extends Enum<SpeedUnits>
implements IUnits<SpeedUnits>
```

Standard AnyLogic speed units, should be used in specific functions and parameters which work with units.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, SpeedUnits units)` | Converts the given value from **this** units to the given `units` |
| `LengthUnits` | `getLengthUnits()` |  |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `TimeUnits` | `getTimeUnits()` |  |
| `double` | `modifier(SpeedUnits units)` |  |
| `static SpeedUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static SpeedUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
