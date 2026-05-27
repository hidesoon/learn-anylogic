*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/DataItem.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class DataItem

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.analysis.ChartItem](ChartItem.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.DataItem

All Implemented Interfaces:
:   `Serializable`

---

```
public class DataItem
extends ChartItem
```

A chart item that contains a single scalar value of type double.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.DataItem)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DataItem()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `List<List<Object>>` | `getPlainDataTable()` |  |
| `final double` | `getValue()` | Returns the value of the data item |
| `void` | `setValue(double val)` | Sets the value of the data item. |
| `String` | `toString()` | Returns the textual representation of the data item - the formatted value. |
| `void` | `update()` | Should be overridden and call setValue(...) if the user has specified the value for item. |
