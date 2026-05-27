*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeSlider.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeSlider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeSlider

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeSlider
extends ShapeInputControl
```

Slider control.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeSlider)

## Nested Class Summary

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `double` | `value` | The current value of the slider that can be accessed *in the overridden action() method*.  **Use [`getValue()`](#getValue()) to obtain the current slider value from other places** |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeSlider(Presentable p, boolean ispublic, double x, double y, double width, double height, boolean enabled, boolean vertical, double min, double max, double step, ShapeControl.ValueType valueType)` | Creates a persistent slider control. |
| `ShapeSlider(Presentable p, boolean ispublic, double x, double y, double width, double height, boolean enabled, boolean vertical, double min, double max, ShapeControl.ValueType valueType)` | Deprecated. |
| `ShapeSlider(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, boolean enabled, boolean vertical, double min, double max, ShapeControl.ValueType valueType)` | Deprecated. may be removed in future releases |
| `ShapeSlider(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, boolean vertical, double min, double max, ShapeControl.ValueType valueType)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `getIntValue()` | Returns the current `int` value of the slider.  This method may only be used in sliders with value type [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT) |
| `double` | `getMax()` | Returns the maximum value of the slider. |
| `double` | `getMin()` | Returns the minimum value of the slider. |
| `double` | `getStep()` | Returns the step of the slider. |
| `double` | `getValue()` | Returns the current value of the slider. |
| `void` | `setRange(double min, double max)` | Sets the minimum and maximum values of the slider.  Doesn't execute user action code  If slider is configured to work with int values (see [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT)), the given `[min, max]` range may be automatically corrected to have integer bounds (within the given double bounds)  This method does nothing if the slider already has such range |
| `void` | `setRange(double min, double max, boolean callAction)` | Sets the minimum and maximum values of the slider.  If the slider value appears out of range or not on the new step grid, it is brought within range and snapped to the grid. |
| `void` | `setStep(double step)` | Sets the step of the slider. |
| `void` | `setStep(double step, boolean callAction)` | Sets the step of the slider. |
| `void` | `setValue(double val)` | Sets the value of the slider. |
| `void` | `setValue(double val, boolean callAction)` | Sets the value of the slider.  If the value is out of range or not on the step grid (if any), sets the closest valid value. |
