*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeScale.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeScale

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeScale

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeScale
extends Shape
```

This shape draws [`Scale`](../Scale.md "class in com.anylogic.engine") of the agent on its animation

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeScale)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeScale(Agent owner, boolean ispublic, double x, double y, double rotation, double length, LengthUnits displayedUnits)` | Constructs a text shape with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `LengthUnits` | `getDisplayedUnits()` |  |
| `double` | `getLength()` |  |
| `Agent` | `getOwner()` |  |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setDisplayedUnits(LengthUnits displayedUnits)` |  |
| `void` | `setLength(double length)` |  |
