*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Network.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Network

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupAggregator](AbstractMarkupAggregator.md "class in com.anylogic.engine.markup")<Owner>

[com.anylogic.engine.markup.AbstractNetwork](AbstractNetwork.md "class in com.anylogic.engine.markup")<[Node](Node.md "class in com.anylogic.engine.markup"),[Path](Path.md "class in com.anylogic.engine.markup"),[Agent](../Agent.md "class in com.anylogic.engine")>

com.anylogic.engine.markup.Network

All Implemented Interfaces:
:   `IRouteProvider<ShortestPathData<Node,Path>>`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `INetwork<Node,Path>`, `LevelElement`, `LevelMarkup`, `Serializable`

---

```
public class Network
extends AbstractNetwork<Node,Path,Agent>
implements LevelMarkup, AggregatableAnimationElement, HasBoundingRectangle
```

Implementation of network for agent movement in continuous space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Network)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Network(Agent owner, String name)` | Creates a network with a specified owner and name |
| `Network(Agent owner, String name, ShapeDrawMode drawMode, double z)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases. |
| `Network(Agent owner, String name, ShapeDrawMode drawMode, double z, boolean isPublic, boolean visible)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases. |
| `Network(Agent owner, String name, ShapeDrawMode drawMode, double z, boolean isPublic, boolean visible, NetworkMarkupElement... markupShapes)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(PalletRack palletRack)` | Adds a pallet rack to the network. |
| `void` | `addAll(NetworkMarkupElement... markupShapes)` | Adds all arguments to the network |
| `static NetworkPort` | `createPort(Agent owner, Path path, PathEndType type)` | Deprecated. |
| `Stream<? extends AbstractMarkup>` | `elementsInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `final Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (either 2D, 3D, or 2D&3D).  If the shape has been created with a no-argument constructor, has no specific limitations on the drawing mode (e.g., 2D only), and its drawing mode hasn't been set yet, then it is initialized to the default 2D&3D drawing mode. |
| `Level` | `getLevel()` | Returns the level where this network is located. |
| `List<PalletRack>` | `getPalletRacks()` | Returns [`List`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util") of all [`PalletRack`](PalletRack.md "class in com.anylogic.engine.markup") in the network. |
| `double` | `getPlainDistance(Point firstPoint, Point secondPoint)` | See [`Point.distance(Point)`](../Point.md#distance(com.anylogic.engine.Point)) |
| `Agent` | `getSpace()` | Returns the space where the space markup element is defined |
| `double` | `getZ()` | Returns the z-coordinate of the base level. |
| `void` | `setDrawMode(ShapeDrawMode drawMode)` | Sets the drawing mode of the shape (either 2D, 3D, or 2D&3D).  This method may be called only once and only for the shapes which are created using a no-argument constructor (since they have no limitations on the drawing mode, e.g. |
| `void` | `setLevel(Level level)` | Sets the new level where this network will be located. |
| `void` | `setZ(double z)` | Sets the z-coordinate of the base level. |
