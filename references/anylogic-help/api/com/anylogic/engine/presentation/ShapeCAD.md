*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeCAD.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeCAD

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeCAD

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeCAD
extends Shape
implements com.anylogic.engine.internal.Child
```

Persistent CAD drawing shape.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeCAD)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeCAD(Presentable presentable, boolean ispublic, double x, double y, double width, double height, String packagePrefix, String filename, int id, Color backgroundColor, String[] layerNames, Color[] customLayerColors)` | Constructs a CAD drawing shape with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final ShapeCAD` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Color` | `getBackgroundColor()` |  |
| `Color` | `getCustomLayerColor(String layerName)` | Returns custom color of the layer's shapes, if the one is defined. |
| `double` | `getHeight()` | Returns the height of the shape. |
| `String` | `getImageFileName()` | Returns the file name of the CAD drawing. |
| `String[]` | `getLayerNames()` | Returns the array of layer names in this CAD, the returned array is backed by this shape and therefore shouldn't be modified by user. |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `double` | `getWidth()` | Returns the width of the shape. |
| `boolean` | `isLayerVisible(String layerName)` | Returns `true` if the layer with the given name is visible, otherwise returns `false`.  Returns `false` if layer with the given name isn't found. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `resetSVGComponent()` |  |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setBackgroundColor(Color backgroundColor)` |  |
| `void` | `setCustomLayerColor(String layerName, Color color)` | Sets custom color for all the shapes for the given layer. |
| `void` | `setHeight(double height)` | Sets the height of the shape. |
| `void` | `setLayerVisible(String layerName, boolean visible)` | Makes the layer with the given name visible/invisible.  Throws an error if layer with the given name isn't found. |
| `void` | `setVisibleLayers(String... layerNames)` | Makes the layers with given names visible and hides all other layers in this CAD.  Throws an error if layer(s) with the given name isn't found.  To show all the layers, please call `setVisibleLayers(getLayerNames())` |
| `void` | `setWidth(double width)` | Sets the width of the shape. |
