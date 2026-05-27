*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeEmbeddedObjectPresentation.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeEmbeddedObjectPresentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeEmbeddedObjectPresentation

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Preview3dShapeEmbeddedObjectPresentation`

---

```
public class ShapeEmbeddedObjectPresentation
extends Shape3D
```

Persistent presentation of Embedded Object shape. Contains a single shape -
top-level presentation group of embedded object. May not be replicated. The
user can add, remove and change shapes in the group dynamically.
Shapes contained in a group have reference to that group.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeEmbeddedObjectPresentation)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeEmbeddedObjectPresentation(Agent agent, ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, boolean drawAgentWithOffset, boolean scaleIsAutomatic, Agent embeddedObject)` | Constructs an embedded object presentation with specific attributes |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final Shape` | `clone()` | This method is not supported and throws exception:  Embedded object presentation cannot be cloned |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `deactivate()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Tells the shape to forget about its current embedded object. |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Agent` | `getEmbeddedObject()` | Returns the embedded object drawn by this shape |
| `Agent` | `getPresentable()` | Returns the presentable ([`Agent`](../Agent.md "class in com.anylogic.engine")) where this shape belongs to. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `boolean` | `isScaleAutomatic()` |  |
| `boolean` | `isVisibleCurrently()` | Takes into account visibility of the [`Level`](../markup/Level.md "class in com.anylogic.engine.markup") |
| `boolean` | `isZeroOrigin_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetSVGComponent()` |  |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setActive(boolean active)` |  |
| `void` | `setAgentVisible(boolean v)` | Hides or shows the embedded object presentation. |
| `void` | `setEmbeddedObject_xjal(Agent embeddedObject)` |  |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
