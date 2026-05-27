*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Histogram2D.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Histogram2D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[Histogram2DData](Histogram2DData.md "class in com.anylogic.engine.analysis")>

com.anylogic.engine.analysis.Histogram2D

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class Histogram2D
extends Chart<Histogram2DData>
```

The chart that displays a collection of two-dimensional histograms. Each histogram
is drawn as a number of rectangular color spots reflecting the PDF value or envelope
at the corresponding (X,Y). The chart X and Y axis are always scaled to fit all histograms.
The chart has a collection of Histogram2DData objects and the collection of associated
visual appearance descriptions. The chart may have scale text labels and a grid.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Histogram2D)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `Histogram2D.Appearance` | Descriptor or histogram 2D appearance. |

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Histogram2D(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, Chart.GridPosition gridPositionX, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, boolean drawEnvelopes, List<Histogram2DData> data, List<String> titles, List<Histogram2D.Appearance> appearances)` | Creates a persistent Histogram2D. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addHistogram2D(Histogram2DData hist, String title, Color color)` | Adds a histogram 2D data object to the chart with the specified visual appearance. |
| `Color` | `getColor(int i)` | Returns the color of the 2D histogram item with the given index. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `setColor(int i, Color c)` | Sets the new color of the 2D histogram item with the given index. |
