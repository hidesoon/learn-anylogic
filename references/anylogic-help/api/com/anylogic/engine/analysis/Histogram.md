*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Histogram.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Histogram

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[HistogramData](HistogramData.md "class in com.anylogic.engine.analysis")>

com.anylogic.engine.analysis.Histogram

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class Histogram
extends Chart<HistogramData>
```

The chart that displays a collection of histograms. The X axis always is scaled to
fit all histogram data ranges. The histograms are also scaled along the Y axis so
that the highest bar of each histogram occupies the full height of the picture.
The PDF bars, the CDF line and the mean location can be shown optionally. The chart
has a collection of HistogramData objects and the collection of associated visual
appearance descriptions. The chart may have scale text labels and a grid.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Histogram)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `Histogram.Appearance` | Descriptor or a histogram appearance. |

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Histogram(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, Chart.GridPosition gridPositionX, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, boolean showPDF, boolean showCDF, boolean showMean, double relativeBarWidth, List<HistogramData> data, List<String> titles, List<Histogram.Appearance> appearances)` | Creates a persistent Histogram. |
| `Histogram(Presentable p, boolean ispublic, int x, int y, int width, int height, Color fillColor, Color lineColor, int picOffsetX, int picOffsetY, int picWidth, int picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, int legendSize, Chart.Direction legendPos, Chart.GridPosition gridPositionX, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, boolean showPDF, boolean showCDF, boolean showMean, double relativeBarWidth, List<HistogramData> data, List<String> titles, List<Histogram.Appearance> appearances)` | Deprecated. Will be removed in the next release. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addHistogram(HistogramData hist, String title, Histogram.Appearance appearance)` | Adds a histogram data object to the chart with the specified visual appearance. |
| `void` | `addHistogram(HistogramData hist, String title, Color colorLowPercent, Color colorHighPercent, Color colorPDF, Color colorCDF, float lineWidthCDF, Color colorMean)` | Adds a histogram data object to the chart with the specified visual appearance. |
| `Histogram.Appearance` | `getAppearance(int i)` | Returns the appearance of the chart item (HistogramData) with the given index. |
| `Color` | `getColor(int i)` | Returns the PDF color of the histogram item with the given index. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `refresh()` | Causes the chart to refresh its picture and legend based on the newest data values. |
| `void` | `setColor(int i, Color c)` | Sets the new PDF color of the histogram item with the given index. |
