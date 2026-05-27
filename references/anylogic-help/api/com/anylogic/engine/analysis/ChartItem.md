*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/ChartItem.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class ChartItem

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.analysis.ChartItem

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `BasicDataSet`, `DataItem`, `Histogram2DData`, `HistogramData`

---

```
public class ChartItem
extends Object
implements Serializable
```

An item that holds data and can be displayed by a chart (a unit of what
can be displayed by the chart). Can be a single scalar value or a set of
values. This base class just has an update() method.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.ChartItem)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ChartItem()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `long` | `getVersion()` | Returns the version of this chart item. |
| `void` | `update()` | Should be overridden and perform chart-dependent update.  By default does nothing. |
