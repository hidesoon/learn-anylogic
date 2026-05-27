*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/TimeColorChart.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class TimeColorChart

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataSet](DataSet.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart2D](Chart2D.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.TimeColorChart

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class TimeColorChart
extends Chart2D
```

The chart that displays a collection of data sets as a number of horizontal strips
with color varying along the X (time) axis. The data set X (time) values must be
non-decreasing. The time axis shows the data in the specified time window.
The correspondence of data set value and a color is defined euther in Presentable
by method getShapeChartColorFromDouble, or by the object ColorMap passed in the
constructor. The thickness of strips can be controlled. The chart may have X (time)
scale text labels and a grid.

Chart may display date labels on the time axis (model date instead of model time).
To turn on this mode please provide not `null` `dateFormatPattern`
using one of available constants (`DEFAULT_TIME_PATTERN`, `DEFAULT_DATE_PATTERN`
or `DEFAULT_DATE_TIME_PATTERN`)
or custom [date/time format pattern](TimePlot.md#syntax)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.TimeColorChart)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `TimeColorChart.ColorMap` | Deprecated. |

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TimeColorChart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, double timeWindow, Chart.TimeWindowMovementType timeWindowMovementType, String dateFormatPattern, double relativeBarWidth, Chart.GridPosition gridPositionT, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles, Color defaultValueColor, ColorMapping[] colorMappings)` | Creates a persistent TimeColorChart. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addDataSet(DataSet ds)` | Adds a DataSet to the chart with default title "Data set". |
| `void` | `addDataSet(DataSet ds, String title)` | Adds a DataSet to the chart. |
| `Color` | `getColor(int i)` | This method always return null for TimeColorChart |
| `ColorMapping` | `getColorMapping(int index)` | Returns the color mapping - conditional expression the value to be checked against to determine the color.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `getColorMappingsCount()` | Returns the number of color mappings - conditional expressions the value to be checked against to determine the color.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Color` | `getDefaultColor()` | Returns the color to be used when all the value doesn't match any of `colorMappings`.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `refresh()` | Causes the chart to refresh its picture and legend based on the newest data values. |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setColor(int i, Color c)` | This method has no effect on TimeColorChart |
| `void` | `setIDEDrivenMode_xjal(Date modelStartDate, long modelTimeUnits)` | *This method shouldn't be called by user  (is public due to technical reasons)* |
