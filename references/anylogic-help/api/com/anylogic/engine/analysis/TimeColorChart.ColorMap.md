*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/TimeColorChart.ColorMap.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class TimeColorChart.ColorMap

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.analysis.TimeColorChart.ColorMap

All Implemented Interfaces:
:   `Serializable`

Enclosing class:
:   [TimeColorChart](TimeColorChart.md "class in com.anylogic.engine.analysis")

---

```
@Deprecated
@AnyLogicLegacyAPI
public abstract static class TimeColorChart.ColorMap
extends Object
implements Serializable
```

Deprecated.

The class used to convert double values to Color. Such converter is only
used when the ChartTimeColor is constructed without Presentable object.
The colorFromDouble method must be defined.

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.TimeColorChart.ColorMap)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ColorMap()` | Deprecated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract Color` | `colorFromDouble(double value)` | Deprecated. |
