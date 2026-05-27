*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/NetworkPortImpl.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class NetworkPortImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Node](Node.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.NetworkPortImpl

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<Node,Path>`, `LevelElement`, `LevelMarkup`, `MarkupPort`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>`, `NetworkPort`, `SVGElement`, `UsdElement`, `Serializable`

---

```
@AnyLogicInternalAPI
public class NetworkPortImpl
extends Node
implements NetworkPort, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.NetworkPortImpl)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `NetworkPortImpl(Agent owner, ShapeDrawMode drawMode, boolean isPublic, PathEnd<Path> pathEnd)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection(Path path, PathEndType type)` |  |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`Node.getLineTexture()`](Node.md#getLineTexture()) should be used instead) |
| `Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `double` | `getNearestPoint(double x, double y, double z, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `MarkupPort` | `getPairedPort()` | Returns the paired port for this markup port. |
| `Position` | `getPosition()` |  |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `Position` | `getPosition(Position out)` |  |
| `double` | `getX()` |  |
| `Point` | `getXYZ()` |  |
| `Point` | `getXYZ(Point out)` |  |
| `double` | `getY()` |  |
| `double` | `getZ()` | Returns the z coordinate of the node. |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `setLineColor(Color lineColor)` | Sets the line color of the markup element. |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setPairedPort(MarkupPort pairedPort)` | Sets the paired port for this markup port. |
