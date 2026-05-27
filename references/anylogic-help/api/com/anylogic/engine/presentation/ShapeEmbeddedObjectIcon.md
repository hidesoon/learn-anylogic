*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeEmbeddedObjectIcon.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeEmbeddedObjectIcon

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeEmbeddedObjectIcon

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
@AnyLogicInternalAPI
public class ShapeEmbeddedObjectIcon
extends Shape
```

Persistent presentation of Embedded Object icon shape plus some info.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeEmbeddedObjectIcon)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeEmbeddedObjectIcon(Agent agent, boolean ispublic, double x, double y, Agent embeddedObject)` | Constructs an embedded object presentation with specific attributes |
| `ShapeEmbeddedObjectIcon(Agent agent, boolean ispublic, double x, double y, AgentList<?> population)` | Constructs an embedded object presentation with specific attributes |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final Shape` | `clone()` | This method is not supported and throws exception:  Embedded object icon cannot be cloned |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `deactivate()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Tells the shape to forget about its current embedded object. |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Agent` | `getEmbeddedObject()` | Returns the embedded object drawn by this shape |
| `AgentList<?>` | `getPopulation()` |  |
| `Agent` | `getPresentable()` | Returns the presentable ([`Agent`](../Agent.md "class in com.anylogic.engine")) where this shape belongs to. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `void` | `resetSVGComponent()` |  |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
