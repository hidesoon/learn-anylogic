*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PedFlowStatistics.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class PedFlowStatistics

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.PedFlowStatistics

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class PedFlowStatistics
extends AbstractLevelMarkup
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.PedFlowStatistics)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PedFlowStatistics()` |  |
| `PedFlowStatistics(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double sx, double sy, double ex, double ey, FlowStatisticsDirection direction, Color color)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `long` | `countPeds()` | Returns total number of pedestrians passed through this line |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Color` | `getColor()` | Returns the color of the markup element, or `null` if markup element has no color |
| `FlowStatisticsDirection` | `getDirection()` | Returns the current flow direction, for which this element collects statistics. |
| `final double` | `getEndX()` | Returns the x coordinate of the end point |
| `final double` | `getEndY()` | Returns the y coordinate of the start point |
| `final double` | `getStartX()` | Returns the x coordinate of the start point |
| `final double` | `getStartY()` | Returns the y coordinate of the start point |
| `double` | `intensity()` | Returns the average pedestrian flow intensity on the line, measured in pedestrians per hour per meter |
| `void` | `onDestroy()` |  |
| `void` | `reset()` | Resets the average traffic and intensity. |
| `void` | `setColor(Color color)` | Sets the color of the markup element. |
| `void` | `setDataSource(PedFlowStatisticsDataSource dataSource)` |  |
| `void` | `setDirection(FlowStatisticsDirection direction)` | Sets the flow direction, for which this element will collect statistics. |
| `void` | `setEndPoint(double x, double y)` | Sets the coordinates of the end point |
| `void` | `setStartPoint(double x, double y)` | Sets the coordinates of the start point |
| `double` | `traffic()` | Returns the average of traffic flow statistics through the line, measured in pedestrians per hour |
