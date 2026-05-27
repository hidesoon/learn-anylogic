*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/analysis/Chart1DSum.html>*

---

Package [com.anylogic.engine.analysis](package-summary.md)

# Class Chart1DSum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](../presentation/ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.analysis.Chart](Chart.md "class in com.anylogic.engine.analysis")<[DataItem](DataItem.md "class in com.anylogic.engine.analysis")>

[com.anylogic.engine.analysis.Chart1D](Chart1D.md "class in com.anylogic.engine.analysis")

com.anylogic.engine.analysis.Chart1DSum

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `PieChart`, `StackChart`

---

```
public abstract class Chart1DSum
extends Chart1D
```

A base class for all charts that display the fractions of the data items
of their total (like Pie or Stack). The data items in this chart cannot take
negative values. The legend values of data items are set to
[data item name]: [data item value] ([data item fraction]%).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.analysis.Chart1DSum)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Chart1DSum(Presentable p, boolean ispublic, double x, double y, double width, double height, Color fillColor, Color lineColor, double picOffsetX, double picOffsetY, double picWidth, double picHeight, Color picBackgoundColor, Color picBorderColor, Color legendTextColor, double legendSize, Chart.Direction legendPos, List<DataItem> dataItems, List<String> titles, List<Color> colors)` | Creates a persistent Chart1DSum. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addDataItem(DataItem di, String title, Color color)` | Adds a DataItem to the chart. |
