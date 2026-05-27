*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorCustomStation.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorCustomStation<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorNode](ConveyorNode.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorCustomStation<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<ConveyorNode<?>,ConveyorPath<?>>`, `com.anylogic.engine.markup.material_handling.IConveyorCustomStationDescriptor<T>`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ConveyorCustomStation<T extends Agent>
extends ConveyorNode<T>
implements com.anylogic.engine.markup.material_handling.IConveyorCustomStationDescriptor<T>
```

Custom station is the space markup element used in material handling models.
It defines a station / working zone where material items are processed.
The process is not set up in this block, you should define it on your own ( Process Modeling Library and Material Handling Library blocks).

If the processing can be defined simply as a delay for the specified time, use the Station element instead.

Custom station is a part of a conveyor network.
Custom station can act as a transit point in a conveyor network, any number of conveyors can lead to/from the custom station.
It can also be a destination for material items transportation defined by the Convey block.

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorCustomStation)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorCustomStation()` |  |
| `ConveyorCustomStation(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `ConveyorCustomStation(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double[] dx, double[] dy, Paint fillColor, Paint lineColor, com.anylogic.engine.markup.material_handling.IConveyorCustomStationDescriptor<T> descriptor, PathEnd<ConveyorPath<?>>... pathEnds)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addVertex(double x, double y)` | Add vertex to build the 2D polygon that will represent this markup. |
| `ConveyorCustomStationAgentLocation` | `agentLocation(T agent)` |  |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Point` | `getCenter()` | Returns the point at the center of this markup |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `double` | `getTransferDistance(ConveyorPath<?> path1, ConveyorPath<?> path2)` |  |
| `void` | `onEnter(T agent)` |  |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `setCenter(Point point)` | Deprecated. |
