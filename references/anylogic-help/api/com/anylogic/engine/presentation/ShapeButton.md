*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeButton.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeButton

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeButton

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeButton
extends ShapeInputControl
```

Button control.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeButton)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeButton(Presentable p, boolean ispublic, double x, double y, double width, double height, Color textColor, boolean enabled, Font font, String text)` | Creates a persistent button control. |
| `ShapeButton(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, boolean enabled, Font font, String text)` | Deprecated. may be removed in future releases |
| `ShapeButton(Presentable p, boolean ispublic, double x, double y, double width, double height, Color backgroundColor, Color textColor, Font font, String text)` | Deprecated. may be removed in future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `executeUserAction(String value)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `String` | `getText()` | Returns the button label text. |
| `void` | `setText(Object text)` | Sets the button label text |
