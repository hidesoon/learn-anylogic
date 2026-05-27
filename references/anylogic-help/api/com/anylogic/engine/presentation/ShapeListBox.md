*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeListBox.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeListBox

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeListBox

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeListBox
extends ShapeInputControl
```

List box control.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeListBox)

## Nested Class Summary

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `String` | `value` | The currently selected item of the list box (or first item of multiselection) that can be accessed *in the overridden action() method*.  **Use [`getValue()`](#getValue()) to obtain the currently selected item from other places** |
| `String[]` | `values` | The currently selected items of the list box (in the multiple-selection mode) that can be accessed *in the overridden action() method*.  **Use [`getValues()`](#getValues()) to obtain the currently selected items from other places** |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeListBox(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, boolean enabled, Font font, String[] items, boolean multipleSelectionMode)` | Creates a persistent list box control. |
| `ShapeListBox(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, Font font, String[] items, boolean multipleSelectionMode)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `String[]` | `getItems()` | Returns array of String items currently in this list box. |
| `String` | `getValue()` | Returns the currently selected text item if in single-selection mode or the first selected text item if in multiple-selection mode Returns `null` if there is no selection. |
| `int` | `getValueIndex()` | Returns the index of the currently selected text item or `-1` when there is no selection. |
| `String[]` | `getValues()` | Returns an array of selected text items (for use in multiple-selection mode)  Returns empty array if there is no selection |
| `int[]` | `getValuesIndices()` | Returns an array of selected items' indices (for use in multiple-selection mode). |
| `void` | `setItems(String[] items)` | Sets new items for this list box  This method preserves current list box values if current values are contained in new `items`.  This method doesn't execute user action code (even if current selection changes).  Note that provided array is used internally and *shouldn't be changed by user* after this method is called. |
| `void` | `setItems(String[] items, boolean callAction)` | Sets new items for this list box. |
| `void` | `setValue(String text)` | Sets the selected text item of the list box.  Clears list box selection if text is `null`  Doesn't execute user action code |
| `void` | `setValue(String text, boolean callAction)` | Sets the selected text item of the list box. |
| `void` | `setValueIndex(int valueIndex)` | Selects the item with the given index.  Clears list box selection if valueIndex is `negative`.  Doesn't execute user action code |
| `void` | `setValueIndex(int valueIndex, boolean callAction)` | Selects the item with the given index. |
| `void` | `setValues(String[] texts)` | Sets the selected text items of the list box (in the multiple-selection mode)  Clears list box selection if `texts` is `null` or empty  Doesn't execute user action code |
| `void` | `setValues(String[] selectedTexts, boolean callAction)` | Sets the selected text items of the list box (in multiple-selection mode) Clears list box selection if `texts` is `null` or empty Executes user action code (if any exists) if `callAction` parameter is `true` |
| `void` | `setValuesIndices(int[] valuesIndices)` | Selects items with the given indices (in the multiple-selection mode)  Clears list box selection if `valuesIndices` is `null` or empty.  Doesn't execute user action code |
| `void` | `setValuesIndices(int[] valuesIndices, boolean callAction)` | Selects items with the given indices (in multiple-selection mode) Clears list box selection if `valuesIndices` is `null` or empty. |
