*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AmountUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class AmountUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[AmountUnits](AmountUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.AmountUnits

All Implemented Interfaces:
:   `IUnits<AmountUnits>`, `Serializable`, `Comparable<AmountUnits>`, `Constable`

---

```
public enum AmountUnits
extends Enum<AmountUnits>
implements IUnits<AmountUnits>
```

Standard AnyLogic amount units, should be used in specific functions and parameters which work with units.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, AmountUnits units)` | Converts the given value from **this** units to the given `units` |
| `AmountType` | `getAmountType()` |  |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `double` | `modifier(AmountUnits units)` |  |
| `static AmountUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static AmountUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
