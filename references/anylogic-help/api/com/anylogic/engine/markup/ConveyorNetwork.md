*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorNetwork.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorNetwork

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupAggregator](AbstractMarkupAggregator.md "class in com.anylogic.engine.markup")<Owner>

[com.anylogic.engine.markup.AbstractNetwork](AbstractNetwork.md "class in com.anylogic.engine.markup")<[ConveyorNode](ConveyorNode.md "class in com.anylogic.engine.markup")<?>,[ConveyorPath](ConveyorPath.md "class in com.anylogic.engine.markup")<?>,[Agent](../Agent.md "class in com.anylogic.engine")>

com.anylogic.engine.markup.ConveyorNetwork

All Implemented Interfaces:
:   `IRouteProvider<ShortestPathData<ConveyorNode<?>,ConveyorPath<?>>>`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `INetwork<ConveyorNode<?>,ConveyorPath<?>>`, `LevelElement`, `LevelMarkup`, `Serializable`

---

```
public class ConveyorNetwork
extends AbstractNetwork<ConveyorNode<?>,ConveyorPath<?>,Agent>
implements LevelMarkup, AggregatableAnimationElement, HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorNetwork)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorNetwork(Agent owner, String name)` |  |
| `ConveyorNetwork(Agent owner, String name, ShapeDrawMode drawMode, double z)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases |
| `ConveyorNetwork(Agent owner, String name, ShapeDrawMode drawMode, double z, boolean isPublic, boolean visible)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases |
| `ConveyorNetwork(Agent owner, String name, ShapeDrawMode drawMode, double z, boolean isPublic, boolean visible, ConveyorMarkupElement<?>... contents)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(ConveyorSpur<?> element)` | Adds the spur to the network. |
| `void` | `add(ConveyorStation<?> element)` | Adds the station to the network. |
| `void` | `add(PositionOnConveyor<?> element)` | Adds the position on conveyor to the network. |
| `void` | `addAll(ConveyorMarkupElement<?>... elements)` | Adds elements to this network |
| `static NetworkPort` | `createPort(Agent owner, ConveyorPath<?> path, PathEndType type)` | Deprecated. |
| `Stream<? extends AbstractMarkup>` | `elementsInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  If the shape has been created with no-argument constructor, and has no specific limitations (like 2D-only), and drawing mode hasn't yet been set, then it is initialized to default (2D + 3D). |
| `Level` | `getLevel()` | Returns the level where this conveyor network is located. |
| `double` | `getPlainDistance(Point firstPoint, Point secondPoint)` | Straight line distance between two points. |
| `List<PositionOnConveyor<?>>` | `getPositionsOnConveyors()` | Returns the list of position on conveyor elements belonging to this conveyor network. |
| `Agent` | `getSpace()` | Returns the space where the markup element is defined |
| `List<ConveyorSpur<?>>` | `getSplitMerges()` | Deprecated. will be removed in the next release. |
| `List<ConveyorSpur<?>>` | `getSpurs()` | Returns the list of conveyor spur elements belonging to this conveyor network. |
| `List<ConveyorStation<?>>` | `getStations()` | Returns the list of stations belonging to this conveyor network. |
| `double` | `getZ()` | Returns the base level z coordinate. |
| `void` | `setDrawMode(ShapeDrawMode drawMode)` | Sets the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  This method may be called only for shapes created using no-argument constructor (which have no limitations like 2D-only) and only once. |
| `void` | `setLevel(Level level)` | Sets the new level where this conveyor network will be located. |
| `void` | `setZ(double z)` | Sets the base level z coordinate. |
