*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/FlowRateUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class FlowRateUnits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[FlowRateUnits](FlowRateUnits.md "enum class in com.anylogic.engine")>

com.anylogic.engine.FlowRateUnits

All Implemented Interfaces:
:   `IUnits<FlowRateUnits>`, `Serializable`, `Comparable<FlowRateUnits>`, `Constable`

---

```
public enum FlowRateUnits
extends Enum<FlowRateUnits>
implements IUnits<FlowRateUnits>
```

Standard AnyLogic flow rate units, should be used in specific functions and parameters which work with units.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, FlowRateUnits units)` | Converts the given value from **this** units to the given `units` |
| `AmountType` | `getAmountType()` |  |
| `AmountUnits` | `getAmountUnits()` |  |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `TimeUnits` | `getTimeUnits()` |  |
| `double` | `modifier(FlowRateUnits units)` |  |
| `static FlowRateUnits` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static FlowRateUnits[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
