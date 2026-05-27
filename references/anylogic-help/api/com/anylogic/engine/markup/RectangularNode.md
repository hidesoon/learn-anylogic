*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RectangularNode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class RectangularNode<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Node](Node.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AreaNode](AreaNode.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.RectangularNode<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `IAreaNodeDescriptor<T>`, `IDescriptor`, `HasBoundingRectangle`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<Node,Path>`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>`, `SVGElement`, `UsdElement`, `Serializable`, `Iterable<T>`

---

```
public class RectangularNode<T extends Agent>
extends AreaNode<T>
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.RectangularNode)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RectangularNode()` |  |
| `RectangularNode(Agent owner)` |  |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double width, double height, double rotation, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, boolean limitSpeed, double maxSpeedInMPS, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double width, double height, double rotation, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double width, double height, double rotation, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double width, double height, double rotation, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, boolean limitSpeed, double maxSpeedInMPS, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double width, double height, double rotation, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double width, double height, double rotation, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, IAreaNodeDescriptor<T> descriptor, double x, double y, double z, double width, double height, double rotation, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` |  |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, IAreaNodeDescriptor<T> descriptor, double x, double y, double z, double width, double height, double rotation, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode, PathEnd<Path>[] pathEnds, Attractor... attractors)` |  |
| `RectangularNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, IAreaNodeDescriptor descriptor, double x, double y, double z, double width, double height, double rotation, Slope slope, Paint fillColor, Paint lineColor, double lineWidth, LineStyle lineStyle, PositionChoiceMode positionChoiceMode)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `area(AreaUnits units)` | Returns the area of this area, measured in area units |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Point` | `getCenter()` | Returns coordinates of the rectangle center. |
| `Point` | `getCenter(Point p)` | Returns coordinates of the rectangle center. |
| `double` | `getHeight()` | Returns the height of the markup shape. |
| `double` | `getNearestPoint(double x, double y, double z, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double px, double py, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `Point[]` | `getPoints()` |  |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `double` | `getRotation()` | Returns the rotation of the shape. |
| `double` | `getWidth()` | Returns the width of the markup shape. |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `setRotation(double rotation)` | Sets the rotation of the shape. |
| `void` | `setSize(double width, double height)` | Sets the width and height of the markup shape. |
| `Area3D` | `toArea3D()` | Returns the 3D representation of this area |
