*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/BarChart.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class BarChart

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataItem](DataItem.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart1D](Chart1D.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.BarChart

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class BarChart
extends Chart1D
```

The chart that displays a number of data items as bars with dimension proportional
to their values (which can be negative). The legend values of data items are set to
[data item name]: [data item value].
The orientation of the bars may be arbitrary (NORTH, SOUTH, EAST, WEST).
The bars scale type may be SCALE\_AUTO, then bars are fitted into the best grid,
or SCALE\_FIXED, when the user specifies the minimum and maximum.
The thickness of bars can be controlled. The chart may have scale text labels
and a grid.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.BarChart)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `BarChart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, Chart.Direction barDirection, Chart.ScaleType scaleType, double minimum, double maximum, double relativeBarWidth, Chart.GridPosition gridPosition, Color gridLineColor, Color gridTextColor, List<DataItem> dataItems, List<String> titles, List<Color> colors)` | Creates a persistent BarChart. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addDataItem(DataItem di, String title, Color color)` | Adds a DataItem to the chart. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `refresh()` | Causes the chart to refresh its picture and legend based on the newest data values. |
| `void` | `setFixedScale(double minimum, double maximum)` | Sets fixed scale for the chart |
