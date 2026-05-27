*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/StackChart.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class StackChart

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataItem](DataItem.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart1D](Chart1D.md "class in com.anylogic.engine.analysis")

[com.anylogic.engine.analysis.Chart1DSum](Chart1DSum.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.StackChart

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class StackChart
extends Chart1DSum
```

The chart that displays a number of data items in the form of a stack where
each data item has a bar with dimension proportional to its fraction the total
sum of the data items. The data items in this chart cannot take
negative values. The legend values of data items are set to
[data item name]: [data item value] ([data item fraction]%).
The orientation of the stack may be arbitrary (NORTH,
SOUTH, EAST, WEST). The stack may be scaled to 100%, SCALE\_100\_PERCENT, in which
case it always occupies the full picture), SCALE\_AUTO, when stack is fitted
into the best grid, or SCALE\_FIXED, when the user specifies the maximum total.
The thickness of stack bars can be controlled. The chart may have scale
text labels and a grid.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.StackChart)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `StackChart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, Chart.Direction barDirection, Chart.ScaleType scaleType, double maximum, double relativeBarWidth, Chart.GridPosition gridPosition, Color gridLineColor, Color gridTextColor, List<DataItem> dataItems, List<String> titles, List<Color> colors)` | Creates a persistent StackChart If the collection of DataItem objects and a collection of their colors are null, new empty collections are created. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `refresh()` | Causes the chart to refresh its picture and legend based on the newest data values. |
| `void` | `setFixedScale(double maximum)` | Sets fixed scale for the chart |
