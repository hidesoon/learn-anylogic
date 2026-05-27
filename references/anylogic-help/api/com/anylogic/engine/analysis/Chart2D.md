*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Chart2D.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Chart2D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataSet](DataSet.md "class in com.anylogic.engine.analysis")>

com.anylogic.engine.analysis.Chart2D

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Chart2DPlot`, `TimeColorChart`, `TimeStackChart`

---

```
public abstract class Chart2D
extends Chart<DataSet>
```

The base class for all charts that display a collection of two-dimensional data sets,
like Plot, TimePlot, TimeStack, Color. Has a collection of DataSet objects. The chart
may have scale text labels and a grid.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Chart2D)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Chart2D(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, Chart.ScaleType scaleTypeY, double minimumY, double maximumY, Chart.GridPosition gridPositionX, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles)` | Creates a persistent Chart2D. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
