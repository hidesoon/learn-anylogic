*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/TimePlot.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class TimePlot

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataSet](DataSet.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart2D](Chart2D.md "class in com.anylogic.engine.analysis")

[com.anylogic.engine.analysis.Chart2DPlot](Chart2DPlot.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.TimePlot

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class TimePlot
extends Chart2DPlot
```

The chart that displays a collection of data sets as plots - polylines with point at
each data point and straight lines in between. The data set X (time) values must be
non-decreasing. The time axis shows the data in the specified time window. The chart
has a collection of DataSet objects and the collection of associated visual appearance
descriptions. The chart may have scale text labels and a grid for both axes.

Chart may display date labels on the time axis (model date instead of model time).
To turn on this mode please provide not `null` `dateFormatPattern`
using one of available constants (`DEFAULT_TIME_PATTERN`, `DEFAULT_DATE_PATTERN`
or `DEFAULT_DATE_TIME_PATTERN`) or the following
Format Pattern Syntax:
(see also [`SimpleDateFormat`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/SimpleDateFormat.html "class or interface in java.text"))

Text can be quoted using single quotes (`'`) to avoid
interpretation.
`"''"` represents a single quote.

The following pattern letters are defined (all other characters from
`'A'` to `'Z'` and from `'a'` to
`'z'` are reserved):

> | Letter | Date or Time Component | Presentation | Examples |
> | --- | --- | --- | --- |
> | `G` | Era designator | [Text](#text) | `AD` |
> | `y` | Year | [Year](#year) | `1996`; `96` |
> | `M` | Month in year | [Month](#month) | `July`; `Jul`; `07` |
> | `w` | Week in year | [Number](#number) | `27` |
> | `W` | Week in month | [Number](#number) | `2` |
> | `D` | Day in year | [Number](#number) | `189` |
> | `d` | Day in month | [Number](#number) | `10` |
> | `F` | Day of week in month | [Number](#number) | `2` |
> | `E` | Day in week | [Text](#text) | `Tuesday`; `Tue` |
> | `a` | Am/pm marker | [Text](#text) | `PM` |
> | `H` | Hour in day (0-23) | [Number](#number) | `0` |
> | `k` | Hour in day (1-24) | [Number](#number) | `24` |
> | `K` | Hour in am/pm (0-11) | [Number](#number) | `0` |
> | `h` | Hour in am/pm (1-12) | [Number](#number) | `12` |
> | `m` | Minute in hour | [Number](#number) | `30` |
> | `s` | Second in minute | [Number](#number) | `55` |
> | `S` | Millisecond | [Number](#number) | `978` |

Pattern letters are usually repeated, as their number determines the
exact presentation:

* Text:
  If the number of pattern letters is 4 or more,
  the full form is used; otherwise a short or abbreviated form
  is used if available.
* Number:
  The number of pattern letters is the minimum
  number of digits, and shorter numbers are zero-padded to this amount.
* Year:
  If the number of pattern letters is 2, the year
  is truncated to 2 digits; otherwise it is interpreted as a
  [number](#number).
* Month:
  If the number of pattern letters is 3 or more, the month is
  interpreted as [text](#text); otherwise,
  it is interpreted as a [number](#number).

*Examples*
> | Date and Time Pattern | Result |
> | --- | --- |
> | `"dd.MM.yyyy HH:mm:ss"` | `07.05.2008 14:49:57` |
> | `"EEE, MMM d, ''yy"` | `Fri, May 7, '08` |
> | `"h:mm a"` | `2:49 PM` |
> | `"yyyy-MM-dd HH:mm:ss.SSS"` | `2008-05-07 14:49:57.304` |

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.TimePlot)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TimePlot(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, double timeWindow, Chart.TimeWindowMovementType timeWindowMovementType, String dateFormatPattern, Chart.ScaleType scaleTypeY, double minimumY, double maximumY, Chart.GridPosition gridPositionT, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles, List<Chart2DPlot.Appearance> appearances)` | Creates a persistent TimePlot. |
| `TimePlot(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, double timeWindow, String dateFormatPattern, Chart.ScaleType scaleTypeY, double minimumY, double maximumY, Chart.GridPosition gridPositionT, Chart.GridPosition gridPositionY, Color gridLineColor, Color gridTextColor, List<DataSet> dataSets, List<String> titles, List<Chart2DPlot.Appearance> appearances)` | Creates a persistent TimePlot. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addDataSet(DataSet ds, String title, Color color, boolean drawLine, boolean fillAreaUnderLine, Chart.InterpolationType interpolationType, double lineWidth, Chart.PointStyle pointStyle)` | Adds a DataSet to the chart with the specified visual appearance. |
| `void` | `refresh()` | Causes the chart to refresh its picture and legend based on the newest data values. |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setFixedVerticalScale(double minimum, double maximum)` | Sets fixed scale for vertical axis of chart |
| `void` | `setIDEDrivenMode_xjal(Date modelStartDate, long modelTimeUnits)` | *This method shouldn't be called by user  (is public due to technical reasons)* |
