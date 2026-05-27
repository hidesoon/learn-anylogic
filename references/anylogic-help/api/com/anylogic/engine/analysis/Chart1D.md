*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Chart1D.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Chart1D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataItem](DataItem.md "class in com.anylogic.engine.analysis")>

com.anylogic.engine.analysis.Chart1D

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `BarChart`, `Chart1DSum`

---

```
public abstract class Chart1D
extends Chart<DataItem>
```

The base class for all charts that display a collection of single data items,
like Pie, Bar, or Stack. Has a collection of DataItem objects and a collection
of their colors. The legend values of data items are set to
[title]: [value].

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Chart1D)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Chart1D(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, List<DataItem> dataItems, List<String> titles, List<Color> colors)` | Creates a persistent Chart1D. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addDataItem(DataItem di)` | Adds a DataItem to the chart with default title and color. |
| `void` | `addDataItem(DataItem di, String title, Color color)` | Adds a data item to the chart. |
| `Color` | `getColor(int i)` | Returns the color of the chart item with the given index. |
| `void` | `setColor(int i, Color c)` | Sets the new color of the chart item with the given index. |
