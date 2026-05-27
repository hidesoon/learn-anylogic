*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ElevatorShaft.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ElevatorShaft

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../presentation/Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](../presentation/Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.markup.ElevatorShaft

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
@AnyLogicInternalAPI
public class ElevatorShaft
extends Shape3D
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ElevatorShaft)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ElevatorShaft(Elevator<?> elevator, Level level)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Elevator<?>` | `getElevator()` |  |
| `ShapeInspect` | `getInspect()` |  |
| `boolean` | `isFrontDoorOpen()` |  |
| `boolean` | `isRearDoorOpen()` |  |
| `boolean` | `onClick(double clickx, double clicky)` | Should be overridden to define the shape reaction on mouse click. |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `setFrontDoorOpen(boolean frontDoorOpen)` |  |
| `void` | `setLineColor(Paint lineColor)` |  |
| `void` | `setPlatformColor(Paint platformColor)` |  |
| `void` | `setRearDoorOpen(boolean rearDoorOpen)` |  |
| `void` | `setZHeight(double zHeight)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
