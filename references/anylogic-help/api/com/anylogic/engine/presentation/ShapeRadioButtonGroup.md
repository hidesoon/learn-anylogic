*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeRadioButtonGroup.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeRadioButtonGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeRadioButtonGroup

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeRadioButtonGroup
extends ShapeInputControl
```

A group of radio buttons.
User's radio button group. Calls presentable object's executeControlAction( id,
index, index of the selected button ) method when a button is selected
(even if it was selected before). The orientation and the array of text
labels for buttons can only be set once when the group is created.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeRadioButtonGroup)

## Nested Class Summary

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `int` | `value` | The currently selected radio button (-1 if none) that can be accessed *in the overridden action() method*.  **Use [`getValue()`](#getValue()) to obtain the currently selected radio button from other places**. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeRadioButtonGroup(Presentable p, boolean ispublic, double x, double y, double width, double height, Color textColor, boolean enabled, Font font, boolean vertical, String[] texts)` | Creates a persistent radio button group control. |
| `ShapeRadioButtonGroup(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, boolean enabled, Font font, boolean vertical, String[] texts)` | Deprecated. may be removed in future releases |
| `ShapeRadioButtonGroup(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, Font font, boolean vertical, String[] texts)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `getValue()` | Returns the currently selected radio button, `-1` if none. |
| `void` | `setValue(int index)` | Sets the radio button with the given index selected, makes others deselected.  Doesn't execute user action code |
| `void` | `setValue(int index, boolean callAction)` | Sets the radio button with the given index selected, makes others deselected.  Executes user action code (if any exists) if `callAction` parameter is `true` |
