*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeCanvas.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeCanvas

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeCanvas

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeCanvas
extends Shape
```

A raster image whose pixels can be modified dynamically at runtime.
Maps directly to HTML5 canvas element and exposes a part of its API.
In contrast with vector graphics, any shapes drawn on the canvas become
a part of a raster image and cannot be accessed afterwards.
After creation (and after clearing), the canvas is transparent.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeCanvas)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeCanvas(boolean ispublic, double x, double y, double rotation, double width, double height)` | Constructs a canvas with specific attributes. |
| `ShapeCanvas(double width, double height)` | Constructs a canvas with given width and height, public visibility, x and y coordinates and rotation set to 0. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `clear()` | Clears the whole canvas (makes it fully transparent). |
| `void` | `clearRectangle(double x, double y, double width, double height)` | Clears a rectangle on the canvas (makes it fully transparent) |
| `boolean` | `contains(double px, double py)` | Tests if the canvas contains the point with the given coordinates |
| `void` | `fillCircle(double cx, double cy, double radius, Paint color)` | Fills a circle with the given color on the canvas, preserving transparency |
| `void` | `fillRectangle(double x, double y, double width, double height, Paint color)` | Fills a rectangle with the given color on the canvas, preserving transparency |
| `double` | `getHeight()` | Returns the height of the canvas. |
| `double` | `getWidth()` | Returns the width of the canvas. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `setGlobalCompositeOperation(String type)` | Sets the type of composing operation to apply when drawing new shapes, where type is a string identifying which of the composing or blending mode operations to use. |
| `void` | `setHeight(double height)` | Sets the height of the canvas. |
| `void` | `setSize(double width, double height)` | Sets the width and height of the canvas. |
| `void` | `setWidth(double width)` | Sets the width of the canvas. |
