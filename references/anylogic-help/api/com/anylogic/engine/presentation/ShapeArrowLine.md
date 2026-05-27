*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeArrowLine.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeArrowLine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeLine](ShapeLine.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeArrowLine

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Segment2D`, `Segment3D`, `Serializable`, `Cloneable`

---

```
public class ShapeArrowLine
extends ShapeLine
```

A line shape with optional arrows.
The arrows may be set at the beginning of the line, at the end, or both.
An arrow can optionally be offset from the beginning or end e.g. positioned in the middle.
The style and size of the arrows is set up manually and is not automatically adjusted to the line width.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeArrowLine)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeArrowLine()` | Constructs an arrow line with the default attributes (no arrows). |
| `ShapeArrowLine(ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, Paint color, double dx, double dy, double dz, double width, double zHeight, LineStyle style, LineArrowStyle beginArrowStyle, double beginArrowOffset, double beginArrowLength, double beginArrowWidth, LineArrowStyle endArrowStyle, double endArrowOffset, double endArrowLength, double endArrowWidth)` | Constructs an arrow line with specific attributes and arrows. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `float` | `getBeginArrowLength()` | Returns the begin arrow length. |
| `float` | `getBeginArrowOffset()` | Returns the begin arrow offset, 0..1. |
| `LineArrowStyle` | `getBeginArrowStyle()` | Returns the begin arrow style, one of [`LineArrowStyle`](LineArrowStyle.md "enum class in com.anylogic.engine.presentation"). |
| `float` | `getBeginArrowWidth()` | Returns the begin arrow width. |
| `float` | `getEndArrowLength()` | Returns the end arrow length. |
| `float` | `getEndArrowOffset()` | Returns the end arrow offset, 0..1. |
| `LineArrowStyle` | `getEndArrowStyle()` | Returns the end arrow style, one of [`LineArrowStyle`](LineArrowStyle.md "enum class in com.anylogic.engine.presentation"). |
| `float` | `getEndArrowWidth()` | Returns the end arrow width. |
| `void` | `setBeginArrowLength(double beginArrowLength)` | Sets the begin arrow length. |
| `void` | `setBeginArrowOffset(double beginArrowOffset)` | Sets the offset of the begin arrow from the beginning of the line in the form of a fraction of the line length. |
| `void` | `setBeginArrowStyle(LineArrowStyle beginArrowStyle)` | Sets the begin arrow style. |
| `void` | `setBeginArrowWidth(double beginArrowWidth)` | Sets the end arrow width. |
| `void` | `setEndArrowLength(double endArrowLength)` | Sets the end arrow length. |
| `void` | `setEndArrowOffset(double endArrowOffset)` | Sets the offset of the end arrow from the beginning of the line in the form of a fraction of the line length. |
| `void` | `setEndArrowStyle(LineArrowStyle endArrowStyle)` | Sets the end arrow style. |
| `void` | `setEndArrowWidth(double endArrowWidth)` | Sets the end arrow width. |
