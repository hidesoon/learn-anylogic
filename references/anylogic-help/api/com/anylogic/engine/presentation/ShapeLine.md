*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeLine.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeLine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeLine

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Segment2D`, `Segment3D`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `ShapeArrowLine`

---

```
public class ShapeLine
extends Shape3D
implements Segment3D
```

A basic line. For line with arrows see [`ShapeArrowLine`](ShapeArrowLine.md "class in com.anylogic.engine.presentation")

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeLine)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeLine()` | Constructs a line with default attributes. |
| `ShapeLine(boolean ispublic, double x, double y, Paint color, double dx, double dy, double width, LineStyle style)` | Constructs a 2D-only line with specific attributes. |
| `ShapeLine(ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, Paint color, double dx, double dy, double dz, double width, double zHeight, LineStyle style)` | Constructs a line with specific attributes. |
| `ShapeLine(ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, Paint color, double dx, double dy, double dz, double width, double zHeight, LineStyle style, LineArrowStyle beginArrowStyle, double beginArrowOffset, double beginArrowLength, double beginArrowWidth, LineArrowStyle endArrowStyle, double endArrowOffset, double endArrowLength, double endArrowWidth)` | Deprecated. this constructor is deprecated since version 8.4 and will be removed in the future. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeLine` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates |
| `float` | `getBeginArrowLength()` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `float` | `getBeginArrowOffset()` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `LineArrowStyle` | `getBeginArrowStyle()` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `float` | `getBeginArrowWidth()` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `Color` | `getColor()` | Returns the color of the line, or `null` if line has no color or has texture (in this case [`getTexture()`](#getTexture()) should be used instead) |
| `double` | `getDx()` | Returns the difference of x coordinates of the line end and start points. |
| `double` | `getDy()` | Returns the difference of y coordinates of the line end and start points. |
| `double` | `getDz()` | Returns the difference of z coordinates of the line end and start points. |
| `float` | `getEndArrowLength()` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `float` | `getEndArrowOffset()` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `LineArrowStyle` | `getEndArrowStyle()` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `float` | `getEndArrowWidth()` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `double` | `getEndX()` | Returns the x coordinate of the line end point. |
| `double` | `getEndY()` | Returns the y coordinate of the line end point. |
| `double` | `getEndZ()` | Returns the z coordinate of the line end point. |
| `double` | `getLength()` | This function is obsolete. |
| `LineStyle` | `getLineStyle()` | Returns the style of the line: LINE\_STYLE\_SOLID, LINE\_STYLE\_DOTTED or LINE\_STYLE\_DASHED |
| `double` | `getLineWidth()` | Returns the width of the line. |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `Texture` | `getTexture()` | Returns the texture of the line, if the line has it |
| `double` | `getZHeight()` | Returns the height of the shape along Z-axis |
| `double` | `getZOffset()` | Returns the offset from z coordinate of the location base.  This e.g. |
| `double` | `length()` | Returns the length of the line. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `resetSVGComponent()` |  |
| `void` | `setBeginArrowLength(double beginArrowLength)` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `void` | `setBeginArrowOffset(double beginArrowOffset)` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `void` | `setBeginArrowStyle(LineArrowStyle beginArrowStyle)` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `void` | `setBeginArrowWidth(double beginArrowWidth)` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `void` | `setColor(Color color)` | Sets the color of the line. |
| `void` | `setColor(Paint color)` | Sets the color (or [`Texture`](Texture.md "class in com.anylogic.engine.presentation")) of the line. |
| `void` | `setContextReference_xjal(Presentable contextReference)` | Deprecated. |
| `void` | `setDx(double dx)` | Sets the difference of x coordinates of the line end and start points. |
| `void` | `setDy(double dy)` | Sets the difference of y coordinates of the line end and start points. |
| `void` | `setDz(double dz)` | Sets the difference of z coordinates of the line end and start points. |
| `void` | `setEndArrowLength(double endArrowLength)` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `void` | `setEndArrowOffset(double endArrowOffset)` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `void` | `setEndArrowStyle(LineArrowStyle endArrowStyle)` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `void` | `setEndArrowWidth(double endArrowWidth)` | Deprecated. this method is deprecated since version 8.4 and will be removed in the future. |
| `void` | `setEndX(double endx)` | Sets the x coordinate of the line end point. |
| `void` | `setEndY(double endy)` | Sets the y coordinate of the line end point. |
| `void` | `setEndZ(double endz)` | Sets the z coordinate of the line end point. |
| `void` | `setLineStyle(LineStyle lineStyle)` | Sets the style of the line: LINE\_STYLE\_SOLID, LINE\_STYLE\_DOTTED or LINE\_STYLE\_DASHED |
| `void` | `setLineWidth(double width)` | Sets the width of the line |
| `void` | `setZHeight(double zHeight)` | Sets the height of the shape along Z-axis |
