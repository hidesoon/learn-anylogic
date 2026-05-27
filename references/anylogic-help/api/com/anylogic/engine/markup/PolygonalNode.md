*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PolygonalNode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class PolygonalNode<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Node](Node.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AreaNode](AreaNode.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.PolygonalNode<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `IAreaNodeDescriptor<T>`, `IDescriptor`, `HasBoundingRectangle`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<Node,Path>`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>`, `SVGElement`, `UsdElement`, `Serializable`, `Iterable<T>`

Direct Known Subclasses:
:   `QueueArea`

---

```
public class PolygonalNode<T extends Agent>
extends AreaNode<T>
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.PolygonalNode)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PolygonalNode()` |  |
| `PolygonalNode(Agent owner)` |  |
| `PolygonalNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, boolean limitSpeed, double maxSpeedInMPS, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PolygonalNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PolygonalNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PolygonalNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, boolean limitSpeed, double maxSpeedInMPS, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PolygonalNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PolygonalNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PolygonalNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, IAreaNodeDescriptor<T> descriptor, double x, double y, double z, double[] dx, double[] dy, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` |  |
| `PolygonalNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, IAreaNodeDescriptor<T> descriptor, double x, double y, double z, double[] dx, double[] dy, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addVertex(double x, double y)` | Adds a point to the collection of vertices that will be used to initialize the polygon of this node. |
| `double` | `area(AreaUnits units)` | Returns the area of this area, measured in area units |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getNearestPoint(double x, double y, double z, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double px, double py, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `int` | `getNPoints()` | Returns the number of points in the markup element. |
| `double` | `getPointDx(int i)` | Returns the x coordinate of a particular point of the markup element relative to the start point. |
| `double` | `getPointDy(int i)` | Returns the y coordinate of a particular point of the markup element relative to the start point. |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `double` | `getXMax()` | Returns the x coordinate of the bottom-right corner of bounding rectangle for this markup element. |
| `double` | `getXMin()` | Returns the x coordinate of the top-left corner of bounding rectangle for this markup element. |
| `double` | `getYMax()` | Returns the y coordinate of the bottom-right corner of bounding rectangle for this markup element. |
| `double` | `getYMin()` | Returns the y coordinate of the top-left corner of bounding rectangle for this markup element. |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
