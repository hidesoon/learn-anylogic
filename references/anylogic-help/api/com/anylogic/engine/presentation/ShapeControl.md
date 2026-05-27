*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeControl.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeControl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeControl

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `Chart`, `ShapeInputControl`, `ShapeWindow3D`

---

```
public abstract class ShapeControl
extends Shape
implements com.anylogic.engine.internal.Child
```

The base class for all controls
(like buttons, sliders, text fields, and also charts).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeControl)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `ShapeControl.ValueType` |  |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final ShapeControl.ValueType` | `TYPE_DOUBLE` | Control value-type constant for `double` number editing mode, applicable for [`ShapeSlider`](ShapeSlider.md "class in com.anylogic.engine.presentation"), [`ShapeTextField`](ShapeTextField.md "class in com.anylogic.engine.presentation"), [`ShapeComboBox`](ShapeComboBox.md "class in com.anylogic.engine.presentation").  See constructors of these controls |
| `static final ShapeControl.ValueType` | `TYPE_INT` | Control value-type constant for `int` number editing mode, applicable for [`ShapeSlider`](ShapeSlider.md "class in com.anylogic.engine.presentation"), [`ShapeTextField`](ShapeTextField.md "class in com.anylogic.engine.presentation"), [`ShapeComboBox`](ShapeComboBox.md "class in com.anylogic.engine.presentation").  See constructors of these controls |
| `static final ShapeControl.ValueType` | `TYPE_STRING` | Control value-type constant for `String` editing mode, applicable for [`ShapeTextField`](ShapeTextField.md "class in com.anylogic.engine.presentation"), [`ShapeComboBox`](ShapeComboBox.md "class in com.anylogic.engine.presentation").  See constructors of these controls |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `action()` | Executes the action associated with the control. |
| `Shape` | `clone()` | **Cloning of controls is not supported**  (Other shapes except GIS and charts allow cloning)  This method throws `UnsupportedOperationException` if called |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `executeAction()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Point` | `getCenter()` | Returns (x, y) coordinates of the control center in 2D (returned z is the base-level of the control). |
| `double` | `getHeight()` | Returns the height of the control. |
| `Presentable` | `getPresentable()` | Returns the presentable object owning the control |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `double` | `getWidth()` | Returns the width of the control. |
| `boolean` | `isEnabled()` | Tests if the control is enabled or disabled. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `resetSVGComponent()` |  |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setEnabled(boolean yes)` | Sets the control enabled or disabled |
| `void` | `setHeight(double height)` | Sets the height of the control. |
| `void` | `setValueToDefault()` | Sets the value of the control to what was provided as the default one. |
| `void` | `setWidth(double width)` | Sets the width of the control. |
