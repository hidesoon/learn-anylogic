*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeInspect.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeInspect

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeInspect

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeInspect
extends Shape
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeInspect)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static final record` | `ShapeInspect.FakeInspectedShape` |  |

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ShapeGroup` | `getGroup()` | Returns the group containing this shape. |
| `Object` | `getInspectedShape()` |  |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `boolean` | `isVisibleCurrently()` | Takes into account visibility of the [`Level`](../markup/Level.md "class in com.anylogic.engine.markup") |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `setSize(double width, double height)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
