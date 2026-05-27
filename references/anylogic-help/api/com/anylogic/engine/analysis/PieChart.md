*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/PieChart.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class PieChart

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataItem](DataItem.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart1D](Chart1D.md "class in com.anylogic.engine.analysis")

[com.anylogic.engine.analysis.Chart1DSum](Chart1DSum.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.PieChart

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class PieChart
extends Chart1DSum
```

The chart that displays a number of data items in the form of a pie where
each data item has a sector with angular extension proportional to its
fraction the total sum of the data items. The data items in this chart cannot take
negative values. The legend values of data items are set to
[data item name]: [data item value] ([data item fraction]%).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.PieChart)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PieChart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, List<DataItem> dataItems, List<String> titles, List<Color> colors)` | Creates a persistent PieChart. |
| `PieChart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, List<DataItem> dataItems, List<String> titles, List<Color> colors)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `refresh()` | Causes the chart to refresh its picture and legend based on the newest data values. |
