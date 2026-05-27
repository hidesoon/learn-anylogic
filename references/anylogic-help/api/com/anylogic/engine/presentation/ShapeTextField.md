*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeTextField.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeTextField

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeTextField

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeTextField
extends ShapeInputControl
```

TextField control.
User's text field. Calls presentable object's executeControlAction( id, index, text );
method on focus lost or Enter pressed.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeTextField)

## Nested Class Summary

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `String` | `value` | The current text in the text field that can be accessed *in the overridden action() method*.  **Use [`getText()`](#getText()) to obtain the current text from other places**. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeTextField(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, boolean enabled, Font font)` | Creates a persistent text field control. |
| `ShapeTextField(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, boolean enabled, Font font, ShapeControl.ValueType valueType, double min, double max)` | Creates a persistent text field control. |
| `ShapeTextField(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, Font font)` | Deprecated. may be removed in future releases |
| `ShapeTextField(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, Font font, ShapeControl.ValueType valueType, double min, double max)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `getDoubleValue()` | Returns the current `double` value of the text field.  Method throws an exception when the value isn't a number. |
| `int` | `getIntValue()` | Returns the current `int` value of the text field.  Method throws an exception when the value isn't a number. |
| `double` | `getMax()` | Returns the maximum value of the text field.  This method may only be used in text fields with value type [`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE) or [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT) |
| `double` | `getMin()` | Returns the minimum value of the text field.  This method may only be used in text fields with value type [`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE) or [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT) |
| `String` | `getText()` | Returns the text of the text field. |
| `void` | `setBackgroundColor(Color backgroundColor)` | Sets the background color of this text field. |
| `void` | `setRange(double min, double max)` | Sets the minimum and maximum values of the text field with numeric value-type: [`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE), [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT).  Doesn't execute user action code  Leaving both min and max with zeroes will result in unlimited range.  If text field is configured to work with int values (see [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT)), the given `[min, max]` range may be automatically corrected to have integer bounds (within the given double bounds)  This method does nothing if the text field already has such range |
| `void` | `setRange(double min, double max, boolean callAction)` | Sets the minimum and maximum values of the text field with numeric value-type: [`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE), [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT).  If current text field value changes, executes user action code (if any exists) in the same thread - if `callAction` parameter is `true`  Leaving both min and max with zeroes will result in unlimited range.  If text field is configured to work with int values (see [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT)), the given `[min, max]` range may be automatically corrected to have integer bounds (within the given double bounds)  This method does nothing if the text field already has such range |
| `void` | `setText(double value)` | Sets the numeric value of the text field with value type [`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE) or [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT).  Doesn't execute user action code |
| `void` | `setText(double value, boolean callAction)` | Sets the numeric value of the text field with value type [`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE) or [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT).  Executes user action code (if any exists) if `callAction` parameter is `true` |
| `void` | `setText(String text)` | Sets the text of the text field  Doesn't execute user action code  If value-type is numeric and the given `text` isn't a valid number, nothing will be changed, and if `text` is a number but not within `[min, max]`, it will be corrected to `min` or `max` |
| `void` | `setText(String text, boolean callAction)` | Sets the text of the text field  Executes user action code (if any exists) if `callAction` parameter is `true`  If value-type is numeric and the given `text` isn't a valid number, nothing will be changed, and if `text` is a number but not within `[min, max]`, it will be corrected to `min` or `max` |
| `void` | `setTextColor(Color textColor)` | Sets the text color of this text field. |
