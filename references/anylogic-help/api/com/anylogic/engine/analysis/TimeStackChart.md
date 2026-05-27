*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/TimeStackChart.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class TimeStackChart

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataSet](DataSet.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart2D](Chart2D.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.TimeStackChart

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class TimeStackChart
extends Chart2D
```

The chart that displays a collection of data sets in the form of a timed stack,
i.e. a each data set is shown as a horizontal strip with height proportional to
the fraction of its value in the total of all data sets at each time moment. The data set
X (time) values must be non-decreasing. The time axis shows the data in the
specified time window. A color is associated with each data set.
Data set Y values must be non-negative. The stack may be scaled to 100%,
SCALE\_100\_PERCENT, in which case it always occupies the full picture height), SCALE\_AUTO,
when stack is fitted into the best grid, or SCALE\_FIXED, when the user specifies
the maximum total. The chart may have scale text labels and a grid.

Chart may display date labels on the time axis (model date instead of model time).
To turn on this mode please provide not `null` `dateFormatPattern`
using one of available constants (`DEFAULT_TIME_PATTERN`, `DEFAULT_DATE_PATTERN`
or `DEFAULT_DATE_TIME_PATTERN`)
or custom [date/time format pattern](TimePlot.md#syntax)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.TimeStackChart)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TimeStackChart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, double timeWindow, Chart.TimeWindowMovementType timeWindowMovementType, String dateFormatPattern, Chart.ScaleType scaleTypeY, double maximumY, Chart.GridPosition gridPositionT, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles, List<Color> colors)` | Creates a persistent TimeStackChart. |
| `TimeStackChart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, double timeWindow, String dateFormatPattern, Chart.ScaleType scaleTypeY, double maximumY, Chart.GridPosition gridPositionT, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles, List<Color> colors)` | Creates a persistent TimeStackChart. |
| `TimeStackChart(Presentable p, boolean ispublic, int x, int y, int width, int height, Color fillColor, Color lineColor, int picOffsetX, int picOffsetY, int picWidth, int picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, int legendSize, Chart.Direction legendPos, double timeWindow, String dateFormatPattern, Chart.ScaleType scaleTypeY, double maximumY, Chart.GridPosition gridPositionT, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles, List<Color> colors)` | Deprecated. Will be removed in the next release. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addDataSet(DataSet ds)` | Adds a DataSet to the chart with default title "Data set" and defalt color royalBlue. |
| `void` | `addDataSet(DataSet ds, String title, Color color)` | Adds a DataSet to the chart with the specified title and color. |
| `Color` | `getColor(int i)` | Returns the color of the chart item with the given index. |
| `void` | `refresh()` | Causes the chart to refresh its picture and legend based on the newest data values. |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setColor(int i, Color c)` | Sets the new color of the chart item with the given index. |
| `void` | `setFixedVerticalScale(double maximum)` | Sets fixed scale for vertical axis of chart |
| `void` | `setIDEDrivenMode_xjal(Date modelStartDate, long modelTimeUnits)` | *This method shouldn't be called by user  (is public due to technical reasons)* |
