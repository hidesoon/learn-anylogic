*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeCheckBox.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeCheckBox

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeCheckBox

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeCheckBox
extends ShapeInputControl
```

Checkbox control.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeCheckBox)

## Nested Class Summary

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `boolean` | `value` | The current state of the check box (`true` means selected) that can be accessed *in the overridden action() method*.  **Use [`isSelected()`](#isSelected()) to obtain the current check box state from other places** |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeCheckBox(Presentable p, boolean ispublic, double x, double y, double width, double height, Color textColor, boolean enabled, Font font, String text)` | Creates a persistent checkbox control. |
| `ShapeCheckBox(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, boolean enabled, Font font, String text)` | Deprecated. may be removed in future releases |
| `ShapeCheckBox(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, Font font, String text)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `String` | `getText()` | Returns the checkbox label text. |
| `boolean` | `isSelected()` | Returns the selected state of the checkbox. |
| `void` | `setSelected(boolean yes)` | Sets the selected state of a persistent checkbox  Doesn't execute user action code |
| `void` | `setSelected(boolean yes, boolean callAction)` | Sets the selected state of a persistent checkbox  Executes user action code (if any exists) if `callAction` parameter is `true` |
| `void` | `setText(Object text)` | Sets the checkbox label text |
