*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeLineFill.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeLineFill

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeLineFill

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `ShapeMultiplePoints`, `ShapeOval`, `ShapeRectangle`

---

```
public abstract class ShapeLineFill
extends Shape3D
```

An intermediate base class - for all shapes that have line and fill.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeLineFill)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeLineFill()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Color` | `getFillColor()` | Returns the fill color of the shape, or `null` if shape has no fill color or has textured fill (in this case [`getFillTexture()`](#getFillTexture()) should be used instead) |
| `Texture` | `getFillTexture()` | Returns the fill texture of the shape, if the shape has fill texture |
| `Color` | `getLineColor()` | Returns the line color of the shape, or `null` if shape has no line color or has textured line (in this case [`getLineTexture()`](#getLineTexture()) should be used instead) |
| `LineStyle` | `getLineStyle()` | Returns the line style of the shape: `{LINE_STYLE_SOLID, LINE_STYLE_DOTTED or LINE_STYLE_DASHED}` |
| `Texture` | `getLineTexture()` | Returns the line texture of the shape, if the shape has line texture |
| `double` | `getLineWidth()` | Returns the line width of the shape. |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `double` | `getZHeight()` | Returns the height of the shape along Z-axis |
| `double` | `getZOffset()` | Returns the offset from z coordinate of the location base.  This e.g. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setFillColor(Color fillColor)` | Sets the fill color of the shape. |
| `void` | `setFillColor(Paint fillColor)` | Sets the fill color (or [`Texture`](Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setLineColor(Color lineColor)` | Sets the line color of the shape. |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setLineStyle(LineStyle lineStyle)` | Sets the line style of the shape: `{LINE_STYLE_SOLID, LINE_STYLE_DOTTED or LINE_STYLE_DASHED}` |
| `void` | `setLineWidth(double width)` | Sets the line width of the shape |
| `void` | `setZHeight(double zHeight)` | Sets the height of the shape along Z-axis |
