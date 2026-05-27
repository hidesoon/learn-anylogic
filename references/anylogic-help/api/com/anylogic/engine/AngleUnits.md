*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AngleUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class AngleUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[AngleUnits](AngleUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.AngleUnits

All Implemented Interfaces:
:   `IUnits<AngleUnits>`, `Serializable`, `Comparable<AngleUnits>`, `Constable`

---

```
public enum AngleUnits
extends Enum<AngleUnits>
implements IUnits<AngleUnits>
```

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, AngleUnits units)` | Converts the given value from **this** units to the given `units` |
| `String` | `formatName(boolean fullName)` |  |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `double` | `modifier(AngleUnits units)` |  |
| `static AngleUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static AngleUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
