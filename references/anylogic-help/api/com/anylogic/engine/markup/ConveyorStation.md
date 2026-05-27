*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorStation.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorStation<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorPathPart](ConveyorPathPart.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorStation<T>

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `INetworkMarkupElement`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `ConveyorSimpleStation`

---

```
public abstract class ConveyorStation<T extends Agent>
extends ConveyorPathPart<T>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorStation)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorStation(ConveyorPath<? extends T> conveyor)` |  |
| `ConveyorStation(ConveyorPath<? extends T> conveyor, double offset, double lengthInMeters)` | Constructor |
| `ConveyorStation(ConveyorPath<? extends T> conveyor, ShapeDrawMode drawMode, boolean isPublic, double offset, double lengthInMeters)` | Constructor |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getLength(LengthUnits units)` | Returns the length of this element |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `setLength(double length, LengthUnits units)` | Sets length of this conveyor part in XY-projection, measured in the given units. |
| `void` | `setNetwork(ConveyorNetwork network)` | Sets the network for this element. |
