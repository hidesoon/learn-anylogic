*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Chart2DPlot.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Chart2DPlot

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataSet](DataSet.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart2D](Chart2D.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.Chart2DPlot

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Plot`, `TimePlot`

---

```
public abstract class Chart2DPlot
extends Chart2D
```

The base class for all charts that display a collection of two-dimensional data sets
in the form of plots, like Plot, TimePlot. The chart has a collection of DataSet objects and the
collection of associated visual appearance descriptions. The chart
may have scale text labels and a grid.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Chart2DPlot)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `Chart2DPlot.Appearance` | Descriptor or a data set plot appearance. |

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Chart2DPlot(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, Chart.ScaleType scaleTypeY, double minimumY, double maximumY, Chart.GridPosition gridPositionX, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles, List<Chart2DPlot.Appearance> appearances)` | Creates a persistent Chart2DPlot. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addDataSet(DataSet ds)` | Adds a DataSet to the chart with default title "Data set" and default visual appearance: royalBlue color, line of width 1 is drawn, points are not drawn, linear interpolation. |
| `void` | `addDataSet(DataSet ds, String title)` | Adds a DataSet to the chart a given title and default visual appearnce: royalBlue color, line of width 1 is drawn, points are not drawn, linear interpolation. |
| `void` | `addDataSet(DataSet ds, String title, Chart2DPlot.Appearance appearance)` | Adds a DataSet to the chart with the specified visual appearance. |
| `void` | `addDataSet(DataSet ds, String title, Color color, boolean drawLine, boolean fillAreaUnderLine, Chart.InterpolationType interpolationType, double lineWidth, Chart.PointStyle pointStyle)` | Deprecated. this method will be removed in the next releases. |
| `void` | `addDataSet(DataSet ds, String title, Color color, boolean drawLine, Chart.InterpolationType interpolationType, double lineWidth, Chart.PointStyle pointStyle)` | Adds a DataSet to the chart with the specified visual appearance. |
| `Chart2DPlot.Appearance` | `getAppearance(int i)` | Returns the appearance of the chart item (DataSet) with the given index. |
| `Color` | `getColor(int i)` | Returns the color of the chart item with the given index. |
| `void` | `setColor(int i, Color c)` | Sets the new color of the chart item with the given index. |
| `void` | `setFixedVerticalScale(double minimum, double maximum)` | Sets fixed scale for vertical axis of chart |
