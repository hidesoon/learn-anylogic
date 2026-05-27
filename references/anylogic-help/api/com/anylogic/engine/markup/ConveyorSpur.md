*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorSpur.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorSpur<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorPathPart](ConveyorPathPart.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorSpur<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `INetworkMarkupElement`, `MarkupPort`, `NetworkPort`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ConveyorSpur<T extends Agent>
extends ConveyorPathPart<T>
implements NetworkPort, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorSpur)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorSpur(ConveyorPath<? extends T> conveyor, ShapeDrawMode drawMode, boolean isPublic, double offsetInPixels, boolean isOnRightSide, Paint lineColor, Paint fillColor)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `ConveyorPath<?>` | `getConnectedPath()` |  |
| `double` | `getConnectionAngle()` |  |
| `Color` | `getFillColor()` | Returns the fill color of the shape, or `null` if the shape has no color or uses a texture (in this case use [getLineTexture()](#getLineTexture()) to get the shape's texture). |
| `Texture` | `getFillTexture()` | Returns the fill texture of the shape or `null` if the shape has no texture but uses a color (in this case use [getLineColor()](#getLineColor()) to get the shape's color). |
| `double` | `getItemEnterOffset()` |  |
| `double` | `getItemEnterOffset(LengthUnits units)` |  |
| `Color` | `getLineColor()` | Returns the line color of the shape, or `null` if the shape has no color or uses a texture (in this case use [getLineTexture()](#getLineTexture()) to get the shape's texture). |
| `Texture` | `getLineTexture()` | Returns the line texture of the shape or `null` if the shape has no texture but uses a color (in this case use [getLineColor()](#getLineColor()) to get the shape's color). |
| `double` | `getMergeLength()` |  |
| `double` | `getMergeLength(LengthUnits units)` |  |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates the distance to the `givenPoint` and writes the nearest point (same as [spur coordinates](#getXYZ())) to the output `Point` object. |
| `MarkupPort` | `getPairedPort()` | Returns the paired port for this conveyor spur. |
| `ConveyorPath<T>` | `getTransition()` |  |
| `double` | `getX()` |  |
| `Point` | `getXYZ()` | Returns the `Point` where the spur connects to main conveyor. |
| `double` | `getY()` |  |
| `double` | `getZ()` |  |
| `boolean` | `isMerge()` |  |
| `boolean` | `isOnRightSide()` | Returns `true` if the conveyor spur is situated on the right-hand side of the main conveyor. |
| `boolean` | `isSplit()` |  |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns `Point` equal to [spur coordinates](#getXYZ()) and writes result to `out`. |
| `void` | `setFillColor(Paint fillColor)` | Sets the fill color (or texture) of the shape. |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or texture) of the shape. |
| `void` | `setOffset(double offset, LengthUnits units)` | Sets the distance from the starting point of the main conveyor to the center of the conveyor spur element (in the specified length units). |
| `void` | `setOnRightSide(boolean isOnRigthSide)` | Sets the conveyor spur element on the right-hand side of the main conveyor. |
| `void` | `setPairedPort(MarkupPort pairedPort)` | Sets the paired port for this conveyor spur. |
