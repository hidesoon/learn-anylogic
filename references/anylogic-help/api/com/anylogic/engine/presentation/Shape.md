*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Shape.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Shape

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.Shape

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Shape3D`, `ShapeCAD`, `ShapeCanvas`, `ShapeControl`, `ShapeEmbeddedObjectIcon`, `ShapeInspect`, `ShapeModelPrimitives`, `ShapeScale`, `ShapeSVG`

---

```
public abstract class Shape
extends Object
implements Locatable2D, Serializable, Cloneable, com.anylogic.engine.internal.Child, SVGElement, UsdElement, LevelElement
```

The base class for all graphical shapes and also for all
controls.
Shapes allow direct programmatic control, i.e. you can change the properties
of the shapes explicitly by calling their methods, e.g. setWidth().
Shape also has reference to the group they belong.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Shape)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `UNKNOWN_NAME` | This string is returned by [`getName()`](#getName()) for shapes with unknown names.  The value of this constant depends on the selected Engine language locale |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Shape()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `canHandleClick(boolean publicOnly)` | Checks if the shape can handle mouse clicks in its current condition, namely with current public and visibility settings. |
| `Shape` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `abstract boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ShapeDrawMode` | `getDrawMode()` | Returns the draw mode for this shape.  Either it is drawn in 2D animation only, or in 3D only, or both in 2D and 3D. |
| `ShapeGroup` | `getGroup()` | Returns the group containing this shape. |
| `Shape` | `getGroupOrOwner()` |  |
| `ShapeInspect` | `getInspect()` |  |
| `Level` | `getLevel()` | Returns the level containing this shape. |
| `String` | `getName()` | If the shape is declared as field in a presentable object class ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")), e.g. |
| `long` | `getOrGenerateUSDId()` |  |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `double` | `getRotation()` | Returns the rotation of the shape. |
| `double` | `getScaleX()` | Returns the scale of the shape along x axis |
| `double` | `getScaleY()` | Returns the scale of the shape along y axis |
| `long` | `getSVGId()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `long` | `getUsdVersion()` |  |
| `double` | `getX()` | Returns the x coordinate of the shape. |
| `double` | `getY()` | Returns the y coordinate of the shape. |
| `boolean` | `isJava2DSwingPresentation()` | Deprecated. |
| `boolean` | `isOnly3D()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isPublic_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isSVGPresentation()` | Deprecated. |
| `boolean` | `isVisible()` | Returns the visibility of the shape. |
| `boolean` | `isVisibleCurrently()` | Takes into account visibility of the [`Level`](../markup/Level.md "class in com.anylogic.engine.markup") |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `onClick(double clickx, double clicky)` | Should be overridden to define the shape reaction on mouse click. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside()` | Returns the randomly chosen point inside the shape area.  This method utilises Random Number Generator of the Presentable object containing this shape. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `removeSVGFromOwner(Shape oldOwner)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `removeSVGImage(List<SVGCommand> commands)` |  |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setChangedUsdVersion()` |  |
| `void` | `setInspect(ShapeInspect inspect)` |  |
| `void` | `setLevel(Level level)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setNextChangedUsdVersion()` | Used in changes during user interactive actions (that can happen during frame collecting) |
| `void` | `setPos(double x, double y)` | Sets both coordinates of the shape |
| `void` | `setPos(Point p)` | Sets both coordinates of the shape |
| `void` | `setPublic_xjal(boolean ispublic)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setRotation(double r)` | Sets the rotation of the shape. |
| `void` | `setScale(double s)` | Sets the same scale of the shape along all the axes |
| `void` | `setScale(double sx, double sy)` | Sets the scales of the shape along both axes |
| `void` | `setScaleX(double sx)` | Sets the scale of the shape along x axis |
| `void` | `setScaleY(double sy)` | Sets the scale of the shape along y axis |
| `void` | `setVisible(boolean v)` | Sets the visibility of the shape. |
| `void` | `setX(double x)` | Sets the x coordinate of the shape |
| `void` | `setY(double y)` | Sets the y coordinate of the shape |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
