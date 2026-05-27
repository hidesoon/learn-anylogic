*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeSVG.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeSVG

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeSVG

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeSVG
extends Shape
```

A custom SVG image rendered from the SVG XML provided by the user as a String object.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeSVG)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeSVG()` | Creates an empty SVG image with default properties: public, located at (0,0) and not rotated. |
| `ShapeSVG(boolean ispublic, double x, double y, double rotation, String svg)` | Creates an SVG image with specific properties |
| `ShapeSVG(String svg)` | Creates an SVG image with default properties: public, located at (0,0) and not rotated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `String` | `getSVG()` | Returns the current SVG image (XML format) or null |
| `void` | `removeSVG()` | Removes SVG image (same effect as setting it to null). |
| `void` | `setSVG(String svg)` | Sets the new SVG image |
