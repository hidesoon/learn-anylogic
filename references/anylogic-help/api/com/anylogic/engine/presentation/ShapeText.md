*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeText.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeText

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeText

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeText
extends Shape3D
```

Persistent text shape.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeText)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeText()` | Constructs a text shape with default attributes. |
| `ShapeText(boolean ispublic, double x, double y, double rotation, Color color, String text, Font font, TextAlignment alignment)` | Constructs a 2D-only text shape with specific attributes. |
| `ShapeText(ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, Color color, String text, Font font, TextAlignment alignment)` | Constructs a text shape with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeText` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `TextAlignment` | `getAlignment()` | Returns the alignment of the text shape. |
| `Color` | `getColor()` | Returns the color of the text. |
| `Font` | `getFont()` | Returns the font of the text shape. |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `String` | `getText()` | Returns the text of the text shape. |
| `void` | `resetSVGComponent()` |  |
| `void` | `setAlignment(TextAlignment alignment)` | Sets the alignment of the text shape. |
| `void` | `setColor(Color color)` | Sets the color of the text. |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setFont(Font font)` | Sets the font of the text shape. |
| `void` | `setText(Object text)` | Sets the text of the text shape. |
