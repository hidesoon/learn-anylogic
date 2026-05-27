*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Chart.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Chart<E extends ChartItem>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.analysis.Chart<E>

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Chart1D`, `Chart2D`, `Histogram`, `Histogram2D`

---

```
public abstract class Chart<E extends ChartItem>
extends ShapeControl
```

The base class for all charts.
Is responsible for the chart overall layout, and for the chart legend functionality.
Delegates the drawing of the chart to its subclasses.
The chart area is divided into two parts: the picture area (where the picture, like
plot, pie, bar, histogram, etc. is drawn) and the legend area. The legend can be
located on either of the four sides of the chart (NORTH, SOUTH, EAST, WEST), or
absent (NONE). The picture can be located at arbitrary position within the picture
area, i.e. the part of the chart not occupied by the legend.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Chart)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `Chart.Direction` | multipurpose direction/position constants |
| `static enum` | `Chart.GridPosition` | grid text position constants |
| `static enum` | `Chart.InterpolationType` | interpolation types |
| `static enum` | `Chart.LegendOrientation` |  |
| `static enum` | `Chart.PointStyle` | line point styles |
| `static enum` | `Chart.ScaleType` | scale types |
| `static enum` | `Chart.TimeWindowMovementType` |  |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `DEFAULT_DATE_PATTERN` |  |
| `static final String` | `DEFAULT_DATE_TIME_PATTERN` |  |
| `static final String` | `DEFAULT_TIME_PATTERN` |  |
| `static final Chart.Direction` | `EAST` |  |
| `static final Chart.GridPosition` | `GRID_DEFAULT` |  |
| `static final Chart.GridPosition` | `GRID_NONE` |  |
| `static final Chart.GridPosition` | `GRID_OPPOSITE` |  |
| `static final Chart.InterpolationType` | `INTERPOLATION_LINEAR` |  |
| `static final Chart.InterpolationType` | `INTERPOLATION_STEP` |  |
| `static final Chart.LegendOrientation` | `LEGEND_HORIZONTAL` |  |
| `static final Chart.LegendOrientation` | `LEGEND_VERTICAL` |  |
| `static final Chart.Direction` | `NONE` |  |
| `static final Chart.Direction` | `NORTH` |  |
| `static final Chart.PointStyle` | `POINT_CIRCLE` |  |
| `static final Chart.PointStyle` | `POINT_NONE` |  |
| `static final Chart.PointStyle` | `POINT_SQUARE` |  |
| `static final Chart.PointStyle` | `POINT_TRIANGLE` |  |
| `static final Chart.ScaleType` | `SCALE_100_PERCENT` |  |
| `static final Chart.ScaleType` | `SCALE_AUTO` |  |
| `static final Chart.ScaleType` | `SCALE_FIXED` |  |
| `static final String` | `SHORT_DATE_PATTERN` |  |
| `static final String` | `SHORT_DATE_TIME_PATTERN` |  |
| `static final String` | `SHORT_TIME_PATTERN` |  |
| `static final Chart.Direction` | `SOUTH` |  |
| `static final Chart.Direction` | `WEST` |  |
| `static final Chart.TimeWindowMovementType` | `WINDOW_MOVES_WITH_DATA` |  |
| `static final Chart.TimeWindowMovementType` | `WINDOW_MOVES_WITH_TIME` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Chart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, Chart.LegendOrientation orientation, List<String> titles)` |  |
| `Chart(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, List<String> titles)` | Creates a persistent chart. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `action()` | Does nothing: no actions are associated with charts. |
| `final Shape` | `clone()` | **Cloning of charts is not supported**  (Other shapes except GIS and controls allow cloning)  This method throws `UnsupportedOperationException` if called |
| `String` | `copyToClipboard()` | Deprecated. will be removed in the future release. |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final E` | `get(int i)` | Returns the chart item (DataItem, DataSet, HistogramData, etc.) with the given index. |
| `abstract Color` | `getColor(int i)` | Returns the color of the chart item with the given index. |
| `final int` | `getCount()` | Returns the number of chart items (data items or data sets) currently displayed by this chart. |
| `JComponent` | `getJComponent()` | Deprecated. This function is deprecated and will be removed in the future. |
| `int[]` | `getSelectedItemIndices()` | Returns an array with indices of selected chart items |
| `final String` | `getTitle(int i)` | Returns the title of chart item (DataItem, DataSet, HistogramData, etc.) with the given index. |
| `void` | `onSelectionChanged_xjal(int[] selectedIndices, boolean programmatically)` | Executes specific action when user clicks on legend and selects/deselects chart item(s).  This method does nothing by default and may be overridden for charts they have any on-selection-changed activity. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `refresh()` | Deprecated. |
| `final void` | `remove(int i)` | Removes the item (DataItem, DataSet, HistogramData, etc.) with the given index from the chart. |
| `final int` | `remove(ChartItem ci)` | Removes the given item (DataItem, DataSet, HistogramData, Histogram2DData) from the chart. |
| `void` | `removeAll()` | Removes all items from the chart. |
| `void` | `selectItem(int itemIndex, boolean selected)` | Selects/deselects (depending on `selected` value) chart item with given index |
| `void` | `setColor(int i, Color c)` | Sets the new color of the chart item with the given index. |
| `void` | `setLegendOrientation(Chart.LegendOrientation orientation)` |  |
| `void` | `setSelectedItemIndices(int[] selectedIndices)` | Selects only chart items with given indices |
| `void` | `update()` | Deprecated. **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `updateData()` | Updates all data items / data sets displayed by this chart. |
