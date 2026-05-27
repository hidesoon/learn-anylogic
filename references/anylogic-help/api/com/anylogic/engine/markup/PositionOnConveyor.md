*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PositionOnConveyor.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class PositionOnConveyor<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorPathPart](ConveyorPathPart.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.PositionOnConveyor<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.IMaterialPointLocation<T>`, `com.anylogic.engine.markup.material_handling.IPositionOnConveyorDescriptor<T>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class PositionOnConveyor<T extends Agent>
extends ConveyorPathPart<T>
implements com.anylogic.engine.markup.material_handling.IPositionOnConveyorDescriptor<T>, AbstractPositionalMarkup
```

Position on conveyor is the graphical element that is used to define the exact position on the conveyor.

It can be used to:

* Define the location where new material items will be placed on the conveyor (by the Convey and ConveyorEnter blocks).
  Note that both blocks place the leading edge of the added material item at the Position on conveyor location.
* Set the destination point for the material items being transported by conveyor(s) (in the Convey block).
* Simulate photo-eyes, scanners and other devices that perform some instant actions with the conveyed material items.
  To model the operation, use the callbacks actions in the element's Actions properties section.
  If the operation requires some time, use station instead.
* Model different types of stops and escapement devices (e.g. blade stop, claw stop, pneumatic escapements).
  You can simulate the conveyor blocking and unblocking operations by calling the element's block() and unblock() functions.

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.PositionOnConveyor)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PositionOnConveyor(ConveyorPath<? extends T> conveyor)` |  |
| `PositionOnConveyor(ConveyorPath<? extends T> conveyor, double offset)` | Constructor |
| `PositionOnConveyor(ConveyorPath<? extends T> conveyor, ShapeDrawMode drawMode, boolean isPublic, double offset, com.anylogic.engine.markup.material_handling.IPositionOnConveyorDescriptor<T> descriptor)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `block()` | Blocks the conveyor movement. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(Agent agent)` | Returns true if the given agent (material item) is currenty located at the position on conveyor, returns false otherwise. |
| `T` | `getAgent()` | Returns the agent (material item) that is currenty located at the position on conveyor, returns null if none. |
| `com.anylogic.engine.markup.material_handling.IPositionOnConveyorDescriptor<T>` | `getLibraryDescriptor()` |  |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `double` | `getX()` |  |
| `double` | `getY()` |  |
| `double` | `getZ()` |  |
| `boolean` | `isBlocked()` | Returns true if this Position on conveyor element is currently set to block the conveyor movement., returns false otherwise. |
| `void` | `onCellEnter()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onCellExit()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onLeadingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onTrailingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `T` | `removeAgent()` | Removes the agent from the conveyor. |
| `void` | `unblock()` | Unblocks the conveyor movement. |
