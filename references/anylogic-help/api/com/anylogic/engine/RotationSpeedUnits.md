*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/RotationSpeedUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class RotationSpeedUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[RotationSpeedUnits](RotationSpeedUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.RotationSpeedUnits

All Implemented Interfaces:
:   `IUnits<RotationSpeedUnits>`, `Serializable`, `Comparable<RotationSpeedUnits>`, `Constable`

---

```
public enum RotationSpeedUnits
extends Enum<RotationSpeedUnits>
implements IUnits<RotationSpeedUnits>
```

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, RotationSpeedUnits units)` | Converts the given value from **this** units to the given `units` |
| `AngleUnits` | `getLengthUnits()` |  |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `TimeUnits` | `getTimeUnits()` |  |
| `double` | `modifier(RotationSpeedUnits units)` |  |
| `static RotationSpeedUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static RotationSpeedUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
