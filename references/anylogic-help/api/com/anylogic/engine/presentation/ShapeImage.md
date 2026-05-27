*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeImage.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeImage

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeImage

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeImage
extends Shape3D
implements com.anylogic.engine.internal.Child
```

Persistent image shape.
The set of images is fixed during the lifetime of this object, but
you can control the index of the image to display.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeImage)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeImage(Presentable presentable, boolean ispublic, double x, double y, double rotation, double width, double height, String[] filenames)` | Deprecated. use [`ShapeImage(Presentable, boolean, double, double, double, double, double, String, String[])`](#%3Cinit%3E(com.anylogic.engine.Presentable,boolean,double,double,double,double,double,java.lang.String,java.lang.String%5B%5D)) |
| `ShapeImage(Presentable presentable, boolean ispublic, double x, double y, double rotation, double width, double height, String packagePrefix, String[] filenames)` | Constructs a 2D-only image shape with specific attributes. |
| `ShapeImage(Presentable presentable, ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, double width, double height, String packagePrefix, String[] filenames)` | Constructs an image shape with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(String filename)` | Adds an image to the image shape. |
| `ShapeImage` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getHeight()` | Returns the height of the image. |
| `int` | `getImageCount()` | Returns the number of the image files in this shape. |
| `String` | `getImageFileName(int i)` | Returns the file name of the image with the given index. |
| `List<String>` | `getImageFileNames()` | Returns the list of image file names of this image shape. |
| `int` | `getIndex()` | Returns the current index of the image being displayed. |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `double` | `getWidth()` | Returns the width of the image. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `remove(int i)` | Removes the image with the given index from the image shape. |
| `void` | `resetSVGComponent()` |  |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setHeight(double height)` | Sets the height of the image. |
| `void` | `setIndex(int index)` | Sets the index of the image to display. |
| `void` | `setSize(double width, double height)` | Sets the width and height of the image. |
| `void` | `setWidth(double width)` | Sets the width of the image. |
