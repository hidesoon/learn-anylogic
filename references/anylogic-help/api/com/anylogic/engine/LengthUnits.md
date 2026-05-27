*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LengthUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class LengthUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[LengthUnits](LengthUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.LengthUnits

All Implemented Interfaces:
:   `IUnits<LengthUnits>`, `Serializable`, `Comparable<LengthUnits>`, `Constable`

---

```
public enum LengthUnits
extends Enum<LengthUnits>
implements IUnits<LengthUnits>
```

Standard AnyLogic length units, should be used in specific functions and parameters which work with units.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, LengthUnits units)` | Converts the given value from **this** units to the given `units` |
| `String` | `formatName(boolean fullName)` |  |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `double` | `modifier(LengthUnits units)` |  |
| `static LengthUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static LengthUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
