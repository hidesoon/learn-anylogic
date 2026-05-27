*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeComboBox.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeComboBox

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeComboBox

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeComboBox
extends ShapeInputControl
```

Combo box control.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeComboBox)

## Nested Class Summary

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `String` | `value` | The currently selected item of the combo box that can be accessed *in the overridden action() method*.  **Use [`getValue()`](#getValue()) to obtain the currently selected item from other places** |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeComboBox(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, boolean enabled, Font font, String[] items, boolean editable, ShapeControl.ValueType valueType)` | Creates a persistent combo box control. |
| `ShapeComboBox(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, Font font, String[] items, boolean editable, ShapeControl.ValueType valueType)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `getDoubleValue()` | Returns the current `double` value of the combo box.  Method throws an exception when the value isn't a number. |
| `int` | `getIntValue()` | Returns the current `int` value of the combo box.  Method throws an exception when the value isn't a number.  This method differs from [`getValueIndex()`](#getValueIndex()): it tries to parse the textual value as number |
| `String[]` | `getItems()` | Returns array of String items currently used in the combo box drop-down list  *The returned array should not be changed by user* |
| `String` | `getValue()` | Returns the currently selected text item. |
| `int` | `getValueIndex()` | Returns the index of the currently selected text item or `-1` when this is editable combobox and it doesn't contain entered value. |
| `void` | `setItems(String[] items)` | Sets new items for this combo box  This method preserves current combo box value: if it is *editable* if it is *not-editable* **and** current value is contained in new `texts` This method doesn't execute user action code (even if current selection changes)  This method throws an exception if this combo box has numeric value-type ([`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE) or [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT)) and some item(s) can't be parsed as a number. |
| `void` | `setItems(String[] items, boolean callAction)` | Sets new items for this combo box  This method preserves current combo box value: if it is *editable* if it is *not-editable* **and** current value is contained in new `texts` |
| `void` | `setValue(double value)` | Sets the numeric value of the combo box with value type [`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE) or [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT).  Doesn't execute user action code |
| `void` | `setValue(double value, boolean callAction)` | Sets the numeric value of the combo box with value type [`ShapeControl.TYPE_DOUBLE`](ShapeControl.md#TYPE_DOUBLE) or [`ShapeControl.TYPE_INT`](ShapeControl.md#TYPE_INT).  Executes user action code (if any exists) if `callAction` parameter is `true` |
| `void` | `setValue(String text)` | Sets the selected text item of the combo box.  Doesn't execute user action code |
| `void` | `setValue(String text, boolean callAction)` | Sets the selected text item of the combo box.  Executes user action code (if any exists) if `callAction` parameter is `true`.  If value-type is numeric and the given `text` isn't a valid number, nothing will be changed |
| `void` | `setValueIndex(int valueIndex)` | Selects the item with the given index.  Doesn't execute user action code |
| `void` | `setValueIndex(int valueIndex, boolean callAction)` | Selects the item with the given index.  Executes user action code (if any exists) if `callAction` parameter is `true`. |
