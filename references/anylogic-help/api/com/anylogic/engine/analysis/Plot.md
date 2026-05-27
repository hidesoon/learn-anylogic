*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Plot.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Plot

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataSet](DataSet.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart2D](Chart2D.md "class in com.anylogic.engine.analysis")

[com.anylogic.engine.analysis.Chart2DPlot](Chart2DPlot.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.Plot

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class Plot
extends Chart2DPlot
```

The chart that displays a collection of data sets as plots - polylines with point at
each data point and straingh lines in between. There are no restrictions on the X and
Y values in the data sets. The chart has a collection of DataSet objects and the
collection of associated visual appearance descriptions. The chart
may have scale text labels and a grid for both axes.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Plot)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Plot(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, Chart.ScaleType scaleTypeX, double minimumX, double maximumX, Chart.ScaleType scaleTypeY, double minimumY, double maximumY, Chart.GridPosition gridPositionX, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles, List<Chart2DPlot.Appearance> appearances)` | Creates a persistent Plot. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `refresh()` | Causes the chart to refresh its picture and legend based on the newest data values. |
| `void` | `setFixedHorizontalScale(double minimum, double maximum)` | Sets fixed scale for horizontal axis of chart |
| `void` | `setFixedVerticalScale(double minimum, double maximum)` | Sets fixed scale for vertical axis of chart |
