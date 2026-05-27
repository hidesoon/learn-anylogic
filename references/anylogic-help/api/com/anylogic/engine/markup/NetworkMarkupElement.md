*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/NetworkMarkupElement.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class NetworkMarkupElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.NetworkMarkupElement

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `INetworkMarkupElement`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `Node`, `PalletRack`, `Path`

---

```
@AnyLogicInternalAPI
public abstract class NetworkMarkupElement
extends MarkupShape
implements INetworkMarkupElement
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.NetworkMarkupElement)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `NetworkMarkupElement()` |  |
| `NetworkMarkupElement(Agent owner)` |  |
| `NetworkMarkupElement(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  If the shape has been created with no-argument constructor, and has no specific limitations (like 2D-only), and drawing mode hasn't yet been set, then it is initialized to default (2D + 3D). |
| `Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
| `double` | `getNearestPoint(double x, double y, double z, LengthUnits units, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `abstract double` | `getNearestPoint(double x, double y, double z, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, LengthUnits units, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `abstract double` | `getNearestPoint(double x, double y, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `Network` | `getNetwork()` |  |
| `void` | `setLevel(Level level)` | Sets the level of this element. |
| `void` | `setNetwork(Network network, int index)` |  |
